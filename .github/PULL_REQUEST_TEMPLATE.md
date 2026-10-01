## Reader problem and change

Describe the affected page and the resulting wording or navigation.

## Public evidence

Link sources for factual or capability changes. State their limits and whether
the evidence is synthetic, historical, or measured. Explain Enthym wording while
preserving technical identifiers and attribution.

## Validation

List outcomes, or explain why a check was skipped:

- `python3 -m unittest discover -s tests -v` (Python 3.11+)
- `python3 scripts/check_docs.py`
- `git diff --check` and `git diff --cached --check`
- Markdown rendering and changed-link review

- [ ] Public additions contain no private repository names, code, findings,
      protected evaluations, gold answers, credentials, or raw/customer traces.
- [ ] Claims retain evidence and limitations; the checker alone does not
      approve scientific claims or disclosure.

<!-- Use SECURITY.md privately for security-sensitive reports. -->
