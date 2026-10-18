# Metrics and evaluation

OCEAN is a hypothesis that must be tested. A convincing demo is not enough: evaluation should include normal cases, ambiguous tasks, failures, and cases where autonomy should stop or ask for help.

## Primary outcomes

- **Verified success rate:** fraction of objectives meeting all required criteria.
- **Time to verified outcome:** elapsed time from accepted objective to verified result.
- **Cost per verified outcome:** total model, tool, infrastructure, and coordination cost divided by successful objectives.
- **Human intervention rate:** frequency and type of human decisions needed during execution.
- **Rework and duplication:** effort spent repeating work or reconciling conflicting attempts.
- **Regression rate:** fraction of completed changes that fail follow-up or integration checks.
- **Safety violations:** unauthorized actions, policy breaches, or constraint violations.

Track distributions and confidence intervals where practical, not only averages. Segment by task difficulty, risk, objective ambiguity, and required tool access.

## Baseline design

Compare OCEAN with a relevant baseline such as sprint-managed execution, Kanban-style flow, or a fixed agent workflow. Use comparable objectives, models, tools, permissions, and resource budgets. Randomize task assignment when feasible and run multiple trials to account for model variability.

## Task set

Include routine tasks, uncertain investigations, dependent parallel tasks, ambiguous objectives, failing tools, budget exhaustion, adversarial inputs, and objectives where the correct action is to stop or request approval.

## Fairness and reproducibility

Record model and tool versions, prompts or policies, task inputs, environment, budgets, number of attempts, evaluation criteria, and exclusions. Keep acceptance checks independent from the system being evaluated where possible.

## Reporting

Report failed runs, variance, limitations, and tradeoffs. Do not infer broad superiority from a small demonstration or cherry-picked tasks. A valid result may show that OCEAN helps some task classes and performs worse on others.

## Adoption gate

Adopt OCEAN for a task class only when improvements in outcome quality, speed, or total cost justify added complexity without unacceptable safety or reliability regressions.
