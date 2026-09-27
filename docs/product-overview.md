# Research program and evidence

Verifiable Labs develops learning methods and models, beginning with coding.
The commercial objective is to turn reliable learning from experience into
useful model capabilities. Verification tools and the evaluation platform
provide training feedback and measurement for that work.

## Current program

| Area | Implemented or recorded today | Next research question |
|---|---|---|
| Coding post-training | Filtered SFT with QLoRA adapters; generation, trajectory selection, fitting, and held-out evaluation in `vlabs-selfimprove` | Does better feedback improve correctness and transfer at a matched total budget? |
| Learning agents | Curriculum/control experiments, persistent experience, and repeated fitting in `vlabs-continual` | Which gains come from weights, curriculum, replay, or the surrounding agent? |
| Verification and formal methods | Reward-gameability checks, evidence schemas, split policy, promotion gates, and selected Lean specifications | How well do feedback signals predict downstream learning on new tasks? |
| World models | Planned research direction; no trained world-model result established here | Can the method extend to learning environment dynamics and planning? |

The implemented training is parameter adaptation of existing pretrained
models. Each current cycle fits a fresh adapter from the original base using
accumulated examples. This is filtered SFT with persistent experience; a
continuing-weight learning method remains a separate experiment.

## Evidence ledger

This summary describes the reviewed V4/V6 experiment records, not a new
training run or an independent checkpoint reproduction. Private links require
organization access.

| Evidence | Supported conclusion | Boundary |
|---|---|---|
| [Selfimprove V4](https://github.com/verifiablelabs/vlabs-selfimprove/blob/main/RESULTS_V4.md) | The Llama comparison found lower hidden-test failure among visible-test-passing outputs after verifier-filtered training | The metric includes ordinary incorrect generalization as well as shortcuts; held-out accuracy superiority was not established. The smaller Gemma comparison was inconclusive. |
| [Continual V6](https://github.com/verifiablelabs/vlabs-continual/blob/main/RESULTS_V6.md) | Recorded model fitting and exploratory transfer between coding families | The preregistered external transfer comparison did not establish a model-controller advantage. Equal fit/row budgets are not proof of equal tokens or total compute. |
| [Public benchmark reports](https://github.com/verifiablelabs/vlabs-evidence/tree/main/results) | Historical measurements of particular verifier behavior on public benchmarks | Execution-time source/data revisions are incomplete; these are not model-training results or newly reproduced runs. Read the [reproducibility notes](https://github.com/verifiablelabs/vlabs-evidence/blob/main/reproducibility-notes.md). |
| [Public examples](https://github.com/verifiablelabs/vlabs-evidence/tree/main/evidence) | Synthetic demonstrations of evidence and assurance-card formats | These are illustrative, not measured model capability or training datasets. |
| [Formal track](https://github.com/verifiablelabs/vlabs-formal) | Selected mathematical properties under explicit assumptions | It does not prove the surrounding service, training outcomes, general intelligence, or implementation-to-proof equivalence. |

The reviewed training repositories contain training logs and saved result
records, but not a complete checkpoint bundle that an outside researcher can
load and independently reproduce. Artifact recovery, immutable revisions,
sealed evaluation, and a checkpoint/evaluation package are the next evidence
milestone. No released checkpoint is implied by the SDK or synthetic demos.

## Direction

Near-term work centers on reproducible coding-model results, controlled
learning-agent experiments, and separating gains from feedback, training
data, and curriculum. World models are a planned extension beyond coding.
Increasing generality and AGI are long-term goals; neither is a current
experimental result.

The existing evaluation platform remains supporting infrastructure. Its
`evaluate_only`, `gate_only`, `improve_and_gate`, and `substrate` modes describe
software interfaces; they are not evidence that a commercial model endpoint
or every hosted workflow is currently available. See
[architecture](architecture-overview.md) and [local entrypoints](onboarding.md).
