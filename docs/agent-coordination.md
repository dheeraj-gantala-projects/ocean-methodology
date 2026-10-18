# Agent coordination

OCEAN treats agents as execution capabilities, not necessarily as permanent organizational roles. A system may use a single agent, specialist agents, or a combination depending on task structure and measured performance.

## When to delegate or parallelize

Parallelize when work can proceed independently, diversity of approach is valuable, or latency reduction justifies additional compute. Prefer one agent when the task is narrow, tightly coupled, or cheaper to complete serially.

Before delegating, define the expected output, scope, accessible context, tool permissions, resource budget, deadline, and completion criteria. Avoid sending broad, ambiguous instructions that encourage duplicate work.

## Shared findings

Share concise, structured findings rather than entire context histories by default. Useful records include:

- Claim or hypothesis.
- Supporting and contradicting evidence.
- Source and timestamp.
- Confidence and known limitations.
- Reproduction steps or artifact reference.
- Recommended next action, if any.

Consumers should be able to inspect the original evidence. A shared note is not automatically true because another agent produced it.

## Ownership and conflicts

Use leases or equivalent coordination to prevent accidental concurrent mutation of the same resource. Leases need expiration and recovery semantics. For shared code, configurations, or documents, isolate work where possible and validate the integrated result.

## Independent review

Use an independent verifier when the risk, complexity, or possibility of confirmation bias justifies it. Independence may require separate context, different tools, or deterministic checks—not simply a second response from the same reasoning path.

## Coordination cost

Measure the cost of spawning, context transfer, synchronization, reconciliation, and redundant work. Add specialist agents only when their expected marginal value is positive.
