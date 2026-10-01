# Code, artifacts, and publication

**GitHub** holds maintained code, specifications, documentation, and approved
result summaries for Enthym. The [public repository map](repository-map.md)
lists public surfaces only. Internal ownership and research findings stay in
access-controlled records; private access does not authorize public export.

**Hugging Face** can hold approved model/data releases with license and
provenance review. The public evidence repository links to a
[clean-gate evidence dataset](https://huggingface.co/datasets/verifiablelabs/vlabs-clean-gate-evidence)
and labels that material synthetic/redacted, rather than a trained checkpoint
or training dataset. This page does not establish current host availability.

**Weights & Biases** can hold sanitized experiment metrics. The public evidence
repository links to [clean-generalization-gate](https://wandb.ai/verifiable-labs/clean-generalization-gate)
as synthetic demonstration material. A dashboard or run name alone is not
proof of a completed model-training experiment. See the
[public evidence README](https://github.com/verifiablelabs/vlabs-evidence/blob/main/README.md)
for the source of those descriptions.

## Evidence categories

Keep these separate in filenames, descriptions, and claims:

- Synthetic fixtures demonstrate formats and workflow behavior.
- Historical measured reports describe recorded results with their original
  limitations; new source fixes do not retroactively revalidate them.
- Model-training records connect actual fitting to evaluated checkpoints.
- Reproducible model releases additionally supply loadable permitted
  artifacts, immutable dependencies, and a documented evaluation procedure.

The current public benchmark reports live separately in
[vlabs-evidence/results](https://github.com/verifiablelabs/vlabs-evidence/tree/main/results).
They must be read alongside the
[reproducibility notes](https://github.com/verifiablelabs/vlabs-evidence/blob/main/reproducibility-notes.md).
The [research overview](product-overview.md) separates public evidence categories.

## Preparing a model result

Join the hypothesis and preregistered endpoint to exact code, model/tokenizer,
data and split revisions; initial/final checkpoint hashes; environment and
commands; run identifiers; denominators and analysis; compute accounting; and
negative results. State whether learning changed weights, agent configuration,
or both. Retain protected raw artifacts in approved private storage.

Publication requires the repository's applicable export-policy checks and
explicit approval. The public evidence README describes approval flags and
dry-run defaults; this page does not independently verify exporter enforcement
or establish that a particular upload occurred. Never publish
protected evaluation content, gold answers, private detector details,
customer/raw traces, or credentials. See [data boundaries](security-boundary.md).
