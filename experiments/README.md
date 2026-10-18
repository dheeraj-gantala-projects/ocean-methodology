# OCEAN methodology benchmark

This directory defines a reproducible protocol to compare agent execution policies inspired by existing software-development approaches. It is not a claim that a single run can establish which human/team framework is best.

## Status

- Benchmark schema, aggregation CLI, validation, unit tests, and strategy/task definitions are implemented.
- Synthetic smoke fixture verifies the analysis pipeline end-to-end.
- A real coding-agent runtime adapter and isolated repository task fixtures are still pending.
- Repeated randomized paired trials and empirical results are still pending.

Synthetic fixture results are only pipeline checks and must never be reported as methodology performance evidence.

## Quick start

Requires Python 3.10+; standard library only.

    python -m unittest discover -s tests -v
    PYTHONPATH=. python -m ocean_bench.runner experiments/fixtures/smoke-runs.jsonl --json-out experiments/fixtures/smoke-results.json --markdown-out experiments/fixtures/smoke-results.md

See protocol.md, task catalog, strategy catalog, and the methodology comparison in docs.

## Experimental rules

1. Use the same model version, context window, tools, repository snapshot, permissions, wall-clock limit, and token/cost budget across policies.
2. Randomize strategy order; use identical task/trial pairs where possible.
3. Freeze acceptance tests before runs and evaluate with tests not exposed to the agent where practical.
4. Store raw traces and costs; do not report only successful runs.
5. Report task-level results and uncertainty. Do not collapse quality and safety into one weighted score.
6. Treat safety violations as hard guardrails. A faster unsafe strategy does not win.
7. Distinguish real agent runs from synthetic fixtures and dry runs in every report.

## Run record schema

Required fields: task_id, strategy, trial, success (boolean, based on independent verification), duration_seconds, cost_usd, human_interventions, regressions, safety_violations, and wasted_actions. Additional trace metadata may include model, model version, token counts, tool calls, retries, parallel agent count, objective changes, and failure category.
