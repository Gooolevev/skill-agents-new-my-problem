# Experiment 001 — Similar Output, Different Engineering Cost

**Status:** Exploratory case note, based on the project author's report. One run per condition. The archives, prompts, transcripts, and raw timing records are not included in this repository and have not been independently checked. This is not a controlled benchmark.

## Reported artifacts

| Property | ДАЛЬ — with Rapid Prototype | тише — without the skill |
|---|---|---|
| Theme | Travel | Nature retreats |
| Implementation | HTML + CSS + JavaScript | React + TypeScript + Vinext, with Sites infrastructure |
| Project archive size | 1.2 MB | 15 MB, including service files and build output |
| Catalog, filtering, responsive layout | Reported present | Reported present |
| Interaction | Modals and selection flow | Favorites persisted in localStorage, dates, cost calculation, FAQ |
| Database used by the demo | None reported | None reported |

The second archive reportedly contains 375 files, including Git objects, build output, many UI components, and a separate static `tishe-for-sharing` version with HTML and CSS. These counts and sizes describe the supplied archives; they do not isolate implementation complexity or effort.

## Reported timing

The author reports that the run without the skill took **2.5× as long** in elapsed time and **approximately 1.5× as long** after a network adjustment. Absolute durations, timestamped intervals, and the adjustment calculation are unavailable here. These ratios cannot currently be reproduced; do not present them as an established skill effect.

## What this observation suggests

The runs may have reached broadly similar demo goals through paths with different setup and delivery costs. The static export suggests a potentially sufficient alternative, but its feature parity and generation history must be checked before concluding that the surrounding infrastructure was avoidable.

Three possible sources of cost deserve separate measurement:

- Repeated diagnostics without new information.
- Implementation or infrastructure beyond what the goal requires.
- External waiting that prevents otherwise independent progress.

The report does not establish how much each source contributed. The second demo also reportedly has more functionality, so equal output quality cannot be assumed.

## Limits and evidence needed

- Recover exact prompts, skill versions, model/settings, tool availability and instructions, initial project state, and cache conditions. Different themes, requirements, or Sites use may explain part of the difference.
- Preserve transcripts, source archives and hashes, absolute elapsed durations, and the rule used for the network adjustment. Distinguish tool-imposed scaffolding from agent-selected infrastructure.
- Check both demos against a shared feature checklist, including the separate static version. Record missing or additional behavior and whether setup instructions work.
- Count source, runtime assets, generated builds, installed dependencies, and repository/service metadata separately. Record compressed archive size independently from uncompressed category sizes.
- Repeat matched runs in varied order. One run per condition cannot estimate generation variance or establish causality.

## Follow-up

Use the [Network Degradation Test](../network-degradation.md) to test whether skill instructions improve dependency handling under controlled conditions. Test Rapid Prototype and Adaptive Autonomy separately before attributing improvements to either skill. Keep the reported case ratios separate from future experimental results.
