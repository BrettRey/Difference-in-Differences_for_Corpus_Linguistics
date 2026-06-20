**Process Note**
I did not open review-output files, but `DECISIONS.md` contained prior board summaries because project instructions required reading it. The review below is grounded in the draft text and `references-local.bib`.

**1. Summary**
The paper’s contribution is a useful translation of DiD credibility conditions into corpus-linguistic terms: a corpus frequency is not the target population rate, so parallel trends must be argued for both the latent rate and the corpus filter.

**2. Strengths**
- The paper names parallel trends as the identifying assumption and repeatedly refuses the common mistake that flat pre-trends prove it. See [sections/02-did-estimand.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:8) and [sections/06-diagnostics.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/06-diagnostics.tex:4).
- The `f = pi + b` decomposition is the core insight, and it is well pitched for non-economists: observed corpus trends combine population usage with composition/measurement drift. The five-unit distinction in [sections/02-did-estimand.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:14) is especially strong.
- The worked example is honest about failure modes. Rung 2 correctly says staggered DiD estimators fix weighting, not selection into treatment timing; see [sections/08-worked-example.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:30).

**3. Weaknesses**
- The “parallel trends twice” argument is basically right, but needs a sharper potential-outcomes statement. If the policy changes `b`, that is not merely a second parallel-trends problem; it is a treatment effect on the measurement/composition process. For an effect on `pi`, that must be excluded, modeled separately, or redefined as part of a broader corpus-text estimand. Clarify [sections/02-did-estimand.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:12).
- The diagnostics ladder depends on judgments that are not yet operational enough: “plausible confound,” “breakdown value beyond any plausible drift,” and “pre-committed non-policy margins” need concrete calibration rules. Otherwise the ladder in [sections/06-diagnostics.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/06-diagnostics.tex:18) risks becoming principled language without reproducible decision rules.
- The inference section is directionally correct but slightly overconfident about remedies. Wild cluster bootstrap and randomization inference are not generic fixes for four or five politically selected clusters; RI requires an assignment model, and WCB can still be fragile. Temper [sections/07-modern-did-choices.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/07-modern-did-choices.tex:10).

Source-grounding flags: `weinreich1968` and `tagliamontedarcy2007` are cited but not in `references-local.bib`; under your rule, they need verification. The simulation claims in [sections/08-worked-example.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:42) also need enough DGP detail to be auditable.

**4. Single Most Important Question**
When observed pre-period trends in corpus frequency `f` look parallel, what evidence would convince you that the unobserved counterfactual trends in both `pi` and `b` are parallel separately, rather than offsetting each other?

**5. Verdict**
Major revisions. The design is promising and unusually honest, but the estimand under policy-induced corpus-filter changes and the operational calibration of diagnostics need tightening before the paper is sound as a methods contribution.