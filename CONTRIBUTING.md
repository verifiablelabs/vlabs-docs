# Contributing to Enthym documentation

Small corrections can go straight to a pull request. Open a documentation issue
before restructuring several pages or changing the stated research direction.
Include the affected page, a public source, and proposed wording.

## Local checks

Use Python 3.11+; the existing documentation checks need no package installation,
provider credentials, model download, or GPU.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
git diff --check
git diff --cached --check
```

The `docs-check` workflow definition configures unit tests and the checker for
pull requests and pushes to `main`, using Python 3.12. Whitespace checks
are local review steps; the workflow does not currently run them. The checker
catches selected claim phrases, secret shapes, and local links; it does not approve scientific claims, private
disclosures, external links, or service availability. Inspect the Markdown diff
and rendered tables, headings, links, and code blocks as part of review.

## Review expectations

- Describe the reader problem and resulting wording or navigation change.
- Link public evidence for a capability, numeric result, or status change.
  State its endpoint, limitations, and whether it is synthetic or measured.
- Use Enthym in company prose while preserving repository, package, import,
  CLI, citation, and license identifiers.
- Keep private repository names, code, findings, evaluation content, gold
  answers, raw/customer traces, and credentials out of public changes.
- Report checks actually run and reasons for skipped checks; distinguish
  local validation from completed CI or experiment reproduction.

Contributions to this repository use its [Apache-2.0 license](LICENSE).
For suspected vulnerabilities or accidental disclosures, follow
[SECURITY.md](SECURITY.md) privately. See the
[contributor workflow](docs/contributor-workflow.md) and
[claim boundaries](docs/positioning.md).
