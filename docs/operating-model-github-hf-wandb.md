# Operating model: GitHub / Hugging Face / W&B (public summary)

- **GitHub** — open-core split: SDK contracts, formal track, examples,
  evidence, and docs are public; scenario generation, contamination
  firewall, anti-hack engine, platform, and all runs/data are private.
- **Hugging Face** — only redacted, license-clean artifacts are ever
  published, gated by an export-policy check and an explicit approval flag.
- **Weights & Biases** — dashboards carry sanitized metrics only (no
  hidden-eval content, no raw traces, no keys), same approval gating.

What is never published anywhere: hidden evaluation content, gold answers,
anti-hack detection details, private verifier logic, raw or customer
traces, secrets.

## Published evidence

Public, **synthetic / redacted** demo evidence:

- **Hugging Face dataset** — <https://huggingface.co/datasets/verifiablelabs/vlabs-clean-gate-evidence>
- **Weights & Biases** (entity `verifiable-labs`): [clean-generalization-gate](https://wandb.ai/verifiable-labs/clean-generalization-gate) · [contamination-firewall](https://wandb.ai/verifiable-labs/contamination-firewall) · [anti-hack-engine](https://wandb.ai/verifiable-labs/anti-hack-engine) · [scenario-compiler](https://wandb.ai/verifiable-labs/scenario-compiler) · [runpod-costs](https://wandb.ai/verifiable-labs/runpod-costs)

All published evidence is **synthetic / redacted** and is **not a training
dataset**. It contains **no** customer data, hidden evaluations, gold
answers, raw traces, private anti-hack traps, or private engine internals.

Install the SDK: `pip install "vlabs-sdk==0.0.2"`
