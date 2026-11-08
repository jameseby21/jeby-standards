# Assignment: every ticket has a person, and workflows map to one

James's rule (2026-11-08): "Every ticket needs an assignee -- as a quick completion check to see which tickets I've "scanned" so far we can check whether assignation is blank (should be a warning now, will be an error eventually) or not. The dropdown options should be all your coworkers, myself, or "Patch" (yourself). Some workflows can be automatically mapped to a specific assignee, like "human review" to myself and "design review" to Chaz and security to big D etc..."

- `assignee` is never blank on a ticket that has left inbox. A blank is a warning today and an error from 2026-11-22 (Desk `desk.toml [rules] assignee_required_from`). Until then James uses blank as "I have not scanned this yet", so nobody fills blanks for him.
- The people are: James (`james`), Patch (`main`, shown as Patch), Chaz (creative director), Em (research), Bri (assistant), Joe (boring stuff: legal, finance, channel), Lily (tech, product, IT), Big D (security), and the code sessions `code:<project>` (a project's own Claude Code session). The list lives in `people.yaml` in the Desk store; the UI dropdown reads it.
- Workflows map to a person by default (Desk `assign.yaml`; a rule never overrides a set assignee):

| Work | Assignee |
| --- | --- |
| human review, approve, choose, answer, provide, any decision | james |
| design, brand, anything a person will see (before it is built) | chaz |
| security, secrets, access, the `security` project | bigd |
| research briefs, market or vendor checks | em |
| tech, product, IT, infrastructure, performance | lily |
| calendar, orders, tracking, admin steps | bri |
| legal, finance, pricing, channel, boring stuff | joe |
| build, implementation, filing, dispatch | main (Patch) |
| code inside a project repo | code:<project> |
