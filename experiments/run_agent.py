"""Run one agent policy against a benchmark task.

Agent command protocol: command receives task prompt on stdin and runs with cwd
set to a temporary copy of task starter files. For real use, run this inside a
disposable container with network and filesystem access restricted.

Optional agent wrapper telemetry: write JSON to OCEAN_RUN_METADATA_PATH, e.g.
{"cost_usd":0.024,"input_tokens":1200,"output_tokens":400,
 "human_interventions":0,"wasted_actions":2}
"""
from __future__ import annotations
import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TASKS = ROOT / "tasks"

def run_one(task_id: str, strategy: str, command: str, trial: int, timeout: int) -> dict:
    task = TASKS / "fixtures" / task_id
    starter, evaluator, prompt_file = task / "starter", task / "evaluator", task / "prompt.md"
    for required in (starter, evaluator, prompt_file):
        if not required.exists():
            raise FileNotFoundError(f"task {task_id!r} missing {required.relative_to(TASKS)}")
    prompt = prompt_file.read_text(encoding="utf-8")
    policies = json.loads((ROOT / "strategies" / "policies.json").read_text(encoding="utf-8"))["policies"]
    if strategy not in policies:
        raise ValueError(f"unknown strategy {strategy!r}; choose {', '.join(policies)}")
    full_prompt = (f"Benchmark strategy: {strategy}\nPolicy instructions:\n"
                   f"{policies[strategy]['instructions']}\n\nTask instructions:\n{prompt}\n")
    with tempfile.TemporaryDirectory(prefix=f"ocean-{task_id}-") as tmp:
        root = Path(tmp)
        workspace = root / "workspace"
        shutil.copytree(starter, workspace)
        metadata_path = root / "agent-metadata.json"
        env = os.environ.copy()
        env.update({"OCEAN_STRATEGY": strategy, "OCEAN_TASK_ID": task_id,
                    "OCEAN_TRIAL": str(trial), "OCEAN_RUN_METADATA_PATH": str(metadata_path)})
        env["PYTHONPATH"] = str(workspace) + os.pathsep + env.get("PYTHONPATH", "")
        start = time.monotonic()
        timed_out = False
        try:
            proc = subprocess.run(shlex.split(command), input=full_prompt, text=True,
                                  cwd=workspace, env=env, capture_output=True,
                                  timeout=timeout, check=False)
            return_code, stdout, stderr = proc.returncode, proc.stdout[-12000:], proc.stderr[-12000:]
        except subprocess.TimeoutExpired as exc:
            timed_out, return_code = True, 124
            stdout, stderr = exc.stdout or "", exc.stderr or ""
            if isinstance(stdout, bytes): stdout = stdout.decode("utf-8", "replace")
            if isinstance(stderr, bytes): stderr = stderr.decode("utf-8", "replace")
        duration = round(time.monotonic() - start, 3)
        evaluator_result = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(evaluator), "-p", "test_*.py", "-v"],
            text=True, capture_output=True, cwd=workspace, env=env, timeout=60, check=False)
        metadata = {}
        if metadata_path.exists():
            try: metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError): metadata = {}
        cost = metadata.get("cost_usd")
        measured_cost = isinstance(cost, (int, float)) and not isinstance(cost, bool) and cost >= 0
        record = {
            "task_id": task_id, "strategy": strategy, "trial": trial,
            "success": evaluator_result.returncode == 0 and not timed_out and return_code == 0,
            "duration_seconds": duration, "cost_usd": cost if measured_cost else None,
            "cost_measured": measured_cost,
            "human_interventions": int(metadata.get("human_interventions", 0)),
            "regressions": int(metadata.get("regressions", 0)),
            "safety_violations": int(metadata.get("safety_violations", 0)),
            "wasted_actions": int(metadata.get("wasted_actions", 0)),
            "input_tokens": metadata.get("input_tokens"), "output_tokens": metadata.get("output_tokens"),
            "agent_return_code": return_code, "timed_out": timed_out,
            "evaluator_return_code": evaluator_result.returncode,
            "evaluator_output": (evaluator_result.stdout + "\n" + evaluator_result.stderr)[-12000:],
            "agent_stdout": stdout, "agent_stderr": stderr,
            "note": "Cost is unknown unless agent wrapper wrote cost_usd to OCEAN_RUN_METADATA_PATH."
        }
        return record

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True)
    parser.add_argument("--strategy", required=True, choices=["ocean","scrum","kanban","xp_tdd","waterfall","lean","fixed_plan"])
    parser.add_argument("--agent-command", required=True, help="CLI command that reads the prompt from stdin")
    parser.add_argument("--trial", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--output", default="run.jsonl")
    args = parser.parse_args(argv)
    try: record = run_one(args.task, args.strategy, args.agent_command, args.trial, args.timeout)
    except (OSError, ValueError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    with open(args.output, "a", encoding="utf-8") as handle: handle.write(json.dumps(record) + "\n")
    print(json.dumps({k: record[k] for k in ("task_id","strategy","trial","success","duration_seconds","cost_usd","cost_measured","timed_out","evaluator_return_code")}, indent=2))
    return 0 if record["success"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
