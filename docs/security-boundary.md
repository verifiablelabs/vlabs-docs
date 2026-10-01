# Data and implementation boundaries

The model research program needs both inspectable evidence and protected
evaluation content. Training data, controller feedback, and final evaluation
sets have different roles; their permitted uses must remain explicit.

**Public:** SDK contracts and CLI, selected Lean specifications and Python
mirrors, synthetic examples, public documentation, and approved labelled
aggregate benchmark reports.

**Private:** model-training implementations and internal run artifacts,
protected evaluation content and gold answers, private verifier details,
raw/customer traces, and credentials. A repository's code license does not
change its visibility or authorize export of protected data.

Follow each maintained repository's disclosure policy and review the applicable
execution and export path before releasing an artifact. This public page does
not establish private implementation details or deployed enforcement.

The public SDK's default `RunConfig` sets `public_export=false` and
`allow_future_training_use=false`. These are requested configuration values;
runtime enforcement must be verified in the owning workflow. Model-training
experiments require their own explicit training-data policy and split manifest.
A final test set must stay outside training and any controller feedback if it is described as sealed; a reused validation score is a control
signal, even when the underlying task text remains hidden.

Post-freeze generation, duplicate checks, and access controls reduce specific
contamination risks. They do not prove novelty relative to unknown base-model
training data. Formal results cover selected mathematical specifications,
not the confidentiality or correctness of the whole service.

Public result summaries must preserve provenance and limitations without
including protected content. Follow the [publication workflow](operating-model-github-hf-wandb.md)
and [security policy](../SECURITY.md).
