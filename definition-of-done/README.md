# Definition of Done (modular)

"Done" is a claim about a complete outcome, supported by evidence, approved in the owner's own words. It is never a synonym for code written, a card moved, a green test, a 200 response, or a feature mentioned in a doc.

## How it composes
- `core.md` applies to every ticket of every kind: software, data, writing, paperwork, research, a decision.
- A ticket names the other modules that apply in its frontmatter: `dod: [core, code, docs]`. The reviewer checks exactly those. Anything not named is explicitly out of scope, so silence is never an excuse and never a burden.
- Each module is a short list of checks. A check passes with evidence, fails, is blocked, or is inapplicable with a one-line reason. "Looks right" is none of those.
- Levels of project management plug in the same way: a solo weekend project names `[core]`; a client deliverable names `[core, code, api, docs, release]`; a tax chore names `[core, admin]`.

| Module | Use when the ticket... |
| --- | --- |
| `core` | always |
| `code` | changes source code |
| `data` | changes a schema, a migration, a fixture, an intake pipeline |
| `api` | changes an endpoint or a contract |
| `ui` | changes a screen, a page, a form, a chart |
| `docs` | should change documentation (nearly every code ticket) |
| `content` | produces writing, copy, a script, a film document, a page for people |
| `admin` | is paperwork, an account, a filing, a payment, a calendar item |
| `research` | produces an analysis, a brief, a recommendation |
| `hardware` | touches a device, a sensor, a board, a physical build |
| `decision` | asks the owner to choose |
| `release` | makes something public: a push to a public repo, a deploy, a publish |

## Status vocabulary (use the narrowest true label)

| Label | Meaning |
| --- | --- |
| Proposed | described, not verified |
| Implemented | exists and was read through for the intended path |
| Test-covered | focused automated checks passed for named boundaries |
| Runtime-verified | the real stack completed the workflow and returned verified content |
| Reviewed | an independent reviewer (agent or person) read the diff against the acceptance and the named modules |
| User-validated | the owner exercised it and said so |
| Done | every named module has evidence, every omission is inapplicable with a reason, no known blocker contradicts the claim, and the owner approved in words |
| Production-ready | Done plus the `release` module |

Never upgrade one label into another.

## The completion record
Every ticket's Report carries a compact evidence matrix: one row per acceptance line, with implementation, focused test, runtime or human evidence, and the result or limitation. Source: generalized from jRE's `docs/guides/DEFINITION_OF_DONE.md` (the strict evidence contract), kept compatible with it.
