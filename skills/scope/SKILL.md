---
name: scope
description: Map an open-ended or cross-layer change to its affected code, data, tests, skills, and documentation before implementation; the partner of proactivity.
---

# Scope

Pairs with `proactivity`. Scope traces a change through every layer it touches before it is widened or started. `proactivity` takes the small improvements the request directly implies. Together they keep a change complete without letting it sprawl.

Use when a request is vague, spans multiple application layers, or appears small but changes a workflow contract.

- Translate the requested outcome into a concrete behavior change and list the surfaces that must agree: schema or database, backend contract and authorization, frontend state and UI, fixtures and data, tests, skills, and documentation (the owners are listed in the repo's `docs/doc-ownership.yaml`).
- Trace the current path from user action to persistence and back to the displayed result. Treat a button as incomplete until its API, server-side behavior, data effect, success state, and failure state are covered.
- Separate required edits from follow-up ideas. Do not add schema, migrations, external integrations, or broad refactors merely because they could be useful.
- Identify settled invariants before editing: stable identity, server validation, provenance, auditability, and no client editing of internal IDs.
- Define the smallest verification matrix that proves each affected boundary, including unauthorized, unreachable-service, validation-error, success, refresh, and narrow-screen behavior when relevant.
- Name the affected test scopes and the verification depth the project's testing rules require. Changed-scope inspection keeps its persistent baseline and expands every mapped scope; an uncertain shared-contract impact escalates to the full run rather than silently omitting coverage.
- Convert each numbered or bulleted requirement into a scope and evidence row before implementation. Later items may qualify earlier ones; do not treat the first few bullets as a complete or replacement request until the entire message is read.
- Report problem, evidence, proposed change, affected files, verification plan, and risks before a material change; after approval, stop at that boundary and record what was actually verified.
