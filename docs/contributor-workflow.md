# Contributor workflow

## Choose the owning repository

Use the [public map](repository-map.md), then read the target README,
CONTRIBUTING file, applicable agent instructions, and actual workflow definitions.
Follow local guidance before shared organization defaults. Check the branch and
working-tree status so changes stay separate from another contributor's work.

Documentation checks, SDK package tests, Lean proofs, artifact validation, and
Node demo tests verify different surfaces. Follow the target repository's
current commands and dependency pins; use no generic organization-wide test
command in place of those instructions.

## Prepare evidence for review

Keep a change focused and identify the issue it addresses. Include exact
commands, runtime, and outcomes for checks performed, with reasons for skipped
checks. A defined workflow is not a passing run; saved-record analysis is not a
new experiment; a code change is not a deployment.

For a scientific statement, link approved public evidence and preserve the
protocol, endpoint, denominators, uncertainty, and limitations. Label synthetic
fixtures, historical measurements, and future plans distinctly. Describe a
negative or inconclusive result with the same care as a favorable result.

## Review and release

The reviewer should verify ownership, behavior or claim scope, validation, data
disclosure, and the diff itself. Model execution, external uploads, deployment,
and repository-settings changes require their own authorized scope and resource
budget. Keep publication review separate from a local test result.

Use public issues for public bugs and proposals. Use the repository's private
security route for vulnerabilities or accidental disclosures. Keep private
repository details and internal findings in access-controlled records. See
[data boundaries](security-boundary.md) and
[publication workflow](operating-model-github-hf-wandb.md).
