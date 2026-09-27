# Code, artifacts, and publication

**GitHub** holds maintained code, specifications, documentation, and approved
result summaries. Public and private ownership is listed in the
[repository map](repository-map.md). Training code and protected run data
remain private; a public documentation link does not grant access.

**Hugging Face** can hold approved model/data releases with license and
provenance review. The existing
[clean-gate evidence dataset](https://huggingface.co/datasets/verifiablelabs/vlabs-clean-gate-evidence)
is synthetic/redacted demonstration material, not a trained checkpoint or a
training dataset.

**Weights & Biases** can hold sanitized experiment metrics. The existing
[clean-generalization-gate](https://wandb.ai/verifiable-labs/clean-generalization-gate)
project is part of the synthetic demonstration surface. A dashboard or run
name alone is not evidence of a completed model-training experiment.

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
The reviewed V4/V6 records are discussed in the [research overview](product-overview.md).

## Preparing a model result

Join the hypothesis and preregistered endpoint to exact code, model/tokenizer,
data and split revisions; initial/final checkpoint hashes; environment and
commands; run identifiers; denominators and analysis; compute accounting; and
negative results. State whether learning changed weights, agent configuration,
or both. Retain protected raw artifacts in approved private storage.

Publication requires the repository's applicable export-policy checks and
explicit approval. Existing HF/W&B exporters default to dry runs; flags and
manifests are controls, not evidence that publication occurred. Never publish
protected evaluation content, gold answers, private detector details,
customer/raw traces, or credentials. See [data boundaries](security-boundary.md).
