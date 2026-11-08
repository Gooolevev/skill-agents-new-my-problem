---
name: rapid-prototype
description: Rapidly build or reshape a throwaway or reversible prototype. Use when the user asks to sketch, mock up, vibe-code, try an idea, get a working demo quickly, or prioritize visible progress over comprehensive verification. Skip new automated tests and exhaustive review by default; do not use for production releases, irreversible data changes, sensitive systems, or critical migrations.
license: MIT
---

# Rapid Prototype

**Outcome:** Deliver something the user can run, click, inspect, or edit quickly. Optimize for time-to-first-useful-artifact, not a production-ready quality certificate.

## Entry contract

- Activate for an exploratory demo, creative UI, quick proof of concept, or a reversible experiment. **Do not silently treat a production change as a prototype.**
- Treat explicit user requests for quality gates or tests as overriding the default no-test posture.
- If the task includes external deployments, production data, security boundaries, billing, or destructive writes, keep the required approvals and safeguards. Use the deep workflow for high-impact parts.
- Preserve the existing project's functioning features and requested stack. Do not rewrite the project to chase a prototype unless asked.

## Build loop

1. **Infer the smallest visible success.** Translate the user's goal into a compact working result, without writing a formal spec unless requested.
2. **Reuse the environment.** Inspect only the files needed to find entry points, dependencies, and the target screen/path. Prefer installed packages and existing patterns.
3. **Choose reversible defaults.** Decide routine styling, file naming, sample data, and small implementation details yourself. If subjective preferences remain open, show a concrete default for feedback.
4. **Build a coherent vertical slice.** Connect only what's necessary for the demo to work end-to-end. Prefer working code over scaffolding and speculative architecture.
5. **Preview when cheap.** Run a single quick start/build/smoke command if it is inexpensive and required to make the demo usable. Do not write test files, run a full test suite, enforce coverage, or perform generic multi-pass code review unless the user asks or a material risk makes a specific check necessary.
6. **Deliver and stop.** Provide how to run it, what is demonstrated, and any known gaps. Never call an untested prototype tested or production-ready.

## Choose a viable implementation under actual constraints

- Prefer the least costly approach that satisfies the requested behavior. Include dependency installation, network and service delays, user setup, failure risk, and maintenance in that choice.
- For a new self-contained demo, consider a static implementation when it covers the requirements. Use a framework, backend, or hosted tool when it provides needed behavior or lowers the actual cost. Preserve an existing working stack and explicit user choices.
- Before a slow external call, check whether its result is needed now. If the tool supports yielding or background work, start the operation and continue independent tasks; otherwise use an available timeout or postpone a nonessential call. Do not assume a blocking tool permits parallel work.
- If an optional resource is unavailable, continue with a labeled local substitute and revisit it when useful. A missing required integration remains an open requirement. Collect or stop background jobs before handoff when supported.

## No-ceremony defaults

- No extended design interviews for low-risk choices.
- No long task breakdown, test-driven development, blanket refactors, coverage targets, or lint-fix detours.
- No new infrastructure or library solely for hypothetical future scale.
- No repeat diagnostics without new evidence. A failed quick check may justify one targeted fix and rerun; if blocked by credentials/permissions, ask the user instead of looping.
- No fake endpoints or fake claims presented as live integration. Label mocks and placeholder content.
- Keep code readable and easy to replace. Fast does **not** mean intentionally messy.

## Definition of done for a prototype

The requested screen, demo, feature, or proof of concept exists and can be inspected or run using the supplied instructions; any remaining unverified behavior is named plainly. If no execution was possible, report that without implying it worked.

## Handoff to deeper work

Upgrade **only the affected workstream** when any of these becomes true:

- User explicitly asks for reliability, production readiness, tests, architectural review, or scale.
- Real data, payments, credentials, permissions, destructive writes, or deployment risk become relevant.
- Repeated failures reveal that superficial changes will not resolve a consequential problem.

When upgrading, say what changed and why. Do not silently convert the whole project into a lengthy audit. If available, apply `$deep-engineering`; use `$adaptive-autonomy` for blocked decisions.
