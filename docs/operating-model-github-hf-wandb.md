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
