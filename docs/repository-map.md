# Public repository map

Enthym's public GitHub work remains under `verifiablelabs`. Existing repository,
package, import, and command names retain the Verifiable Labs identifiers.
This map was checked against public repository metadata on 2026-09-30.

“Implemented” describes code present in a maintained repository. It does not
establish a package release, independent reproduction, or live service health.
Demonstrations and historical results have separate evidence roles.

## Maintained public work

| Repository | Role and maturity | Contributor entrypoint |
|---|---|---|
| [vlabs-docs](https://github.com/verifiablelabs/vlabs-docs) | Documentation: research direction, public scope, and contribution guidance | README, CONTRIBUTING, and standard-library documentation checks |
| [.github](https://github.com/verifiablelabs/.github) | Organization profile and shared contribution guidance | `profile/README.md` and repository README; Markdown review |
| [vlabs-sdk](https://github.com/verifiablelabs/vlabs-sdk) | Implemented interfaces: typed contracts, supplied-evidence promotion gate, CLI, and dummy provider | README, `MIGRATION.md`, `pyproject.toml`, and CI |
| [vlabs-formal](https://github.com/verifiablelabs/vlabs-formal) | Selected formal specifications: Lean definitions and a hand-maintained Python mirror | README, CONTRIBUTING, and Lean/property-test workflows |
| [vlabs-integrity](https://github.com/verifiablelabs/vlabs-integrity) | Implemented audit tooling: checks against known deviation classes using a trusted reference and input generator | README and CI; read the execution/isolation boundary before custom audits |
| [vlabs-evidence](https://github.com/verifiablelabs/vlabs-evidence) | Evidence collection: historical public-benchmark reports and separately labelled synthetic fixtures | README, `reproducibility-notes.md`, and artifact validator |
| [vlabs-examples](https://github.com/verifiablelabs/vlabs-examples) | Demonstrations: synthetic SDK inputs and dummy-provider examples | README and CONTRIBUTING; check card compatibility against current SDK migration notes |
| [vlabs-demo](https://github.com/verifiablelabs/vlabs-demo) | Demonstration: offline Node mechanism on constructed toy cases | README, `bin/vlabs-demo.js`, and `npm test`; no field detection-rate claim |
| [vlabs-status](https://github.com/verifiablelabs/vlabs-status) | Monitoring configuration: scheduled service probes | README and scheduled workflow; configuration alone establishes neither availability nor an independent database check |

## Archived public predecessor

| Repository | Historical role | Use today |
|---|---|---|
| [verifiable-labs-envs](https://github.com/verifiablelabs/verifiable-labs-envs) | Earlier environment, SDK, and training workspace; GitHub marks it archived | Historical source and provenance. Begin SDK or formal work in the maintained repositories above. |

An archived README can retain older migration instructions. Its text does not
override current repository metadata. Existing dependency pins require review
by their owners before migration; the map does not establish that every legacy
dependency has been replaced.

## Internal ownership

Model research, protected evaluation material, and operational ownership belong
in access-controlled internal documentation. This public map does not enumerate
private repositories, reveal their implementation, or publish internal findings.
Public summaries require review of their evidence and release permission. See
[data boundaries](security-boundary.md) and [contributor workflow](contributor-workflow.md).
