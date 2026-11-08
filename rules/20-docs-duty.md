# Docs duty

- Docs change in the same commit as the code they describe, or the commit says why not: trailer `Docs: none - <reason>`.
- Each repo keeps `docs/doc-ownership.yaml` (glob -> doc#section). A changed file's owning section is updated or regenerated in the same change. Generated blocks are never hand-edited.
- One owner per fact. Link to it; never restate it. An unreachable doc is a defect.
- Dated records (audits, hand-offs, sprint logs) preserve evidence and never pose as current instructions.
- A passing validator is not proof the docs are true. Check computable facts (versions, counts, routes) against code before reporting.
