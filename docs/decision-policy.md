# Decision policy

OCEAN needs a policy for choosing the next action, not just a description of phases. The policy should be explicit enough to evaluate, while remaining adaptable to the task domain.

## Candidate actions

Candidates may include gathering an observation, asking a clarifying question, testing a hypothesis, implementing a change, delegating a bounded task, verifying a result, waiting for a dependency, stopping, or escalating to a human.

## Decision factors

Evaluate candidate actions using:

- Expected contribution to the objective.
- Expected information gain or uncertainty reduction.
- Cost in money, compute, elapsed time, and coordination.
- Risk, reversibility, and blast radius.
- Dependencies, resource contention, and deadlines.
- Probability that the result can be evaluated reliably.

A conceptual heuristic is:

`score(action) = expected_progress + information_weight * expected_information_gain - cost_weight * expected_cost - risk_penalty`

This is a design aid, not a universal optimizer. Metrics must be normalized and calibrated for the domain. Hard constraints are enforced separately and cannot be overridden by a high score.

## Value of information

Gather more information when it could change the selected action or materially reduce the risk of a costly decision. Do not investigate indefinitely when the information is unlikely to change the choice or when the cost exceeds its expected value.

## Ask, act, or stop

Ask a human when critical intent is ambiguous, authority is missing, constraints conflict, or a decision exceeds the agent's permitted risk. Act when the next step is authorized and adequately specified. Stop or escalate when budgets expire, repeated attempts fail, the objective becomes infeasible, or expected value becomes non-positive.

## Decision records

For consequential decisions, record the chosen action, relevant alternatives, evidence used, assumptions, uncertainty, estimated cost, applicable policy checks, and outcome. Keep the record proportionate to the risk.

## Avoid false precision

A numeric score cannot reliably capture every value conflict. Use explicit hard constraints, calibrated estimates, and domain-specific policies. Evaluate decisions by observed results rather than trusting the score itself.
