# Comparing OCEAN with established approaches

## Purpose and limits

OCEAN is a new proposal, not an established methodology. Its value must be established empirically. The comparison below identifies useful baselines and translates selected principles into **agent execution policies**. It does not claim to reproduce full human/team methodologies in an LLM prompt.

## Methodologies to compare

| Approach | What it contributes | Agent-oriented operationalization | Likely strengths to test | Likely risks to test |
|---|---|---|---|---|
| OCEAN (proposal) | Objective-centered execution, uncertainty-aware exploration, adaptive work graph, evidence-backed completion, bounded autonomy | Clarify goal and constraints, observe, maintain a provisional graph, adapt to evidence, independently verify | Uncertain and changing multi-step tasks | Planning overhead, excess exploration, over-complex graph management |
| Scrum (framework) | Product/Sprint Goals, bounded iterations, inspection and adaptation | Work toward a defined iteration goal, inspect increment against a Definition of Done, adapt the next iteration | Coherent increments, inspectable progress | Artificial iteration boundaries or overhead on tiny tasks |
| Kanban (flow method) | Visualize and manage flow, explicit policies, WIP limits, flow improvement | Pull ready work from a queue with WIP limit and explicit blocked/done states | Continuous streams, reducing context switching | Queue priority can be wrong when new information changes the objective |
| Extreme Programming (XP) | Engineering practices such as test-first development, small releases, continuous integration, refactoring | Test-first small changes and frequent integration; no fake pair-programming unless a second agent actually participates | Regression prevention, localized code changes | Test-writing overhead where test harnesses are poor; test gaming |
| Waterfall (sequential lifecycle) | Requirements/design/implementation/verification stages and explicit change control | Freeze an initial specification and plan; proceed through staged gates; record changes to earlier stages | Stable, well-specified tasks and auditability | Expensive rework when assumptions change |
| Lean software development | Value focus, waste reduction, small batches, fast feedback, built-in quality, learning | Prefer small reversible experiments; measure value and waste; limit WIP and improve from feedback | Cost efficiency and minimizing unnecessary work | Misclassifying exploration or verification as waste |
| Fixed-plan control (experimental) | Deliberately non-adaptive control group | Plan once, execute in order, deviate only if blocked or safety requires it | Measures whether adaptation adds value at all | Brittle behavior under uncertainty |

Sources describe Scrum as a framework, not a complete prescriptive methodology; Kanban is a flow-management method; XP emphasizes a network of engineering practices. For that reason, benchmark labels use “inspired” where the agent policy is only a partial operationalization.

## Research-backed measurement choices

The benchmark combines methodology-specific questions with software delivery and coding-agent evaluation lessons:

- DORA's software delivery performance measures include change lead time, deployment frequency, failed deployment recovery time, change fail rate, and deployment rework rate. These are useful when a benchmark includes deployment/release workflows, but they are not substitutes for per-task correctness metrics.
- SWE-bench evaluates coding agents against repository-level software issues. The OCEAN pilot should borrow the idea of a pinned repository state plus executable tests, while keeping tasks and hidden acceptance tests independent from the agent's own completion claim.
- Research on benchmark reliability warns that flawed tasks, exposed solutions/tests, and reward hacking can inflate apparent agent performance. Therefore, freeze acceptance tests, use isolated environments, preserve traces, and report failures.
- A methodology comparison must hold the model, tools, permissions, repository snapshot, time/cost budget, and acceptance tests constant wherever possible. Otherwise, the result confounds methodology with agent capability or environment.

## What counts as evidence for OCEAN?

Evidence must come from real, repeated agent runs—not from the synthetic fixture bundled with the benchmark. The synthetic fixture only verifies that the result pipeline parses records, calculates metrics, and flags guardrail failures.

Pre-register hypotheses, run paired trials on the same tasks, stratify by task type and uncertainty, and report both successful and failed runs. A small pilot is exploratory, not proof of superiority. If OCEAN helps uncertain investigations but loses on simple tasks, the practical outcome may be task-dependent policy selection rather than a universal winner.

## References

1. Scrum Guide, official current guide: https://scrumguides.org/download.html
2. The Kanban Guide, official May 2025 edition: https://kanbanguides.org/the-kanban-guide/translations/
3. Agile Alliance, Extreme Programming (XP): https://agilealliance.org/glossary/xp/
4. DORA, software delivery performance metrics: https://dora.dev/guides/dora-metrics/
5. SWE-bench project: https://github.com/swe-bench
6. SWE-bench Pro paper, long-horizon software engineering tasks: https://arxiv.org/abs/2509.16941
7. SWE-Bench Pro Verified, reliability concerns and task validation (2026): https://arxiv.org/abs/2609.08149
