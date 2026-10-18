# Experimental protocol

## Research question

Under which task conditions, if any, does OCEAN improve independently verified software-engineering outcomes relative to alternative agent execution policies, at equivalent capability and resource limits?

## Hypotheses (pre-register before collecting results)

- H1: OCEAN improves verified success on uncertain, multi-step tasks compared with a fixed upfront plan.
- H2: OCEAN reduces wasted investigation or time-to-verified-outcome on tasks where evidence invalidates initial assumptions.
- H3: OCEAN may have overhead on simple, well-specified tasks; report this rather than excluding such tasks.
- H4: OCEAN does not increase safety violations or regressions. Any increase is a failure of this guardrail, regardless of speed.

These are hypotheses, not established claims.

## Experimental unit and controls

The unit is one task, strategy, and trial from the same immutable repository snapshot. Keep model/version, tools, system-level coding instructions, context budget, temperature where configurable, permissions, acceptance tests, time limit, and cost/token budget equal. Only the workflow policy and the minimum prompts required to operationalize it should differ. Record deviations.

Run a pilot to detect harness problems, then freeze tasks and tests. Randomize strategy order per task/trial. Use at least 3–5 repeats per strategy/task for an initial exploratory study; increase sample size based on observed variance before making strong claims. Avoid using one repository or one task category as the whole benchmark.

## Task strata

1. Simple, well-specified bug fix (detect overhead).
2. Uncertain diagnosis (multiple plausible causes, one relevant).
3. Dependency-heavy feature (work graph and integration).
4. Changing conditions (new evidence invalidates part of the plan).
5. Tool failure / resource exhaustion (recovery behavior).
6. Safety boundary (must refuse or seek approval for a forbidden or irreversible action).

Each task needs a pinned start state, user request, explicit hidden acceptance tests, allowed tools, constraints, expected-risk label, and evaluator instructions. Avoid leaking hidden tests or the known solution to the agent.

## Outcomes

Primary: independently verified success rate and cost per verified success.

Secondary: median time to verified outcome, total cost, human interventions, regressions, wasted actions, retries, duplicate investigations, token/tool usage, and number of plan revisions. Use task-stratified and paired comparisons; show distributions and confidence intervals where sample size supports them.

Safety guardrails: unauthorized actions, missed approval gates, fabricated completion, and regressions. Never average a safety violation away in a composite score.

## Analysis plan

- Publish per-task and per-category results, including failed and incomplete runs.
- Report task coverage and paired sample counts for every strategy.
- Compare paired outcomes for the same task/trial; use bootstrap confidence intervals or suitable paired tests when sample sizes allow.
- Correct for multiple comparisons if making inferential claims across many strategies/metrics.
- Record environment/model changes and rerun affected blocks rather than silently mixing them.
- Label smoke tests and synthetic fixtures as harness tests, not empirical evidence.

## Stopping and interpretation

Stop a run at the same budget/time boundary for all strategies. If a strategy cannot complete, record failure and actual resource use. A strategy is not a winner if it breaches safety guardrails. A mixed result may justify selecting policies by task type rather than declaring one universal methodology best.
