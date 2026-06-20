**1. Summary**

The paper’s contribution is a teachable corpus-linguistic translation of DiD: observed corpus frequency equals latent usage plus corpus filter, so identification requires a named treatment, a plausible comparison, and parallel-trends discipline in both usage and composition/measurement.

**2. Strengths**

- The paper has a real spine, not a threat grab-bag. The `f = pi + b` move and “parallel trends twice” framing give corpus readers a memorable identification discipline ([section 2](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:8)).
- The treatment discussion is unusually good for cross-disciplinary DiD. It makes timing, force, implementation, and leakage part of the estimand rather than background history ([section 3](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/03-treatments.tex:8)).
- The staggered-adoption material lands because it is not magic-method decoration: the draft clearly says modern estimators fix weighting, not endogenous timing ([section 7](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/07-modern-did-choices.tex:6); [section 8](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:34)).

**3. Weaknesses**

- The estimand still needs one final lock. Section 2 says the target is the effect on `pi`, but also says a policy-induced shift in the corpus filter is “part of what the policy did” ([section 2](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:12)). If the estimand is population usage, `T -> C -> f` is not part of that estimand; it is a different textual-output estimand. Add a compact estimand ledger for each rung: target, treatment, control, time window, outcome, identifying unit, clustering unit, direct/total effect.
- The worked example is honest, but rung 3 is not yet as executable as rungs 1-2. Trilingual Switzerland is potentially the cleanest design choice, but it currently stops at the measurement threat rather than applying the ladder with treatment/control/counterfactual spelled out ([section 8](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:52)). Either complete it as a full rung or label it an extension.
- The simulation subsection makes quantitative claims without enough design documentation for a reader to audit them: `+0.13`, false positives past half, missed effects above nine in ten ([section 8](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:44)). Add a table or appendix giving DGP, sample structure, threat varied, estimand, ladder verdict, and failure rate.

**Source-Grounding Flags**

All cited keys appear in `references-local.bib` except `weinreich1968` and `tagliamontedarcy2007` in [section 1](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/01-problem.tex:4). The `Bulletin officiel` coverage claim also needs a verified local citation if retained ([section 8](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:52)).

**4. Most Important Question**

What is the strongest causal claim the author wants the reader to retain: an ATT on the edited written standard, or an effect on population language use? State that once, then let every rung either earn it or demote it.

**5. Verdict**

Major revisions. The architecture is strong and teachable, but the worked example and estimand ledger need tightening before the design can be followed end to end by a non-econometrician corpus reader.