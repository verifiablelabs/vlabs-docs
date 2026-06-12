# SDK and CLI (public surface)

## Schemas and config

- `RunConfig` — modes `evaluate_only` (default) / `gate_only` /
  `improve_and_gate` / `substrate`, privacy-preserving defaults.
- `EvaluationContract`, `ScoreSet`, `TransferMetrics`, `GateOutcome`,
  `AssuranceCardV2`, split policy validation.
- `ModelProvider` interface (`validate_config` / `estimate_cost` / `run` /
  `dry_run`) with a deterministic `DummyProvider`.

## Install

```bash
pip install vlabs-sdk   # import name: vlabs_sdk
```

```python
from vlabs_sdk.providers.dummy_provider import DummyProvider
from vlabs_sdk.schemas import AssuranceCardV2, ScoreSet
from vlabs_sdk.run_config import default_config
```

(Migrating from the legacy `verifiable-labs-envs` package? See
[vlabs-sdk MIGRATION.md](https://github.com/verifiablelabs/vlabs-sdk/blob/main/MIGRATION.md).)

## clean-gate CLI

```bash
vlabs clean-gate --old baseline.json --new candidate.json
# exit 0 = ACCEPT, exit 1 = REJECT (reasons printed)
```

See runnable demos in
[vlabs-examples](https://github.com/verifiablelabs/vlabs-examples).
