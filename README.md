# Verifiable Labs documentation

Verifiable Labs is a commercial AI model company working toward increasingly
general, self-improving intelligence. Our current research starts with
verifier-guided post-training of coding models, supported by evaluation,
agent-learning experiments, and selected formal specifications.

## Start here

- [Research program and evidence](docs/product-overview.md): implemented
  training, recorded findings, limitations, and planned world-model research.
- [Repository map](docs/repository-map.md): where each maintained component
  lives, what is private, and which repositories are archived.
- [Local setup and contributor entrypoints](docs/onboarding.md): begin with
  documentation, SDK examples, or the relevant private research repository.
- [Architecture](docs/architecture-overview.md): how model learning and
  verification fit together.
- [Positioning and claim boundaries](docs/positioning.md),
  [data boundaries](docs/security-boundary.md), and
  [publication workflow](docs/operating-model-github-hf-wandb.md).

## Check these docs locally

Requires Python 3.11 or newer. The checks use the standard library only;
there is no package install, model download, GPU, or provider key.

```bash
git clone https://github.com/verifiablelabs/vlabs-docs.git
cd vlabs-docs
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
```

The checker catches selected unsupported-claim phrases, secret-shaped
strings, and broken local Markdown links. It does not verify scientific
results, external links, live service availability, or every possible prose
claim. Review the evidence and its limitations alongside every result.

## License

Apache-2.0. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
