# OCEAN

**Objective-Centered Execution and Adaptive Navigation** is a proposed operating methodology for AI-agent-driven work. It organizes execution around measurable objectives, explicit constraints, adaptive planning, efficient agent coordination, and independently verified outcomes—not around mandatory sprint cycles or static task plans.

> **Status:** Experimental proposal. OCEAN is not an established standard, and its effectiveness has not yet been demonstrated. This repository defines a methodology and a plan to test it.

## Why OCEAN?

Many software delivery practices assume people plan work in advance, manually assign tasks, coordinate through meetings, and review progress on a calendar. Agents introduce different opportunities—and different failure modes. They can work continuously, explore alternatives, and execute tasks in parallel, but they can also waste compute, repeat failed work, misinterpret goals, and declare success without sufficient evidence.

OCEAN proposes an alternative: give the system a well-defined objective and constraints, let it choose and adapt its execution strategy, and require evidence that the outcome meets its acceptance criteria.

## The OCEAN loop

1. **Observe** — Gather relevant state, history, capabilities, dependencies, and missing information.
2. **Clarify** — Define the objective, success criteria, invariants, risk boundaries, and resource budgets.
3. **Explore** — Generate candidate approaches and select useful next actions; build a provisional work graph.
4. **Act and adapt** — Execute permitted work, coordinate when useful, and revise the plan as evidence changes.
5. **Normalize and verify** — Integrate results, independently verify acceptance criteria, record evidence, and update shared state.

This is a feedback loop, not a linear lifecycle. A failed verification can return the system to any earlier phase.

## Core principles

- **Outcomes over task lists:** specify what success means; do not require every step to be known upfront.
- **Uncertainty-aware decisions:** gather information when it can materially improve the choice of action.
- **Dynamic work graphs:** add, split, reprioritize, block, or abandon work as the situation changes.
- **Economical coordination:** use parallel agents only when expected benefit exceeds coordination and compute costs.
- **Evidence-backed completion:** an agent's claim is not, by itself, proof that an objective is achieved.
- **Bounded autonomy:** policies, budgets, permissions, deadlines, and approval gates are enforced outside the agent's discretion.
- **Validated learning:** improve future strategies from execution history without turning isolated successes into universal rules.

## Quick start

To apply OCEAN to a project:

1. Write one objective with measurable success criteria.
2. Document constraints, non-goals, risk boundaries, and resource budgets.
3. Observe the current environment and list consequential unknowns.
4. Generate a provisional graph of investigations, experiments, and implementation work.
5. Choose the next action by expected progress, information value, cost, dependencies, and risk.
6. Execute within permissions and budgets; collect structured results.
7. Verify outcomes independently. Continue, adapt, stop, or escalate based on evidence.

Start with [the operating model](docs/operating-model.md), [objective specification](docs/objectives-and-constraints.md), and [decision policy](docs/decision-policy.md).

## Documentation

| Document | Purpose |
|---|---|
| [Methodology overview](docs/methodology.md) | Scope, vocabulary, intended use, and relationship to existing approaches |
| [Operating model](docs/operating-model.md) | The OCEAN loop and transitions between phases |
| [Objectives and constraints](docs/objectives-and-constraints.md) | Writing goals that are measurable, bounded, and verifiable |
| [Adaptive work graph](docs/adaptive-work-graph.md) | Dynamic decomposition, dependencies, and parallelism |
| [Decision policy](docs/decision-policy.md) | Selecting the next action under uncertainty and limited resources |
| [Agent coordination](docs/agent-coordination.md) | Delegation, shared findings, ownership, and conflict handling |
| [Verification and evidence](docs/verification-and-evidence.md) | Acceptance checks, provenance, and completion states |
| [Safety and governance](docs/safety-and-governance.md) | Permissions, approvals, stop conditions, and operational safety |
| [Metrics and evaluation](docs/metrics-and-evaluation.md) | How to test whether OCEAN improves outcomes |
| [Worked example](docs/worked-example.md) | Applying OCEAN to an API latency objective |
| [Glossary](docs/glossary.md) | Shared definitions for implementation and discussion |
| [Roadmap](docs/roadmap.md) | Proposed path from written methodology to evaluated prototype |

## What OCEAN is—and isn't

OCEAN is a **proposed methodology**, not a framework, SDK, runtime, or proof that agent autonomy always outperforms human planning. It borrows useful concepts from feedback control, iterative development, flow management, continuous integration, and risk-based governance. Its hypothesis is that these concepts can be organized around adaptive, outcome-driven agent execution.

OCEAN does not require eliminating humans, deterministic workflows, deadlines, release windows, or periodic reviews. It treats them as constraints and governance mechanisms to apply where they add value, rather than making them mandatory execution primitives for every task.

## Evaluation before adoption

Compare an OCEAN-based workflow with an appropriate baseline (for example, a sprint-based workflow or a continuous-flow workflow) on comparable tasks and equivalent permissions and resource budgets. Measure verified success rate, time to verified outcome, human interventions, total cost, duplicated work, retries, regression rate, and safety violations. Run multiple trials and report failures and uncertainty, not just successful demonstrations.

See [Metrics and evaluation](docs/metrics-and-evaluation.md).

## Contributing

Contributions should make the methodology clearer, safer, more testable, or better supported by evidence. See [Roadmap](docs/roadmap.md) for the current proposed development sequence. Please distinguish established results from hypotheses and implementation proposals.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
