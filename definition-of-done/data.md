# data

- [ ] Migration upgrades from the previous head and from a fresh database; never edit a shipped migration.
- [ ] Schema shape, keys, uniqueness, checks, indexes, defaults, nullability and numeric precision match the contract.
- [ ] Provenance, temporal history, stable identifiers and real-versus-synthetic distinctions preserved; no real-world fact invented to make a fixture pass.
- [ ] Seed and repeat-seed deterministic; authorized edits survive a reseed.
- [ ] Representative normal, sparse, rich, duplicate, conflicting, outlier and corrupted records exercised.
- [ ] Readback: a separate query proves saved state; cascades checked up and down dependency paths.
- [ ] Real source data stays in the owner's vault; fixtures are labeled synthetic.
- [ ] Bulk jobs follow the staged protocol: unit test, one record end to end, a seeded sample, then the whole job; dry-run and sample controls exist.
