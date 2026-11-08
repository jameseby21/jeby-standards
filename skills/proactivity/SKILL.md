---
name: proactivity
description: Infer small, directly implied improvements from explicit requirements while keeping scope bounded, evidence-based, and visible to the user; the partner of scope.
---

# Proactivity

Pairs with `scope`. Proactivity takes the small improvement a stated requirement directly implies. `scope` traces a change through every layer it touches before it is widened. Proactivity without scope drifts into unrequested work; scope without proactivity ships the literal words and misses the obvious.

Use whenever a stated requirement naturally implies a nearby usability, accessibility, consistency, or validation behavior.

- Infer only the smallest behavior required to make the stated intent work for a normal user. Examples: human-friendly wording implies human-friendly dates and numbers; sortable tables imply visible arrow state and keyboard semantics.
- State the inference briefly in the work update and keep it within the same conceptual change.
- Preserve settled domain rules, API boundaries, provenance, and authorization. Do not infer schema, destructive, external-service, or broad product changes from a UI request.
- Prefer a focused test or deterministic guard for each inferred behavior that could regress.
- If the inferred behavior changes data sent to the server, verify the contract and preserve the original value for auditability; otherwise stop and present it as a separate proposal.
- `restraint` classes any step beyond the literal request (In, Gray, Dark); proactivity never reclassifies a Dark step to keep moving.
- After a substantive inferred improvement, record the evidence and any unresolved validation in the ticket Report (and a lesson, rule plus test, when it prevents a repeat failure) rather than claiming the pattern is universally solved.
