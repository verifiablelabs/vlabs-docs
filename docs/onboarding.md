# Local setup and entrypoints

Choose the repository for the work you need. The [repository map](repository-map.md)
is the ownership guide; archived monorepos are historical references.

## Public documentation

Python 3.11+ is sufficient. No package installation is needed.

```bash
git clone https://github.com/verifiablelabs/vlabs-docs.git
cd vlabs-docs
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
```

## Public SDK

Start with [SDK and CLI](sdk-and-cli.md) to install from a current checkout,
inspect the gate command, and use the synthetic examples. The SDK does not
include a trained Verifiable Labs model. A provider key is not required for
its deterministic dummy provider or supplied-card gate.

## Research contributors with private access

| Work | Starting point |
|---|---|
| Coding post-training | [vlabs-selfimprove](https://github.com/verifiablelabs/vlabs-selfimprove): README, `PREREGISTRATION_V4.md`, `RESULTS_V4.md`, and `experiments/analyze_seal_v4.py` |
| Learning-agent experiments | [vlabs-continual](https://github.com/verifiablelabs/vlabs-continual): README, `PREREGISTRATION_V6.md`, `RESULTS_V6.md`, and `experiments/analyze_v6.py` |
| Experiment accounting | [vlabs-research](https://github.com/verifiablelabs/vlabs-research): typed episode records, split contracts, and transfer summaries |
| Run planning | [vlabs-runs-internal](https://github.com/verifiablelabs/vlabs-runs-internal): configuration validation and plan output; no run executor |
| Platform development | [vlabs-platform service README](https://github.com/verifiablelabs/vlabs-platform/blob/main/services/api/README.md): local API setup and dependencies |

Begin by inspecting recorded results and running the relevant repository's
local checks. Numeric result analysis is different from reproducing model
inference or training. Training requires the repository's specified runtime,
model/data access, compute budget, and experiment configuration; this docs
checkout does not provision those resources.

## Evidence review

Read the [evidence ledger](product-overview.md#evidence-ledger) before citing
results. Public [reproducibility notes](https://github.com/verifiablelabs/vlabs-evidence/blob/main/reproducibility-notes.md)
distinguish synthetic examples from historical measured reports. Any new
model result should connect its exact code/data revisions, checkpoint hashes,
held-out split, analysis, and limitations before it is used as a headline.
