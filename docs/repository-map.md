# Repository map

This is the canonical navigation and ownership map for Verifiable Labs,
reviewed on 2026-09-26. The company develops AI models and learning methods;
verification and evaluation infrastructure support that program. Repository
names describe components, not separate company strategies.

Private links require organization access. “Current home” identifies where
changes belong; it does not imply a released product, independently replicated
result, or healthy production deployment.

## Model and agent research — private

| Repository | Current responsibility | Evidence or entrypoint |
|---|---|---|
| [vlabs-selfimprove](https://github.com/verifiablelabs/vlabs-selfimprove) | Coding-model post-training and verifier-filtered SFT | V4 preregistration, results, and numeric analysis |
| [vlabs-continual](https://github.com/verifiablelabs/vlabs-continual) | Curriculum, persistent experience, and model-fitting experiments | V6 preregistration, results, and numeric analysis; V5 is a historical stage |
| [vlabs-research](https://github.com/verifiablelabs/vlabs-research) | Typed research records, transfer accounting, and split contracts | Code and tests; this component is not the trainer or the current result store |
| [certloop](https://github.com/verifiablelabs/certloop) | Proof-producing reasoning and self-correction prototype | Synthetic offline fixtures; larger benchmark claims need their own data and run evidence |
| [vlabs-runs-internal](https://github.com/verifiablelabs/vlabs-runs-internal) | Validated experiment plans | Planning scaffold only; it does not launch or execute runs |

World-model research is planned. No repository is presented here as a shipped
world model. The [research overview](product-overview.md) separates current
results from the long-term goal of increasingly general intelligence.

## Public interfaces, evidence, and communication

| Repository | Current responsibility |
|---|---|
| [vlabs-sdk](https://github.com/verifiablelabs/vlabs-sdk) | Public SDK contracts, schemas, provider interface, and promotion-gate CLI |
| [vlabs-formal](https://github.com/verifiablelabs/vlabs-formal) | Selected Lean specifications and their Python mirror |
| [vlabs-evidence](https://github.com/verifiablelabs/vlabs-evidence) | Approved public benchmark reports and separately labelled synthetic evidence |
| [vlabs-examples](https://github.com/verifiablelabs/vlabs-examples) | Synthetic SDK examples |
| [vlabs-integrity](https://github.com/verifiablelabs/vlabs-integrity) | Public verifier-gameability audit tooling |
| [vlabs-demo](https://github.com/verifiablelabs/vlabs-demo) | Small terminal demonstration of reward-gameability checks |
| [vlabs-docs](https://github.com/verifiablelabs/vlabs-docs) | Public research scope, architecture, setup, and this map |
| [.github](https://github.com/verifiablelabs/.github) | Public organization profile |
| [vlabs-status](https://github.com/verifiablelabs/vlabs-status) | Status-monitoring automation; monitor configuration is not a service-health guarantee |

## Research and service infrastructure — private

| Repository | Current responsibility |
|---|---|
| [vlabs-verifier-robustness-engine](https://github.com/verifiablelabs/vlabs-verifier-robustness-engine) | Coding-verifier robustness engine and benchmark work |
| [vlabs-gameability](https://github.com/verifiablelabs/vlabs-gameability) | Gameability audit implementation and service integration |
| [vlabs-scenario-compiler](https://github.com/verifiablelabs/vlabs-scenario-compiler) | Evaluation-contract and scenario-draft generation |
| [vlabs-contamination-firewall](https://github.com/verifiablelabs/vlabs-contamination-firewall) | Split, contamination-risk, and release-policy implementation |
| [vlabs-anti-hack-engine](https://github.com/verifiablelabs/vlabs-anti-hack-engine) | Private reward-gaming and security checks |
| [vlabs-private-eval-vault](https://github.com/verifiablelabs/vlabs-private-eval-vault) | Evaluation-vault policy and storage scaffold; no frozen evaluation corpus is established by the scaffold |
| [vlabs-platform](https://github.com/verifiablelabs/vlabs-platform) | Hosted API, access, billing, and reviewed integration copies of engines |
| [vlabs-infra](https://github.com/verifiablelabs/vlabs-infra) | Deployment configuration and operational runbooks |
| [verifiable-labs-website](https://github.com/verifiablelabs/verifiable-labs-website) | Company website and public research presentation |

Changes to a split engine originate in its owning repository. The platform's
integration copies require a reviewed sync; editing an archived predecessor
will not update the maintained service. Training experiments have their own
dependencies and are not automatically executed by the hosted platform.

## Archived predecessors

| Repository | Historical role | Use today |
|---|---|---|
| [verifiable-labs-envs](https://github.com/verifiablelabs/verifiable-labs-envs) — public, archived | Earlier environment/SDK monorepo | Historical source and provenance; use `vlabs-sdk` and `vlabs-formal` for their maintained surfaces |
| [verifiable-labs-private](https://github.com/verifiablelabs/verifiable-labs-private) — private, archived | Earlier private integration monorepo | Historical source and provenance; follow the split ownership above |

Some deployed or research paths may retain pinned legacy runtime dependencies.
Archived status does not prove those dependencies have been migrated. Preserve
those pins until the owning repository verifies a replacement; do not use an
old README as the current organization map. No rename, deletion, or archive
transition is required by this map.
