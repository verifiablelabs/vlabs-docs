# Product overview

Verifiable Labs runs in four customer-selectable modes. The default is the
most private one.

| Mode | What it does |
|---|---|
| **evaluate_only** (default) | Compile an evaluation contract, generate public/hidden/OOD/adversarial scenarios, score clean performance with contamination + hack-risk analysis. No agent mutation, no export. |
| **gate_only** | Baseline vs candidate: clean VGS delta, hidden/OOD transfer, contamination + hack risk, cost/latency — ACCEPT / REJECT / LIMITED_ROLLOUT with an assurance card. |
| **improve_and_gate** | Evaluate, diagnose failures, propose human-reviewed improvement suggestions and candidate configs, re-gate. Never auto-applied. |
| **substrate** | Clean feedback records, transfer metrics, failure memory, generated curriculum — per explicit data policy. |

Privacy-preserving defaults: nothing is exported, nothing is reused for
training (`allow_future_training_use: false`), and human review is
required.

## Onboarding paths

1. **Dashboard upload** — upload an agent bundle; we compile a contract
   draft, scenario plan, and dry-run cost estimate.
2. **CLI / API key** — drive runs from your terminal or CI.
3. **Bring your own key (BYOK)** — your provider key, encrypted and
   project-scoped; we charge orchestration/scoring only, no token markup.
4. **Self-hosted / VPC** — run inside your boundary (architecture defined;
   productionization in progress).

## Provider support

A provider abstraction with a deterministic dummy provider is implemented
and CPU-smoke-tested end-to-end; commercial providers plug in behind the
same interface.
