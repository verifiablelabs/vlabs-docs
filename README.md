# Enthym documentation

Enthym develops AI learning methods, starting with coding and using verification
to study the quality of feedback. Increasingly general models are a research
goal. Our public work provides evaluation interfaces, selected formal
specifications, audit tools, and evidence formats.

The GitHub organization remains `verifiablelabs`; repository and package names
retain their Verifiable Labs identifiers. Use Enthym for the startup brand while
preserving technical names and historical attribution.

## Start here

- [Research direction and public evidence](docs/product-overview.md): scope,
  demonstrations, historical reports, and evidence needed for a model claim.
- [Public repository map](docs/repository-map.md): implemented tools,
  demonstrations, monitoring configuration, and the archived predecessor.
- [Local entrypoints](docs/onboarding.md) and
  [contributor workflow](docs/contributor-workflow.md): where to start,
  validate a change, and prepare it for review.
- [Architecture](docs/architecture-overview.md),
  [positioning](docs/positioning.md), [data boundaries](docs/security-boundary.md),
  and [publication workflow](docs/operating-model-github-hf-wandb.md).

## Check these docs locally

Requires Python 3.11 or newer. These checks use the standard library only.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
git diff --check
git diff --cached --check
```

The checker catches selected unsupported-claim phrases, secret-shaped strings,
and broken local Markdown links. It does not validate scientific results,
external links, live services, every prose claim, or all forms of private data.
Review the evidence and disclosure boundary alongside every claim.

## License

[Apache-2.0](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md) and
[SECURITY.md](SECURITY.md).
