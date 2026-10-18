# Operating model

OCEAN is a feedback-driven loop with five named activities: Observe, Clarify, Explore, Act and adapt, and Normalize and verify. The names are memory aids, not mandatory phases that must execute exactly once or in order.

## 1. Observe

Collect the minimum relevant picture of the environment: current state, prior history, available tools and capabilities, dependencies, active runs, relevant policies, and known unknowns. Prefer observations that could affect the next decision. Record provenance and freshness.

## 2. Clarify

Translate the request into an objective contract. Define measurable success criteria, constraints, non-goals, risk tier, budget, permitted actions, and approval boundaries. Ask for clarification when ambiguity materially affects safety, scope, or the ability to verify success.

## 3. Explore

Generate candidate actions and a provisional work graph. Identify dependencies, possible parallelism, likely information value, costs, and failure modes. The graph is an evolving hypothesis, not an immutable plan.

## 4. Act and adapt

Select authorized work according to decision policy and available resources. Run it in an isolated or controlled environment when practical. Observe results, record evidence, and adapt the graph when new information changes the best course. Enforce budgets and policies outside the agent's discretion.

## 5. Normalize and verify

Integrate changes, validate acceptance criteria, record evidence, resolve or explicitly retain known issues, and update the objective state. Use independent or deterministic verification commensurate with risk. If checks fail, return to the activity that can best address the failure.

## State transitions

A useful objective state model includes `proposed`, `ready`, `active`, `blocked`, `verifying`, `achieved`, `abandoned`, and `failed`. Implementations may distinguish more states. State transitions should be auditable and controlled by explicit conditions rather than free-form agent claims.

- `achieved`: every required acceptance criterion has sufficient evidence.
- `blocked`: progress depends on unavailable information, resources, a dependency, or a decision.
- `abandoned`: an authorized decision stops work because it is no longer valuable or appropriate.
- `failed`: the execution process ends without meeting the objective, under defined failure conditions.

## Event-driven execution

Reconsider work when meaningful events occur: a dependency completes, a verification fails, new telemetry arrives, a budget approaches its limit, or a human changes priority. Periodic reconciliation may still be useful for detecting lost events and stale leases, but calendar-based sprints are not required for every execution cycle.

## Stop and escalation conditions

Stop or escalate on authorization gaps, safety concerns, conflicting constraints, repeated non-progress, budget exhaustion, deadline expiry, or low expected value. Keep partial results and evidence so work can resume safely if authorized.
