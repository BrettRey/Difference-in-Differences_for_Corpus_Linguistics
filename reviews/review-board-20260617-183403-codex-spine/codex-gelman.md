**1. Summary**  
This paper translates DiD from an econometric template into a corpus-design discipline: the target is a latent population usage rate, while observed corpus frequency is a contaminated measurement whose composition and coding process must be part of the identification argument.

**2. Strengths**

- [sections/02-did-estimand.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex) gets the main move right: ATT on latent `pi`, not observed `f`, and the warning against token-count precision is essential.
- [sections/05-identification-threats.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/05-identification-threats.tex) wisely presents the DAG as a threat inventory, not an identification machine. The measurement node and policy-moved composition arm are doing real work.
- [sections/08-worked-example.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex) is unusually honest about failure modes: shared waves, interference, small clusters, hidden composition, and “not identified” are allowed outcomes.

**3. Weaknesses**

- [sections/02-did-estimand.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex) still begins too much in DiD-as-genre: “under a single assumption” is misleading even before the corpus-specific second assumption appears. Say explicitly that DiD is a contrast inside a broader time-series model, not a magic estimator.
- [sections/08-worked-example.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex) needs to justify why France, Québec, Belgium, or trilingual Switzerland actually pin down the counterfactual, rather than merely decorating the design with comparison series. Pre-trend checks are not enough when treatment timing follows the same ideological process that moves usage.
- The “bounded estimate” language in section 08 risks sounding more certain than the design deserves. If the bound is not a formal sensitivity interval including trend, composition, measurement, and few-cluster uncertainty, call it a sensitivity-framed estimate, not something “licensed” by diagnostics.

**4. Key Question**  
Why is DiD the primary design rather than a multilevel model of the entire corpus time series, with latent usage rates, policy events, outlet/title effects, composition, measurement shifts, and smooth calendar-time trends? What does the comparison corpus identify that the model would not otherwise have to assume?

**5. Verdict**  
**Sound-with-revisions**: the design spine is good, but it must stop selling DiD as the organizing technology and present it as one contrast in a larger model-based uncertainty problem.

**Q1. Four-Unit Taxonomy**  
Aggregation should be distinct. Do not fold it into clustering. Clustering is about dependence and uncertainty; aggregation is about the cell at which counts are summed before estimation. Those are different.

A better taxonomy is: linguistic unit, measurement/counting unit, aggregation or analysis cell, identifying unit, clustering/dependence unit. In corpus work, tokens may be counted, title-by-outlet-by-month cells may be modeled, policy may vary by polity, and residual dependence may live at outlet, polity, or time levels. Collapsing aggregation into clustering hides exactly the kind of precision problem the paper is trying to expose.

**Q2. `f = pi + b`**  
Keep it, but state it as a scale-specific decomposition, not a literal homoskedastic error model. If `b` is defined as `f - pi` on the frequency scale, then the linear identity `DiD(f) = DiD(pi) + DiD(b)` is exact. No homoskedasticity is needed for that algebra.

The honest cost is interpretive: proportions are bounded, composition bias can interact with the latent rate, and near 0 or 1 a probability-scale contrast may behave badly. A logit-scale version would be more model-like but less pedagogically clean. I would keep the additive version in section 02, add one sentence saying `b` is the corpus-production gap on the chosen scale, and later recommend binomial/logit or multilevel sensitivity checks.

**Q3. Foundational Citation**  
For this audience, I would use the Roth/Sant’Anna/Bilinski/Poe 2023 review as the single anchor, not Card and Krueger 1994. That recommendation needs verification before use because it is not in `references-local.bib`.

Put it in section 02 after the opening paragraph’s statement of the ATT and parallel trends idea. Card and Krueger is historically iconic, but it anchors the reader in an application genre. This paper needs an estimand-and-assumptions anchor. Bertrand, Duflo, and Mullainathan 2004 is already verified locally and fits the token-precision/inference warning, but it is not the right general foundation for the section.