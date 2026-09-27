# Architecture overview

The model research program connects three layers: learning code, verification
and evaluation, and evidence. The [repository map](repository-map.md)
identifies the maintained home for each component.

## Model learning

`vlabs-selfimprove` implements a coding loop: generate candidate solutions,
select training examples, fit a QLoRA adapter, and evaluate. `vlabs-continual`
adds experiments with curriculum control, persistent experience, and teacher
feedback. The current implementations fit fresh adapters from the base model
on accumulated experience; they do not incrementally update the previous
cycle's adapter weights.

A change to a model's parameters is different from a prompt, memory prefix,
or agent configuration change. Reports must identify which changed and
measure each contribution through controls. The broader research goal is
reliable transfer to new tasks, not a higher score under one evaluator.

## Verification and evaluation

The supporting evaluation architecture includes:

1. Evaluation contracts and scenario drafts with explicit split policy.
2. Provider interfaces and evaluation runners; the public SDK includes a
   deterministic dummy provider.
3. Checks for contamination risk and reward gaming, with evidence attached
   to the decision.
4. Promotion gates that compare supplied measurements against defined
   criteria and produce typed assurance cards.
5. Episode records, transfer summaries, and failure bookkeeping.

A generated scenario draft needs a trusted scoring oracle before it supports
a semantic correctness claim. Generating after a recorded model freeze is a
contamination-reduction measure: ordering timestamps does not authenticate
them or rule out semantic overlap with unknown pretraining data. Likewise,
passing a verifier is evidence under that verifier's scope, not proof that an
accepted solution is correct on every input.

The platform's four modes describe evaluation, gating, human-reviewed
configuration suggestions, and record collection. Their `improve_and_gate`
mode must not be confused with the parameter-training loops above. The
`vlabs-research` record schemas and `vlabs-runs-internal` planning scaffold do
not themselves train models or execute the planned experiments.

## Formal and data boundaries

Selected mathematical properties behind the contamination-resistant
promotion gate are machine-verified in Lean 4. A hand-maintained Python mirror
has property tests derived from selected definitions; no mechanized
code-to-proof parity is claimed. Theorems about accepted sequences assume the
stated gate conditions hold; they do not guarantee that a training process
will produce such a sequence.

Private learning and evaluation components remain private. Public contracts,
selected specifications, and approved aggregate evidence provide inspectable
interfaces without exposing protected evaluation content. See
[data boundaries](security-boundary.md).
