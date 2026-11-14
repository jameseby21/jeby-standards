---
name: modularity
description: Define the smallest observable behavior first, then modularize only the collaborators with a credible reason to vary; each module has one owner, one contract, and behavior plus contract tests; a level in a hierarchy is a module with its own profile, rollup and view.
---

# Modularity

Its pair is not yet written (PAIRS.md: half missing). The candidate name is `cohesion`: keep together what changes together, so modularity never splits a thing into pieces that must always move as one. Until James defines it, this skill carries the restraint itself in the anti-patterns below.

Source rule (Plantriloquist case, 2026-10-14, FORGE-0006): "Define the smallest observable behavior, then modularize only collaborators with credible reasons to vary." The owner wanted modularity by default while protecting simple proof-of-concept actions from needless frameworks: "tell a joke" is granular; voice, joke source and playback target are modular.

Use this skill when designing a feature, a data model, a hierarchy, a pipeline or a report, and whenever a change touches more than one collaborator.

## Decision rule

1. **Name the granular behavior**: the smallest thing a person can observe and check (a row appears, a joke is told, a company opens into its projects). Write it as the acceptance line.
2. **List the collaborators** that produce it (sources, renderers, stores, rules, levels).
3. **For each collaborator ask: what would make this vary?** Evidence (two implementations exist or are ticketed) or explicit product intent counts. A credible answer makes it a module with a contract; no answer keeps it inline.
4. **Each module**: one owner, one contract (inputs, outputs, errors), behavior tests on the granular behavior and contract tests on the boundary, a line in the owning doc.
5. **A level in a hierarchy is a module**: it has its own profile (what it is), its own rollup (how its children sum or rank) and its own view (how a person opens it). A level missing any of the three is not a level yet.

## Checks

- The granular behavior is written before any module exists.
- Every module names its reason to vary; one with a single implementation and no stated variation is inlined.
- Contracts are tested at the boundary, behaviors at the surface; neither alone passes.
- No framework for a proof of concept; no proof of concept hard-wired into a framework.
- Hierarchy levels each have profile, rollup and view.

## Applied

- 2026-11-08 (James: "Ticket < Track < Project < company < jeby overall"): each level becomes a module with profile, rollup and view; the board drill is composition of level views; sprint and the other slices are a separate module that cuts across levels rather than a level. Ticketed in the DESK hierarchy tickets.
