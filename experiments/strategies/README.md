# Strategy adapters

Each strategy must have the same external tool interface and acceptance criteria. These are agent-oriented operationalizations inspired by the named approaches, not claims to implement every aspect of the original team framework.

| Strategy ID | Policy | Operationalized rule |
|---|---|---|
| ocean | OCEAN | Explicit objective/constraints, observe and clarify, provisional adaptive work graph, evidence-led replanning, independent verification. |
| scrum | Scrum-inspired iteration | Goal and bounded iteration; select a coherent increment, inspect at iteration end, adapt the next iteration. No human-only ceremonies required in the agent loop. |
| kanban | Kanban-inspired flow | Pull next ready work, explicit states/dependencies, WIP limit, optimize flow and blocked-work visibility; replan through queue policies. |
| xp_tdd | XP/TDD-inspired | Test-first loop, small changes, continuous integration, refactoring only with tests green; prioritize tight feedback. Pair programming is represented only if a second agent is actually used. |
| waterfall | Sequential staged plan | Requirements/specification, design, implementation, verification; changes to earlier stages require explicit change control. |
| lean | Lean-inspired | Identify value and waste, prefer smallest useful experiment/change, limit work in progress, inspect outcomes and eliminate recurring waste. |
| fixed_plan | Fixed-plan control | Produce a plan once, then execute it in order; only deviate when blocked or a safety rule requires it. This is an experimental control, not a named industry methodology. |

Keep policy-specific prompts short and publish them verbatim. Record any adapter differences that could confound results.
