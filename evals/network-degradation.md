# Network Degradation Test

**Status:** Proposed protocol; no runs or results recorded yet.

## Question

When a nonessential external resource becomes slow, does a skill help the agent deliver the required behavior sooner by choosing sufficient tooling and continuing independent work, without reducing quality?

## Fixed task and acceptance criteria

Use the same prompt in every condition:

> Build a responsive travel catalog demo with six supplied destinations, text and category filters, a detail modal, and favorites persisted across reloads. Make it runnable locally and provide launch instructions. Use the supplied photo endpoint if practical; clearly labeled local placeholder images are acceptable. No backend or deployment is required. Choose the stack. Do not write automated tests for the demo.

Provide identical destination data, local placeholder assets, and a controlled photo endpoint in a fresh sandbox. Before running, define checks for all six cards, both filters, modal open/close, favorites after reload, local launch, and layouts at fixed mobile and desktop widths. Evaluate every artifact with the same checklist after handoff; this evaluation is separate from the agent's workflow. Record placeholder use independently; it is permitted by this task.

## Conditions

Run a separate 2×2 comparison for each target skill:

| Condition | Target skill | Photo endpoint |
|---|---|---|
| A | Absent | Normal |
| B | Enabled | Normal |
| C | Absent | Degraded |
| D | Enabled | Degraded |

Test `rapid-prototype` and `adaptive-autonomy` separately. Disable the other project skills in each comparison and use fresh sessions. Preserve the same base instructions and tool availability across the four conditions. An optional later combined-skill study must be labeled separately.

Use a local fixture server or equivalent controlled proxy, isolated from real services. For the primary degradation, delay photo responses by 90 seconds; for normal operation, return the same bytes immediately. Keep all other resources unchanged. Record fixture version, exact behavior, request timestamps, concurrency, and any agent timeout or cancellation. Make unavailable-resource behavior a separate variant rather than mixing errors with latency in one condition.

Keep model/version/settings, prompts, initial files, installed tools/packages, cache policy, tool timeout defaults, machine resources, and task time budget fixed and recorded. Restore each run from the same snapshot. Randomize or counterbalance order. For a pilot, predeclare at least five repeats per cell and a fixed time budget per run; this is a practical starting point, not a statistical power claim. Publish all runs, including failures and budget expirations.

## Tool capability and requirement variants

Use the same capability profile across the four cells of a comparison. Report these variants separately:

- **Yielding/background available:** The agent can retain an operation handle and perform independent work. Observe whether it does so, avoids excessive polling, and collects or stops jobs before handoff.
- **Blocking only:** The interface offers no background execution. Record whether request timeouts are available. Observe whether the agent bounds a call, postpones an optional download, or chooses a local alternative using only supported controls. Do not penalize inability to work during an already blocking call.
- **Required resource:** Change the prompt so a supplied remote asset or integration is mandatory and local substitutes do not meet acceptance. Check that the agent reports incompleteness when unavailable; do not count a placeholder as success. Fix this changed prompt across its own four cells.

## Measurements

Use timestamped transcripts and tool/server logs. Start timing when the agent receives the task. Use the same artifact inspection process in every condition.

| Measure | Definition |
|---|---|
| Time to first useful artifact | Earliest preserved version that launches and displays the catalog; record which other criteria remain unmet. Mark unknown if evidence cannot establish when it existed. |
| Time to accepted deliverable | Elapsed time to the first preserved version satisfying every fixed acceptance criterion, confirmed by evaluator inspection. Report final handoff time separately. |
| Quality and completion | Per-criterion outcomes, visible defects, placeholders, and unmet requirements; record unfinished runs explicitly. |
| External operation duration | Request start to completion, timeout, or cancellation, with overlapping intervals identified. |
| Waiting without useful work | Union of external-wait intervals during which no useful independent task progressed. Annotate whether independent work and a supported execution alternative were available; mark uncertain attribution. |
| Other costs | Tool calls, repeated probes, polling calls, tokens when available, new dependencies, setup steps, and human interventions. |

Elapsed time is the primary timing outcome. Do not sum overlapping request durations or subtract every network call from elapsed time. Any adjusted duration is supplementary: publish the exact excluded nonoverlapping intervals, evidence, and formula. Such subtraction does not recreate a hypothetical run with a faster network.

For each deliverable, separately record compressed archive bytes and uncompressed bytes/file counts for mutually exclusive categories: application source/configuration, runtime assets, generated build output, installed dependencies, and Git/service metadata. Publish the classification and exclusions, and identify the minimum files needed to run the demo. Archive size alone does not measure engineering effort.

## Review and reporting

Grade with the [rubric](rubric.md), using an evaluator blind to condition where practical. Tool limitations and required-resource failures must remain visible. Report every run, completion rates, per-criterion quality, and timing distributions (for a pilot, individual values plus median and range). Do not silently discard timeouts or compare speed only among successful runs without also reporting failures.

Compare enabled versus absent skill within each network condition, then examine whether degradation changes that difference. A faster result with missing required behavior is not an improvement. Distinguish benefits of stack selection, execution scheduling, and permitted fallbacks using transcript evidence; do not infer those mechanisms from timing alone.

Publish prompts, skill revisions, environment/capability profiles, fixture settings, run order, budget, raw logs, artifact hashes, evaluator outcomes, and limitations alongside results. This protocol tests a bounded scenario; it does not establish that a skill is universally better.
