# Local entrypoints

Choose a maintained repository from the [public map](repository-map.md).
Archived repositories provide provenance and historical source.

## Documentation

With Python 3.11+ in a local checkout, run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
git diff --check
git diff --cached --check
```

These commands use only the standard library. See [CONTRIBUTING](../CONTRIBUTING.md)
for the review workflow and the checks' limits.

## SDK and demonstrations

Start with [SDK and CLI](sdk-and-cli.md), read the current card migration notes,
and select compatible synthetic examples. The dummy provider and supplied-card
gate require no provider key. The SDK does not include a trained Enthym model.

The [terminal demo](https://github.com/verifiablelabs/vlabs-demo) runs on embedded
toy cases from a reviewed checkout. The [integrity tool](https://github.com/verifiablelabs/vlabs-integrity)
has a different execution boundary: inspect its isolation requirements before
custom audits. A demo command does not establish safe execution of arbitrary
untrusted source.

## Formal specifications and evidence

Follow the formal repository's CONTRIBUTING file and separate Lean and Python
workflows. For evidence changes, follow the evidence repository's validator
and checksum policy. These checks validate different properties; passing one
does not substitute for the others.

## Internal contributions

Contributors with private access should use the relevant repository's own
instructions, current branch, and workflow. Confirm the owning repository
before editing an integration copy. Keep private repository navigation and
findings in approved internal records. Model/provider execution and publication
require their own authorization, dependencies, and resource budget.

See [contributor workflow](contributor-workflow.md) and
[research direction and public evidence](product-overview.md).
