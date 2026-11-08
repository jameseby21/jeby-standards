# api

- [ ] Authorization asserted for anonymous, insufficient-role and intended-role callers, separately from hidden navigation.
- [ ] Status and payload asserted separately; required fields, types, counts, ordering, nullability, redaction and pagination checked.
- [ ] Validation errors name the field, the value, the reason and a suggestion.
- [ ] Database and audit state asserted independently of the response body.
- [ ] Conflict, dependency failure, retry and idempotency behavior asserted where the endpoint mutates state (idempotency keys wherever money or external calls exist).
- [ ] Internal IDs, secrets and private fields do not leak.
- [ ] Contract snapshot (OpenAPI or equivalent) regenerated and committed.
