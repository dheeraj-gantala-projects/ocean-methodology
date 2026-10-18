# Verification and evidence

OCEAN distinguishes execution status from verified outcome. Agents can report that an attempt ran successfully, but objective completion is based on acceptance evidence.

## Evidence record

An evidence record should capture, as appropriate:

- The criterion or claim being evaluated.
- The result and measured value.
- Source artifact, run identifier, and reproducible command or procedure.
- Time, environment, version, and relevant configuration.
- Identity of the producer and verifier.
- Limitations, uncertainty, and known gaps.

Keep evidence immutable or versioned. Link to artifacts rather than embedding unnecessarily large outputs in shared state.

## Verification strategy

Use deterministic checks where available: tests, type checks, policy evaluators, deployment health checks, schema validation, and benchmark measurements. Use agent review for semantic issues that require judgment, but do not treat fluent explanations as a substitute for executable or independently inspectable evidence.

## Independence and risk

The higher the impact of an error, the stronger the verification should be. Independence may involve a separate agent with different context, a deterministic checker, a human reviewer, or a controlled experiment. A second answer from the same reasoning path is not necessarily independent validation.

## Completion rule

An objective can move to `achieved` only when all mandatory criteria pass, required invariants are checked, and any mandated approvals are recorded. If evidence is missing or inconclusive, the objective remains under verification, blocked, or escalated.

## Failure handling

A failed check should create a structured finding that records the criterion, observed result, expected result, evidence, and suggested next step. The scheduler can reopen the relevant investigation or return the objective to an active state. Avoid repeatedly running the same failing check without a changed hypothesis or condition.
