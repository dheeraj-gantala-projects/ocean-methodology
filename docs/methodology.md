# OCEAN methodology

## Purpose

Objective-Centered Execution and Adaptive Navigation (OCEAN) is a proposal for organizing work performed partly or primarily by AI agents. Its central hypothesis is that execution should adapt to evidence while remaining anchored to explicit outcomes and constraints.

OCEAN is experimental. It is not an established standard, and no claim is made that it universally outperforms Scrum, Kanban, Waterfall, or other approaches. It should be evaluated against a suitable baseline in the target domain.

## Scope

OCEAN describes how a system can define objectives, choose and adapt work, coordinate agents, enforce boundaries, and verify outcomes. It does not prescribe a programming language, model provider, agent framework, issue tracker, version control system, or user interface.

## Core concepts

- **Objective:** the outcome to achieve, with measurable criteria and constraints.
- **Work graph:** the current model of tasks and dependencies needed to achieve the objective.
- **Agent run:** a bounded attempt to perform work.
- **Evidence:** an inspectable basis for accepting or rejecting a claim.
- **Policy:** machine-enforced rules for permissions, budgets, approvals, and prohibited actions.

## Operating loop

OCEAN uses five named activities: Observe, Clarify, Explore, Act and adapt, and Normalize and verify. They are a feedback model, not mandatory sequential stages. An implementation can enter or revisit any activity as context changes.

## Relationship to existing approaches

OCEAN borrows compatible practices from iterative delivery, flow management, continuous integration, feedback control, and risk-based governance. It does not require rejecting sprints or human planning. Time-based cycles may remain useful for stakeholder alignment, budgeting, releases, and regulatory reviews, while agent execution proceeds continuously where appropriate.

## Design principles

1. Outcomes over predetermined task lists.
2. Explicit constraints and bounded authority.
3. Information gathering when it can improve decisions.
4. Dynamic decomposition and dependency-aware execution.
5. Coordination only when its expected value justifies its cost.
6. Verification based on evidence, not agent self-report alone.
7. Learning from execution without overgeneralizing from isolated outcomes.
8. Measurement and comparison before claiming improvement.

## Non-goals

OCEAN is not an argument for unlimited autonomy, removing humans from consequential decisions, eliminating all planning, or treating a language model's confidence as a correctness guarantee. It is not a claim that one decision formula works for every task.
