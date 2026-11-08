# Agent Judgment Skills — three complementary modes for coding agents

An **experimental** collection of [Agent Skills](https://agentskills.io/) for navigating the tension between speedy prototypes, deliberate engineering, and autonomous decision-making.

> **Hypothesis:** Better coding agents choose sufficient implementations under actual constraints, avoid low-value diagnostic loops, and keep independent work moving when external dependencies stall. These skills have not yet been shown to improve performance in a controlled evaluation.

## The three skills

| Skill | Activate when | Default behavior |
|---|---|---|
| [`rapid-prototype`](.skills/rapid-prototype/SKILL.md) | A quick demo, exploratory UI, mockup or throwaway experiment | Implement first; no new tests, full test suite or extended review by default. Cheap build/preview if needed. |
| [`deep-engineering`](.skills/deep-engineering/SKILL.md) | A complex, high-risk, long-lived or production-quality change | Reason about architecture, plan meaningful slices, verify consequential behavior; avoid endless checking. |
| [`adaptive-autonomy`](.skills/adaptive-autonomy/SKILL.md) | The agent is uncertain, stuck, repetitively debugging or deciding who should act | Choose ACT / PROBE / PIVOT / ESCALATE; choose a suitable execution mode if needed. |

**Not all three at once.** `rapid-prototype` and `deep-engineering` are alternative execution postures. `adaptive-autonomy` is an optional decision policy that can assist either one. Explicit user instructions and required safeguards always override their defaults.

### Using Addy Osmani's agent-skills for deep work

For detailed specification, staged implementation, testing, and review, you can install [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) separately. Our `deep-engineering` skill selects an appropriate mode and can refer to the matching specialized skills **if installed**. It does not bundle or copy that project. The external suite's `/build auto` still uses test-driven steps, so it is not a rapid no-tests preset.

## Install in a Codex project

Copy any/all skill folders from this repository's `.skills/`, including their own `references/` when present, into the project's `.agents/skills/` directory:

```bash
mkdir -p .agents/skills
cp -R /path/to/agent-judgment-skill/.skills/{adaptive-autonomy,rapid-prototype,deep-engineering} .agents/skills/
```

The command assumes a Bash-compatible shell. In **fish**, use:

```fish
mkdir -p .agents/skills
for skill in adaptive-autonomy rapid-prototype deep-engineering
    cp -R /path/to/agent-judgment-skill/.skills/$skill .agents/skills/
end
```

Then ask the agent, for example:

```text
$rapid-prototype Build a responsive animated homepage. No automated tests; show me a working demo.
$deep-engineering Refactor VIN extraction with reference fixtures, integration tests, and failure analysis.
$adaptive-autonomy The integration is blocked. Decide whether to probe, pivot, or ask for my input.
```

Automatic selection is tool-dependent; explicit invocation is the most predictable way to compare behavior. You can also install a single skill instead of all three.

## Evaluate before making performance claims

Use matched tasks **with and without** the relevant skill. Record elapsed time, tokens, correctness, functioning deliverables, redundant tool calls, and human interventions. In particular, test whether rapid mode accidentally hides mistakes, and whether deep mode gets stuck. Evaluation templates: [`evals/scenarios.md`](evals/scenarios.md), [`evals/rubric.md`](evals/rubric.md).

The [Experiment 001 case note](evals/experiments/001-similar-output-different-cost.md) records a user-reported exploratory comparison, including unverified measurements and limitations. It does not establish a causal speedup. The [Network Degradation Test](evals/network-degradation.md) specifies a future comparison of skill use and network conditions, with separate measures for delivered quality, waiting, and packaging cost.

## Validation

```bash
python3 scripts/validate_skill.py
```

This performs a **lightweight structural check**, not a behavioral evaluation or a substitute for the official `skills-ref validate` tool. Specification: [agentskills.io/specification](https://agentskills.io/specification).

## License

MIT. See [LICENSE](LICENSE).
