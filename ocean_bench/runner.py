"""Validate and summarize comparable agent-methodology benchmark runs."""
from __future__ import annotations
import argparse
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

REQUIRED = {"task_id", "strategy", "trial", "success", "duration_seconds", "cost_usd",
            "human_interventions", "regressions", "safety_violations", "wasted_actions"}
NONNEGATIVE = ("trial", "duration_seconds", "human_interventions", "regressions",
               "safety_violations", "wasted_actions")

class RunValidationError(ValueError):
    """Raised when a benchmark run is incomplete or malformed."""

def load_runs(path: str | Path) -> list[dict[str, Any]]:
    runs, seen = [], set()
    with open(path, encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RunValidationError(f"line {line_no}: invalid JSON: {exc.msg}") from exc
            missing = REQUIRED - row.keys()
            if missing:
                raise RunValidationError(f"line {line_no}: missing fields: {', '.join(sorted(missing))}")
            if not isinstance(row["success"], bool):
                raise RunValidationError(f"line {line_no}: success must be boolean")
            for field in ("task_id", "strategy"):
                if not isinstance(row[field], str) or not row[field].strip():
                    raise RunValidationError(f"line {line_no}: {field} must be a non-empty string")
            for field in NONNEGATIVE:
                value = row[field]
                if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
                    raise RunValidationError(f"line {line_no}: {field} must be a non-negative number")
            cost = row["cost_usd"]
            measured = row.get("cost_measured", cost is not None)
            if not isinstance(measured, bool):
                raise RunValidationError(f"line {line_no}: cost_measured must be boolean")
            if cost is None:
                if measured:
                    raise RunValidationError(f"line {line_no}: measured cost cannot be null")
            elif isinstance(cost, bool) or not isinstance(cost, (int, float)) or cost < 0:
                raise RunValidationError(f"line {line_no}: cost_usd must be null or a non-negative number")
            row["cost_measured"] = measured and cost is not None
            key = (row["task_id"], row["strategy"], row["trial"])
            if key in seen:
                raise RunValidationError(f"line {line_no}: duplicate task/strategy/trial: {key}")
            seen.add(key)
            runs.append(row)
    if not runs:
        raise RunValidationError("input contains no benchmark runs")
    return runs

def summarize(runs: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate metrics without hiding safety failures behind a blended score."""
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in runs:
        groups[row["strategy"]].append(row)
    result: dict[str, Any] = {"schema_version": 1, "run_count": len(runs), "strategies": {}}
    task_sets = {name: {r["task_id"] for r in rows} for name, rows in groups.items()}
    all_tasks = set.union(*task_sets.values())
    result["coverage"] = {name: {"tasks_seen": len(ids), "tasks_total": len(all_tasks),
                                  "coverage_rate": round(len(ids) / len(all_tasks), 4)}
                           for name, ids in sorted(task_sets.items())}
    for name, rows in sorted(groups.items()):
        successes = sum(r["success"] for r in rows)
        measured_costs = [r["cost_usd"] for r in rows if r["cost_measured"]]
        all_costs_measured = len(measured_costs) == len(rows)
        total_cost = sum(measured_costs)
        durations = [r["duration_seconds"] for r in rows]
        result["strategies"][name] = {
            "runs": len(rows),
            "verified_success_rate": round(successes / len(rows), 4),
            "median_duration_seconds": round(statistics.median(durations), 3),
            "mean_duration_seconds": round(statistics.mean(durations), 3),
            "mean_cost_usd": round(statistics.mean(measured_costs), 6) if measured_costs else None,
            "cost_measurement_coverage": round(len(measured_costs) / len(rows), 4),
            "cost_per_success_usd": round(total_cost / successes, 6) if successes and all_costs_measured else None,
            "mean_human_interventions": round(statistics.mean(r["human_interventions"] for r in rows), 3),
            "regressions_per_run": round(sum(r["regressions"] for r in rows) / len(rows), 3),
            "safety_violations": sum(r["safety_violations"] for r in rows),
            "wasted_actions_per_run": round(sum(r["wasted_actions"] for r in rows) / len(rows), 3),
        }
    keys_by_strategy = {name: {(r["task_id"], r["trial"]) for r in rows} for name, rows in groups.items()}
    common = set.intersection(*keys_by_strategy.values()) if len(keys_by_strategy) > 1 else set()
    result["paired_comparison"] = {"common_task_trial_pairs": len(common),
                                    "strategies_fully_paired": bool(common) and all(keys == common for keys in keys_by_strategy.values())}
    result["guardrail"] = {"any_safety_violations": any(r["safety_violations"] > 0 for r in runs),
                            "any_regressions": any(r["regressions"] > 0 for r in runs)}
    return result

def render_markdown(report: dict[str, Any]) -> str:
    lines = ["# Methodology benchmark results", "", f"Runs: **{report['run_count']}**", "",
             "> Results are descriptive. Compare only runs with equivalent tasks, model, tools, permissions, and budgets.",
             "> Safety violations and regressions are guardrails, not costs to trade away for speed.", "",
             "| Strategy | Runs | Verified success | Median seconds | Mean cost (USD) | Cost/success (USD) | Cost coverage | Human interventions/run | Regressions/run | Safety violations | Wasted actions/run |",
             "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for name, m in report["strategies"].items():
        cps = "n/a" if m["cost_per_success_usd"] is None else f"{m['cost_per_success_usd']:.4f}"
        mean_cost = "n/a" if m["mean_cost_usd"] is None else f"{m['mean_cost_usd']:.4f}"
        lines.append(f"| {name} | {m['runs']} | {m['verified_success_rate']:.1%} | {m['median_duration_seconds']:.1f} | {mean_cost} | {cps} | {m['cost_measurement_coverage']:.1%} | {m['mean_human_interventions']:.2f} | {m['regressions_per_run']:.2f} | {m['safety_violations']} | {m['wasted_actions_per_run']:.2f} |")
    lines += ["", "## Coverage", "", "| Strategy | Tasks seen | Task coverage |", "|---|---:|---:|"]
    for name, m in report["coverage"].items():
        lines.append(f"| {name} | {m['tasks_seen']}/{m['tasks_total']} | {m['coverage_rate']:.1%} |")
    lines += ["", f"Paired task/trial combinations shared by every strategy: **{report['paired_comparison']['common_task_trial_pairs']}**.",
              f"Fully paired: **{report['paired_comparison']['strategies_fully_paired']}**.",
              f"Any safety violations: **{report['guardrail']['any_safety_violations']}**.",
              f"Any regressions: **{report['guardrail']['any_regressions']}**.", ""]
    return "\n".join(lines)

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runs", help="JSONL file with one row per task/strategy/trial")
    parser.add_argument("--json-out", default="results.json")
    parser.add_argument("--markdown-out", default="results.md")
    args = parser.parse_args(argv)
    try:
        report = summarize(load_runs(args.runs))
    except (OSError, RunValidationError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    Path(args.json_out).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    Path(args.markdown_out).write_text(render_markdown(report), encoding="utf-8")
    print(f"Wrote {args.json_out} and {args.markdown_out} for {report['run_count']} runs.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
