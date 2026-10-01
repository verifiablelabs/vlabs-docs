# Positioning

**Primary sentence.** Enthym develops AI learning methods, starting with coding
and using verification to study the quality of feedback.

**Research direction.** Increasingly general models that learn reliably from
experience. World models and AGI are future research goals, not achieved
capabilities. Verification and evaluation support that program.

## Brand and technical identity

Use **Enthym** for the startup in current prose. Explain once, where useful,
that public work is hosted by the existing `verifiablelabs` organization and
retains Verifiable Labs technical identifiers. Preserve repository URLs,
package names, imports, CLI names, historical citations, and license attribution.
Brand wording is not an instruction to rename or republish anything.

## Describe status precisely

| Evidence or status | Appropriate language |
|---|---|
| Implemented public code | Name the interface or tool and link its source; describe constraints |
| Synthetic demonstration | Label it illustrative; state the mechanism or format demonstrated |
| Historical measured report | Name the dataset, endpoint, revision limits, and original interpretation |
| Planned research | Use “we intend to study” or “research goal” without a capability headline |
| Service or package availability | Verify the actual release or deployment separately from source code |

The [research overview](product-overview.md) separates these categories. Model
capability claims need an approved, inspectable evidence package; a verifier
result or synthetic card is not a model benchmark.

## Claim boundaries

We do not claim achieved AGI, unbounded self-improvement, demonstrated
frontier-model capability, or equivalence to OpenAI or Anthropic.
We do not claim independent certification or a compliance audit from a tool
report, assurance-card name, checksum, or selected theorem.
We do not claim that filtering eliminates contamination.
We do not claim a formally verified system, product, API, or training algorithm.

The formal scope is:

> Selected mathematical properties behind the contamination-resistant
> promotion gate are machine-verified in Lean 4. A hand-maintained Python
> mirror has property tests derived from selected definitions; no mechanized
> code-to-proof parity is claimed.

State assumptions alongside a theorem. Passing a defined gate does not prove
a model's generalization, population performance, or service security.
