---
name: generalize-it
description: Generalize a proven local change across every affected product surface, environment, test, and document without preserving accidental machine assumptions.
---

# Generalize It

Pairs with `formalize-it`: formalize-it writes the rule precisely from one case; generalize-it carries a proven change across every surface it should hold on. Generalize only what is written down and proven.

Use this skill when behavior that works in one path, page, table, machine, store or environment should become a reliable system-wide capability.

## Workflow

1. Define the invariant that should hold everywhere.
2. Find every producer, consumer, configuration source, launcher, route, component, test, fixture, and document affected by it.
3. Separate the local workaround from the reusable design.
4. Choose the smallest shared abstraction that removes duplication without obscuring behavior.
5. Implement representative variants and regression coverage.
6. Verify root-level operation, clean setup, and relevant environment boundaries.
7. Update current guidance and troubleshooting evidence.

## Realized-state learning

- Treat explicit user validation plus passing evidence as a realized state: preserve it as the new baseline instead of continuing speculative redesign.
- Promote the successful invariant, mechanism, verification, and limits into the relevant specialized skill, the standards lessons, and authoritative documentation.
- Generalize only dimensions supported by evidence or explicit product intent; do not turn one success into an unsupported universal rule.
- Keep pending generalizations visible in the roadmap or catalog when the current capacity or scope gate defers implementation.

## Checks

- Hard-coded values and duplicated logic
- Existing and new records, pages, tables, routes, and workflows
- Backend contracts, frontend models, fixtures, migrations, imports, and exports
- Development, test, build, launch, and deployment commands
- Localhost, LAN, alternate hosts, clean machines, process ownership, ports, persistent volumes, and permissions
- Provenance, stable IDs, temporal history, and real-versus-synthetic distinctions

Never declare generalization complete from one successful path. When setup, ports, Docker, credentials, or launchers are affected, require clean-environment evidence and two consecutive no-code-change verification passes.

## Applied

- 2026-11-08 (James: "'sprint' is more generalized and synced across libraries and maybe some other ways of slicing and dicing them"): the work hierarchy and its cross-cutting slices (sprint, assignee, tag, type) hold in every ticket store and library, not only the umbrella; one sprint calendar is the invariant, each store reads it. Ticketed as a DESK sprint-calendar ticket; checked when a second store exists.
