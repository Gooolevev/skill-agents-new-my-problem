---
name: deep-engineering
description: Deliberately design and implement complex, high-consequence, or production-oriented coding tasks. Use when the user requests robustness, architecture, reliability, thorough investigation, migration safety, meaningful tests, or a carefully reasoned design. Do not use for throwaway prototypes or minor visual tweaks unless explicitly asked.
license: MIT
---

# Deep Engineering

**Outcome:** Solve the important problem thoroughly, with explicit assumptions, coherent architecture, and evidence of correctness—without confusing prolonged activity with progress.

## Decide what deserves depth

1. Restate the concrete outcome and constraints in a few lines, separating intent from the user's proposed approach.
2. Identify the genuine hard parts: invariants, APIs, data flow, threat boundaries, failure modes, performance constraints, and migration risks.
3. Explore at least one meaningful alternative when a foundational choice has lasting consequences. Explain the trade-off, not every trivial possibility.
4. Produce a proportionate implementation plan or spec **for the consequential parts**, then implement in useful vertical slices.
5. Verify the behavior that can cause real harm or invalidate the goal. Use focused automated tests, integration checks, and review where the consequence justifies them.
6. Record unresolved risks, evidence of completion, and follow-up work. Do not claim checks passed when they were not run.

## Integrate with Addy Osmani's Agent Skills when available

This skill is a **mode selector and guardrail**, not a copied replacement for the external repository.

If `addyosmani/agent-skills` is installed, use the relevant specialized skill for the current stage, for example:

- `spec-driven-development` for multi-component feature requirements.
- `planning-and-task-breakdown` for dependencies and sequencing.
- `incremental-implementation` for staged implementation.
- `test-driven-development` when tests are valuable and practical.
- `debugging-and-error-recovery` for investigation.
- `code-review-and-quality` for release or merge-readiness.

Read or invoke only the relevant installed skills. Do **not** assume those names exist, or fabricate a slash command if a tool does not offer it. Follow the user's explicit desired rigor and your agent's actual tools. The external package is optional.

## Prevent analysis paralysis

- Every substantial diagnostic action must produce a possible new observation that could change the next decision.
- After repeated non-informative checks, stop repeating the same hypothesis. Pivot to another independent task, use a genuinely different probe, or request a specific human input.
- A blocker requiring credentials, approval, or subjective judgment belongs to the responsible human; surface it concisely rather than spending an hour circling it.
- Do not turn a proven pre-existing unrelated failure into an unrequested full-project cleanup.
- Deep mode means **high-quality decisions**, not infinite tests or maximum deliberation.

## Stop conditions

Stop the current investigative branch when the relevant success criteria are supported, the next step requires human authority, or further actions have insufficient expected information value. Report the evidence and remaining uncertainty. Use `$adaptive-autonomy` to handle ambiguous blockages, not to force another review loop.
