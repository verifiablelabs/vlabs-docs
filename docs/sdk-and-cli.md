# SDK and CLI (public surface)

## Schemas and config

- `RunConfig` — modes `evaluate_only` (default) / `gate_only` /
  `improve_and_gate` / `substrate`, privacy-preserving defaults.
- `EvaluationContract`, `ScoreSet`, `TransferMetrics`, `GateOutcome`,
  `AssuranceCardV2`, split policy validation.
- `ModelProvider` interface (`validate_config` / `estimate_cost` / `run` /
  `dry_run`) with a deterministic `DummyProvider`.

## clean-gate CLI

```bash
vlabs-prm-eval clean-gate --old baseline.json --new candidate.json
# exit 0 = ACCEPT, exit 1 = REJECT (reasons printed)
```

See runnable demos in
[vlabs-examples](https://github.com/verifiablelabs/vlabs-examples).
