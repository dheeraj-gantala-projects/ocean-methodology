# Roadmap

This roadmap is a proposal, not a commitment or a report of completed implementation work.

## Stage 1 — Specification

- [x] Define the methodology and its status as an experimental proposal.
- [x] Document the operating loop, objective contract, work graph, decisions, coordination, verification, safety, and evaluation.
- [x] Provide a worked example, glossary, and contribution guidance.

## Stage 2 — Reference schemas

- [ ] Define versioned schemas for objectives, work nodes, agent runs, evidence, policies, and state transitions.
- [ ] Specify idempotency, leases, retry semantics, and event provenance.
- [ ] Add schema validation examples and compatibility guidance.

## Stage 3 — Minimal reference runtime

- [ ] Implement objective intake and acceptance-criteria validation.
- [ ] Add a policy-enforcing scheduler with budgets and capability-based work selection.
- [ ] Implement a persistent work graph and auditable run records.
- [ ] Add evidence-backed verification and stop/escalation paths.

## Stage 4 — Evaluation harness

- [ ] Build a task suite with representative success, failure, ambiguity, and safety cases.
- [ ] Compare continuous adaptive execution against relevant baselines.
- [ ] Publish reproducible results, limitations, and negative findings.

## Stage 5 — Integrations

- [ ] Prototype adapters for version control, CI, issue tracking, and observability.
- [ ] Test recovery from interrupted runs, tool failures, and stale ownership leases.
- [ ] Document deployment, audit, privacy, and operational requirements.

## Exit criteria

Advance based on evidence, not schedule alone. Do not describe OCEAN as effective or production-ready until evaluation supports the specific claims being made.
