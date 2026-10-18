# OCEAN methodology benchmark

This directory defines a reproducible protocol to compare agent execution policies inspired by existing software-development approaches. It is not a claim that a single run can establish which human/team framework is best.

## Status

- Implemented: JSONL metric aggregation, validation tests, a generic CLI agent adapter, three executable bug-fix/diagnosis/feature tasks, hidden acceptance tests, strategy policy prompts, and a harness-only deterministic test double.
- CI unit tests include end-to-end execution of the adapter against all three tasks using the known-good test double.
- Still pending: connect a real coding-agent runtime, run repeated randomized paired trials, and publish empirical results.
- The deterministic test double is only a harness test. Its scores must never be presented as methodology performance evidence.

## Quick start

Requires Python 3.10+; standard library only.

    python -m unittest discover -s tests -v
    PYTHONPATH=. python -m ocean_bench.runner experiments/fixtures/smoke-runs.jsonl --json-out /tmp/smoke-results.json --markdown-out /tmp/smoke-results.md

Run a real agent CLI that reads the task prompt from stdin:

    python experiments/run_agent.py --task simple-bug-fix --strategy ocean --agent-command "your-agent-wrapper" --trial 1 --output results/live-runs.jsonl

Replace your-agent-wrapper with a local adapter for your chosen coding agent. The adapter must read the prompt from stdin and edit files in the current working directory. To report cost accurately, it should write JSON to the OCEAN_RUN_METADATA_PATH environment variable; at minimum include cost_usd. Unknown costs are stored as null and are not reported as zero.

The generic runner launches the command in a temporary workspace and evaluates it against tests stored outside that workspace. This is isolation from accidental test edits, not a security sandbox. Run untrusted agents inside a disposable container/VM with restricted network, filesystem, credentials, and process access.

## Available executable tasks

- simple-bug-fix: percentage discount calculation, including invalid input behavior.
- uncertain-diagnosis: capped exponential retry backoff, including invalid parameters.
- dependency-heavy-feature: bounded slug normalization, punctuation runs, truncation, and invalid lengths.

Task starter files and public tests are copied to the agent workspace. Acceptance tests remain outside that workspace and are executed after the agent exits. The task names are benchmark strata, not claims that the task perfectly represents that whole category.

## Experimental rules

1. Use the same model version, tools, system-level coding instructions, repository snapshot, permissions, wall-clock limit, and cost/token budget across policies.
2. Randomize strategy order; use identical task/trial pairs where possible.
3. Freeze acceptance tests before runs and do not expose evaluator files to the agent.
4. Store raw traces and measured costs; never fabricate missing cost data.
5. Report task-level results and failures, not only averages.
6. Treat safety violations as hard guardrails. A faster unsafe strategy does not win.
7. Clearly distinguish harness tests, synthetic fixtures, and real agent runs in every report.
