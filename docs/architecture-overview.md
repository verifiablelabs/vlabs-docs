# Public architecture overview

Enthym's public work connects evaluation interfaces, verification specifications,
and evidence records. The [public repository map](repository-map.md) identifies
their maintained homes.

## Interfaces

The SDK defines evaluation contracts, score sets, split policies, transfer
metrics, and assurance cards. Its provider interface includes a deterministic
dummy provider. The promotion-gate CLI compares supplied evidence with defined
criteria; it does not itself produce a model-training result.

The SDK configuration exposes the mode names `evaluate_only`, `gate_only`,
`improve_and_gate`, and `substrate`, with capability flags. Those definitions
do not themselves execute an evaluation, change a configuration, or collect
records. A report must identify whether an intervention changes model
parameters, prompts, memory, or configuration.

## Verification

The public integrity tool audits known deviation classes using a trusted
reference and input generator. Passing those checks is scoped evidence, not
proof that every possible solution is correct. Read that repository's execution
and isolation requirements before using custom candidate source.

Selected mathematical properties of the promotion gate are machine-verified in
Lean 4. A hand-maintained Python mirror has property tests derived from selected
definitions; no mechanized code-to-proof parity is claimed. These specifications
do not prove the surrounding service or model-training outcomes.

## Records and disclosure

Public synthetic examples demonstrate the structure of supplied metrics and
assurance cards. Historical benchmark reports measure particular verifier
behavior under their recorded protocols. Neither establishes a released model
checkpoint or general intelligence.

Private implementations, evaluation material, and internal experiment findings
stay in access-controlled records. Public summaries need evidence review and
release approval. See [data boundaries](security-boundary.md) and
[publication workflow](operating-model-github-hf-wandb.md).
