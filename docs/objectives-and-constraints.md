# Objectives and constraints

An objective is a compact contract describing why work exists, what success means, and what execution must respect. It is not merely a natural-language request passed to an agent.

## Recommended objective template

```yaml
id: objective-001
title: Reduce API tail latency
purpose: Improve user-facing response time
success_criteria:
  - metric: p95_latency_ms
    operator: <=
    target: 200
    evaluation_window: 30m
constraints:
  - preserve externally observable behavior
  - monthly infrastructure spend must not exceed the approved budget
non_goals:
  - broad architectural rewrite
risk_tier: medium
budget:
  max_cost_usd: 50
  max_duration_minutes: 120
  max_parallel_runs: 4
authority:
  allowed_actions:
    - read telemetry
    - create isolated code changes
    - run tests
  approval_required_for:
    - production deployment
    - destructive data changes
verification:
  - load test against the agreed baseline
  - regression suite passes
owner: engineering
```

This is illustrative; adapt units, fields, and policy to the domain.

## Required elements

A good objective names the desired outcome, a measurable acceptance condition, relevant baseline and measurement window, invariants, scope, budget, risk boundaries, and who can approve changes. It should state important non-goals to limit unnecessary work.

## Ambiguity handling

If missing information could materially change the strategy or make verification impossible, ask a targeted question or propose explicit assumptions for approval. Do not invent critical business intent. Low-impact ambiguity may be handled with a recorded, reversible assumption.

## Constraint hierarchy

Security, privacy, authorization, legal obligations, and platform safety policies are hard boundaries. Objective preferences and resource budgets are interpreted within those boundaries. An objective cannot authorize an action the agent is not permitted to perform.

## Changes to the contract

Agents may recommend changes when the objective appears infeasible or inconsistent. They must record the reason and evidence. Only an authorized actor or policy-defined authority can approve material changes to success criteria, risk tolerance, or budget.

## Completion

Objective completion requires evidence for each required success criterion and confirmation that relevant invariants remain satisfied. An agent's statement that work is done is not sufficient.
