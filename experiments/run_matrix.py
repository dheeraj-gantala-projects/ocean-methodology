"""Run a randomized, paired matrix across policies and task fixtures."""
from __future__ import annotations
import argparse
import json
import random
import sys
from pathlib import Path
from run_agent import ROOT, run_one

DEFAULT_TASKS = ["simple-bug-fix", "uncertain-diagnosis", "dependency-heavy-feature"]
DEFAULT_STRATEGIES = ["ocean", "scrum", "kanban", "xp_tdd", "waterfall", "lean", "fixed_plan"]

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent-command", required=True, help="CLI command that reads prompt from stdin")
    parser.add_argument("--tasks", nargs="+", default=DEFAULT_TASKS)
    parser.add_argument("--strategies", nargs="+", default=DEFAULT_STRATEGIES)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--seed", type=int, default=20261018)
    parser.add_argument("--output", default="results/live-runs.jsonl")
    args = parser.parse_args(argv)
    if args.trials < 1:
        parser.error("--trials must be at least 1")
    policies = json.loads((ROOT / "strategies" / "policies.json").read_text(encoding="utf-8"))["policies"]
    unknown = set(args.strategies) - policies.keys()
    if unknown:
        parser.error(f"unknown strategies: {', '.join(sorted(unknown))}")
    for task in args.tasks:
        if not (ROOT / "tasks" / "fixtures" / task).is_dir():
            parser.error(f"unknown executable task: {task}")
    schedule = [(task, strategy, trial)
                for trial in range(1, args.trials + 1)
                for task in args.tasks for strategy in args.strategies]
    random.Random(args.seed).shuffle(schedule)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("", encoding="utf-8")  # each invocation produces one clean matrix
    completed, failed = 0, 0
    for task, strategy, trial in schedule:
        try:
            record = run_one(task, strategy, args.agent_command, trial, args.timeout)
        except Exception as exc:
            print(f"ERROR task={task} strategy={strategy} trial={trial}: {exc}", file=sys.stderr)
            failed += 1
            continue
        with output.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record) + "\n")
        completed += 1
        failed += not record["success"]
        print(f"{completed}/{len(schedule)} task={task} strategy={strategy} trial={trial} "
              f"success={record['success']} cost={record['cost_usd']}")
    print(f"Finished: {completed} recorded, {failed} failed/incomplete. Raw records: {output}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
