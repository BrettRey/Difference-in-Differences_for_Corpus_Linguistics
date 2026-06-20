1. **One-Sentence Summary**

Rungs 1-2 are directionally sound as a methods scaffold, but the current simulation evidence only validates toy recoverability under near-oracle measurement and still leaves the real measurement problem: hidden editing/composition drift and strategy-invariance.

2. **Are Rungs 1-2 Sound As Drafted?**

**Partly.** What works: the draft keeps the worked example methodological, splits edited-standard from population claims, downgrades the randomization check, and lets diagnostics force “not identified.” That is the right discipline.

The weak point is measurement. The inference is: “a reweighted press DiD can support a bounded policy effect on the edited written standard.” The missing premise is: “conditional on measured margins, the editing operator and strategy mix have no differential post-treatment drift.” That premise is named in the design spec, but not yet operationalized enough in [sections/08-worked-example.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:9).

Partial pooling is still slightly overclaimed at [line 11](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:11): the recovery sim shows no 2x2 variance gain, so rung 1 should not imply it stabilizes the DiD contrast. Defer the payoff to rung 2+ sparse group-time cells.

3. **Does The Simulation Evidence Support The Claims?**

**It supports a narrow pedagogical claim, not a real-corpus recovery claim.** No obvious bug, but the DGP is too easy by design.

In [rung1-recovery-sim.py](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/simulations/rung1-recovery-sim.py:68), measured drift is exactly a shift in an observed A/B stratum, and reweighting uses the correct reference mix. Of course it recovers. That is fine if described as “post-stratification works when the relevant drift is measured,” not as evidence that real editing bias is recoverable.

The unmeasured arm is honest but binary: [line 64](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/simulations/rung1-recovery-sim.py:64) makes unmeasured editing bias numerically identical to a real effect. Good boundary case, but real corpora are partial-proxy cases: noisy observed margins plus residual hidden editing.

The ladder sim is also oracle-like: composition and wire interference are generated as directly observed diagnostics in [rung1-ladder-sim.py](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/simulations/rung1-ladder-sim.py:85). It validates routing logic, not diagnostic power in real corpora.

4. **Still Wrong Or Missing**

- The strategy-agnostic outcome still needs a real measurement-invariance rule. “We test rather than assume” is not enough unless the paper says what form-specific divergence does to the claim.

- The measured/unmeasured split understates the hard part unless a middle case is added: noisy proxies, partially measured composition, and a hidden editing operator with tunable size.

- The simulations do not yet include the promised malign-strategy arm, so they do not test the Dawes-style threat that “any feminine marking” can collapse different social/morphological strategies.

5. **Single Most Important Fix**

Add one measurement-realism simulation and matching prose rule: decompose bias into measured composition, noisy proxy error, hidden editing drift, and strategy-mix drift; then show when reweighting survives and when the ladder demotes the result to descriptive or not identified.

6. **Verdict**

**Draft the rest once the central fix is made.**

Source grounding: I am relying on the project notes here; Burnett & Bonami, Dawes, Moreau, Fujimura, and the modern DiD/text-as-data citations should remain marked for final verification unless already fully read and checked.