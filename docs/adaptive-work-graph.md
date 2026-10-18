# Adaptive work graph

A work graph represents the current best understanding of activities needed to achieve an objective. It is expected to evolve as new information arrives.

## Node types

- **Task:** a concrete unit of work that produces an artifact or state change.
- **Investigation:** gathers information to reduce uncertainty.
- **Experiment:** tests a hypothesis under defined conditions.
- **Decision:** records a choice, rationale, constraints, and authorized decision-maker where relevant.
- **Verification:** evaluates one or more acceptance criteria against evidence.

Implementations may use other node types, but each node should have a clear purpose and observable output.

## Edges and dependencies

Edges represent prerequisites, information dependencies, conflicts, or required ordering. Do not serialize work unless a dependency or shared-resource constraint requires it. Parallel work is appropriate only when expected benefits exceed coordination and conflict costs.

## Required node properties

A practical node should record:

- A stable identifier and parent objective.
- Expected output and acceptance criteria.
- Dependencies and affected resources.
- Required capabilities and permission scope.
- Budget or deadline, when applicable.
- Current state, owner or lease, and attempt history.
- Evidence and provenance for claimed results.

## Dynamic changes

Agents may propose splitting, adding, reprioritizing, or abandoning nodes. A deterministic scheduler validates dependency integrity, budgets, permissions, and policy before accepting changes. Material changes to an objective or its constraints require authorized approval.

## Preventing graph pathologies

The runtime should detect cycles, repeated equivalent work, stale nodes, runaway decomposition, and dependencies on abandoned tasks. Use deduplication keys or semantic similarity cautiously; similar-looking tasks can have materially different constraints. Apply limits for depth, task count, concurrency, and repeated attempts.

## Completion

A node's execution may succeed without the objective being achieved. Mark a node complete only when its defined acceptance checks pass. Mark the objective achieved only after all objective-level criteria and required verifications pass.
