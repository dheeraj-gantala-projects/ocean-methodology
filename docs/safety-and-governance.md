# Safety and governance

Autonomy should expand only where control and verification are adequate. Safety controls are part of the methodology, not an optional afterthought.

## Policy enforcement

Enforce access control, resource ceilings, approval requirements, and prohibited actions outside the language model's discretion. Agents may propose actions, but a policy layer must authorize them before execution.

## Risk tiers

Use risk-based controls. Read-only investigation may need lightweight controls; changes to production systems, personal data, financial operations, security policy, or destructive state require stronger validation and explicit approval as appropriate.

## Least privilege and isolation

Grant only the tools and permissions needed for the current work. Isolate concurrent runs, scope credentials, avoid sharing secrets in agent context or logs, and expire temporary access. Treat external content and tool results as untrusted input rather than policy instructions.

## Resource budgets

Define hard limits for cost, tokens, wall-clock time, tool calls, retries, concurrency, and affected resources where applicable. The scheduler must stop or seek authorization when a limit is reached. Agents cannot silently increase their own budgets.

## Human approval

Require authorized review for high-impact or irreversible changes, objective-contract changes, production deployments where mandated, and any action outside the agent's delegated authority. Make approval requests specific: proposed action, expected impact, evidence, alternatives, and rollback plan.

## Stop conditions

Stop or escalate on policy violations, unexpected destructive effects, critical uncertainty, conflicting instructions, repeated failures, budget exhaustion, or evidence that the objective is no longer feasible. Preserve a safe checkpoint and record the reason.

## Auditability and privacy

Record consequential actions, authorization decisions, tool inputs and outputs where appropriate, evidence references, and state transitions. Minimize sensitive data retention, redact secrets, enforce access to traces, and follow applicable retention policies.

## Recovery

Prefer reversible changes, checkpoints, idempotent operations, and tested rollback plans. After an incident, determine which control failed and add tests or deterministic protections rather than relying solely on prompt changes.
