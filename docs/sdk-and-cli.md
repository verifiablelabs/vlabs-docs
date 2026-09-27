# SDK and CLI

The public SDK provides evaluation contracts, typed evidence, provider
interfaces, and a promotion-gate CLI. It is supporting infrastructure for the
model research program; it does not contain a trained model.

## Local setup

Requires Python 3.11+. Installing from the maintained checkout avoids relying
on a stale version in an older documentation page. Installation needs network
access for dependencies.

```bash
git clone https://github.com/verifiablelabs/vlabs-sdk.git
cd vlabs-sdk
python3 -m venv .venv
source .venv/bin/activate
python -m pip install .
vlabs --help
vlabs clean-gate --help
```

The import package is `vlabs_sdk`; the command is `vlabs`.

```python
from vlabs_sdk.providers.dummy_provider import DummyProvider
from vlabs_sdk.schemas import AssuranceCardV2, ScoreSet
from vlabs_sdk.run_config import default_config
```

To compare existing, schema-valid score files:

```bash
vlabs clean-gate --old baseline.json --new candidate.json
# exit 0 = ACCEPT, exit 1 = REJECT (reasons printed)
```

`baseline.json` and `candidate.json` are inputs you supply, not files created
by the installation. Use [vlabs-examples](https://github.com/verifiablelabs/vlabs-examples)
for synthetic inputs and the
[SDK migration notes](https://github.com/verifiablelabs/vlabs-sdk/blob/main/MIGRATION.md)
for the current card format. Gate acceptance checks supplied evidence against
defined criteria; it is not a new model evaluation.

## Interfaces

- `RunConfig`: `evaluate_only`, `gate_only`, `improve_and_gate`, and `substrate`.
- `EvaluationContract`, `ScoreSet`, `TransferMetrics`, `GateOutcome`, and
  `AssuranceCardV2`, with split-policy validation.
- `ModelProvider`: `validate_config`, `estimate_cost`, `run`, and `dry_run`;
  the public implementation includes `DummyProvider`.

The evaluation configuration defaults to no export and no future training
reuse. Those defaults govern that workflow; they do not describe the separate,
explicitly configured model-training experiments.
