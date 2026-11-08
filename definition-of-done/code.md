# code

- [ ] Branch per ticket; conventional commits; no `--no-verify`; no force-push.
- [ ] Focused test written or identified before implementation when practical; observed failing for the missing behavior; every regression test states the behavior it protects.
- [ ] Tests assert outcomes, not execution; deterministic, isolated, independent of order and of local data.
- [ ] Change-aware inspection run: the persistent baseline plus every test for the affected scope; full inspection at milestone and release gates.
- [ ] Lint and format clean on touched files.
- [ ] Error paths behave intentionally: empty, boundary, malformed, duplicate, stale and hostile inputs.
- [ ] Long-running scripts show progress and a final summary; large files are streamed and released, never held all at once.
- [ ] Dependencies pinned to versions that resolve on a clean install on every supported platform; unsupported platforms named as unverified.
- [ ] Reviewer agent ran on the diff against the acceptance; findings fixed or recorded.
