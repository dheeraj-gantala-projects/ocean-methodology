# Task catalog

Three executable Python tasks currently ship with starter code, public tests, a prompt, and evaluator tests kept outside the agent workspace.

| ID | Category | Task shape | Key discriminator |
|---|---|---|---|
| simple-bug-fix | Low uncertainty | Repair percentage discount calculation | Detects adaptation/planning overhead on a localized bug. |
| uncertain-diagnosis | High uncertainty | Correct retry delay/backoff policy and validation | Tests interpretation of a policy defect and edge cases. |
| dependency-heavy-feature | Integration-like feature | Implement bounded slug normalization | Tests requirements coverage and edge cases in a new utility. |
| changing-conditions | Dynamic | New evidence invalidates part of a sub-plan | Specification only; fixture pending. |
| tool-failure-budget | Resilience | Tool failure under fixed resource budget | Specification only; fixture pending. |
| safety-boundary | Governance | Stop and request approval before forbidden action | Specification only; fixture pending. |

The first three are deliberately small pilot tasks, not a validated broad benchmark suite. Add multiple independent tasks per stratum before making general claims. Hidden acceptance tests must remain outside the agent's working directory and be independently reviewed.
