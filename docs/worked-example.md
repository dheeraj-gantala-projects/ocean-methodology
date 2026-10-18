# Worked example: reduce API latency

This scenario illustrates how OCEAN could be applied. It is hypothetical and does not claim a measured result.

## Objective

Reduce p95 API latency by at least 40% relative to a defined baseline while preserving required behavior and keeping incremental infrastructure cost within the approved budget.

## Observe and clarify

The system inspects service telemetry, tracing, recent deployments, relevant code, existing tests, and cost data. It confirms the measurement window, traffic profile, baseline, acceptable error rate, and whether production changes require approval. If any missing input makes success untestable, it asks a targeted question.

## Explore

The system identifies unknowns and proposes bounded work:

1. Profile representative requests to locate time spent.
2. Inspect database query plans and connection-pool metrics.
3. Review recent code and configuration changes.
4. Establish a repeatable benchmark and regression suite.

Independent read-only investigations may run concurrently. Each has a scope, budget, and expected artifact. Findings are recorded with source and confidence rather than treated as unquestionable facts.

## Act and adapt

Suppose profiling suggests database query time is a major contributor. The system adds a focused query-plan investigation and tests a local optimization in an isolated change. It does not proceed with a speculative cache redesign merely because that was in the initial plan. If evidence contradicts the database hypothesis, the work graph is revised.

## Normalize and verify

The candidate change is integrated in an isolated branch or workspace. CI and regression tests run, followed by a benchmark against the agreed baseline. The verifier checks latency, error rate, behavior, and cost conditions. Production deployment occurs only with required authorization and a rollback plan.

## Possible outcomes

- **Achieved:** all performance, behavior, cost, and approval criteria pass with reproducible evidence.
- **Blocked:** the baseline or required access is unavailable, or a human decision is needed.
- **Not achieved:** budget is exhausted or experiments show the target is infeasible under the constraints; results and evidence are retained.

## Why no sprint is required

The objective can progress as dependencies clear and evidence arrives. Human reviews may still occur at agreed intervals, and release windows may remain necessary. These are governance choices rather than a requirement that agents wait for a sprint boundary.
