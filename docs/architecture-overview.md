# Architecture overview (public)

Verifiable Labs runs an Evaluate / Improve / Gate / Substrate pipeline:

1. **Contract compiler** turns an agent goal into an evaluation contract.
2. **Scenario generator** produces public / hidden / OOD / adversarial
   scenarios (generated after freeze — never reused from training corpora).
3. **Evaluation** runs the agent through a provider abstraction
   (dummy provider in the open SDK; commercial providers server-side).
4. **Contamination firewall** scores data-contamination risk (DCR) and
   enforces split policy; **anti-hack scanning** scores hack risk.
5. **Clean promotion gate** decides ACCEPT / REJECT / LIMITED_ROLLOUT from
   clean VGS, generalization gap, and regression checks.
6. **Assurance card** records the decision; **substrate records** capture
   transfer metrics and failure memory under an explicit data policy.

The open-source surface is the SDK contracts ([vlabs-sdk](https://github.com/verifiablelabs/vlabs-sdk))
and the formal track ([vlabs-formal](https://github.com/verifiablelabs/vlabs-formal)).
Scenario generation, the firewall, anti-hack detection details, and the
platform are private — that separation keeps the feedback clean.

Selected mathematical properties behind the contamination-resistant
promotion gate are machine-verified in Lean 4. A hand-maintained Python mirror
has property tests derived from selected definitions; no mechanized
code-to-proof parity is claimed.
