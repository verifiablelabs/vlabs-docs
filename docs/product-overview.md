# Research direction and public evidence

Enthym studies learning from experience, starting with coding and the quality
of verification feedback. Public evaluation and audit tooling supports that
research direction. World models and increasingly general intelligence are
future goals; the artifacts below do not establish those capabilities.

## Public evidence ledger

| Public surface | What it supports | Limits |
|---|---|---|
| [SDK](https://github.com/verifiablelabs/vlabs-sdk) | Typed contracts, a dummy provider, and CLI that gates supplied score cards | No trained model is supplied; accepting a card does not measure a new model |
| [Formal track](https://github.com/verifiablelabs/vlabs-formal) | Selected mathematical specifications and a hand-maintained Python mirror | Explicit assumptions; no mechanized implementation-to-proof parity or whole-service proof |
| [Integrity tooling](https://github.com/verifiablelabs/vlabs-integrity) | Audits against known deviation classes under a trusted reference and input generator | No universal correctness or unhackability claim; review the execution boundary |
| [Benchmark reports](https://github.com/verifiablelabs/vlabs-evidence/tree/main/results) | Historical reported verifier measurements on public benchmarks | Incomplete execution-time source/data revision records; no model-training results or newly reproduced runs |
| [Evidence fixtures](https://github.com/verifiablelabs/vlabs-evidence/tree/main/evidence) and [SDK examples](https://github.com/verifiablelabs/vlabs-examples) | Illustrative formats and synthetic supplied metrics | No measured customer or model capability |
| [Terminal demo](https://github.com/verifiablelabs/vlabs-demo) | Mechanism demonstration on constructed toy cases | No field detection, false-positive, latency, or model-comparison measurement |

Read the public [reproducibility notes](https://github.com/verifiablelabs/vlabs-evidence/blob/main/reproducibility-notes.md)
alongside historical measurements. Artifact checksums protect recorded bytes;
they do not independently attest to the original experiment or provide missing
run-time provenance. Source fixes do not retroactively revalidate old results.

## Evidence needed for a model result

An approved public model claim should identify the tested hypothesis, exact
code/model/data revisions, permitted checkpoint artifacts, train/validation/test
roles, evaluated endpoint, denominators, uncertainty, controls, compute
accounting, and limitations. Explain whether changes affect model parameters,
agent configuration, or both. Describe saved-record analysis separately from
training or inference reproduction.

Internal studies and private repository findings are reviewed in access-controlled
records. This page publishes no internal result summary. A public model release
or hosted endpoint needs its own release evidence and availability checks.

## Interfaces and availability

The SDK's `evaluate_only`, `gate_only`, `improve_and_gate`, and `substrate`
modes are software interfaces. Their names do not establish that every hosted
workflow is available or that each mode trains parameters. See
[architecture](architecture-overview.md), [local entrypoints](onboarding.md),
and the [public repository map](repository-map.md).
