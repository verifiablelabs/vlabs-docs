# The public/private boundary

Clean feedback only stays clean if evaluation content cannot leak into
training data or public corpora. The boundary is enforced as policy and
code, not convention:

**Public** (Apache-2.0, on GitHub): the SDK contracts, environments, the
Lean 4 formal track and its property-tested Python mirror, the
`clean-gate` CLI, examples with synthetic data, redacted evidence.

**Private, never published**: hidden evaluation content and gold answers,
anti-hack detection details and traps, private verifier logic, the
contamination registry, raw and customer traces, secrets.

Operationally: exports are dry-run by default and pass a public-export
policy check (classification-aware) before anything leaves the boundary;
remote actions require explicit per-service approval flags; uploads are
scanned and redacted; audit events record every gate decision and export.

Selected mathematical properties behind the contamination-resistant promotion gate are machine-verified in Lean 4. The implementation is property-tested against the formal specification.
