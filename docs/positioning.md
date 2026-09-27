# Positioning

**Primary sentence.** Verifiable Labs is an AI model company working toward
increasingly general, self-improving intelligence.

**Category.** Commercial AI model research and development. Our current
starting point is verifier-guided post-training of coding models. Evaluation,
formal specifications, and agent infrastructure support that model program.

**Research thesis.** Feedback that distinguishes useful solutions from
reward shortcuts may produce better training data and more reliable learned
capabilities. We test that thesis by changing model parameters and comparing
performance, transfer, and failures under stated evaluation conditions.

## Present work and future direction

| Status | How we describe it |
|---|---|
| Implemented | Filtered supervised fine-tuning with QLoRA adapters on existing open-weight coding models; verification and evaluation tooling |
| Active research | Learning agents, curriculum control, persistent experience, model adaptation, and transfer between coding task families |
| Planned | World-model research: learning environment dynamics and using them for planning beyond coding |
| Long-term goal | Increasingly general models and AGI; this is research ambition, not an achieved capability |

Our present training runs adapt other developers' pretrained models. They do
not establish a new pretrained foundation model. Current learning cycles
refit fresh adapters from the base model using accumulated experience; they
should not be described as continuously updating the same weights.

The [research overview](product-overview.md) is the source for current
claims and evidence. A result in one coding family is not a general-purpose
capability claim. Product availability must be described separately from
implemented research or service code.

## Claim boundaries

We do not claim achieved AGI, guaranteed general intelligence, unbounded
self-improvement, or demonstrated frontier-model capability.
We do not claim that filtering eliminates contamination.
Generated tasks may resemble a model's unknown pretraining data.
We do not claim a formally verified system, product, API, or training algorithm.

The formal scope is:

> Selected mathematical properties behind the contamination-resistant
> promotion gate are machine-verified in Lean 4. A hand-maintained Python
> mirror has property tests derived from selected definitions; no mechanized
> code-to-proof parity is claimed.

Keep the assumptions adjacent to any stronger discussion of a theorem.
Acceptance by a defined gate does not prove that training will find a better
checkpoint, that a sample estimate equals population performance, or that a
model has general intelligence.
