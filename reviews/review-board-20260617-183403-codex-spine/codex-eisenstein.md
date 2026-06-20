**Structured Review**

1. **Summary:** The paper translates DiD from a generic policy-evaluation tool into a corpus-linguistic design discipline: observed corpus frequencies are not the estimand, and every causal claim must survive both linguistic diffusion and corpus-construction threats.

2. **Strengths**
- The estimand move is strong: [§02](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:6) cleanly separates latent population rate `pi` from observed frequency `f`, which is exactly the bridge corpus linguists need.
- [§04](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/04-outcomes.tex:5) treats feminization as a bundle of strategies rather than a single surface count. That is sociolinguistically right: adoption can be lexically, morphologically, regionally, and institutionally uneven.
- The worked example’s decision ladder is the right genre for this paper. [§08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:24) makes “descriptive only” and “not identified” legitimate outputs rather than failures to be hidden.

3. **Weaknesses**
- The draft still sometimes talks as if policy is a clean step shock. [§02](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:4) frames DiD as a before/after shock contrast, while [§08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:18) more correctly asks about acceleration and waypoint timing. The treatment section needs to make explicit that the policy date is discrete but the linguistic process is dynamic diffusion.
- The unit taxonomy is almost right but underplays aggregation and dependence. [§02](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:12) says the clustering unit is “here the variety again”; that risks hiding author, outlet, article, wire-copy, topic-burst, and title-level dependence. Those do not create identifying variation, but they do affect measurement uncertainty and false precision.
- Several diagnostics are asserted before they are operationalized: AFP exposure, pre-1991 slope checks, randomization nulls, and “breakdown value larger than any plausible ideology shift” in [§08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:20). Section 06 must turn these into measurable rules, not prose cautions.

4. **Key Question:** What exactly is the diffusion estimand: a policy-date level shift, an acceleration in adoption, a change in adoption hazard for specific titles/forms, or a shift in edited-standard convention?

5. **Verdict On Design:** **Sound-with-revisions**: the spine is solid, but the dynamic diffusion estimand and aggregation/dependence structure need to be made explicit.

**Q1. Four-Unit Taxonomy**

Add aggregation as a distinct fifth unit, or at least a named “analysis cell.” Do not fold it into clustering.

Measurement unit asks what is counted: token, document, title occurrence. Aggregation asks what contributes one observation to the estimator: variety-year, outlet-month, author-period, title-strategy-period. Clustering asks where residual dependence lives. These are different.

For corpus practice, this fifth unit matters because token-level counts can overweight prolific authors, wire stories, repeated topics, or a few high-frequency titles. A good example taxonomy would be:

- linguistic unit: feminine marking of eligible profession/title nouns
- measurement unit: eligible title tokens conditioned on female referent
- aggregation unit: outlet-by-period-by-title/strategy cells
- identifying unit: polity/variety with policy timing
- clustering/dependence unit: variety for identification, plus outlet/author/article/topic structures for uncertainty and diagnostics

The four-way cut is conceptually good, but corpus practice has a real aggregation joint.

**Q2. `f = pi + b`**

Keep `f = pi + b`, but state that it is an identity on the additive frequency scale, not a homoskedastic error model. If `b = f - pi`, then `DiD(f) = DiD(pi) + DiD(b)` follows exactly by linearity.

The honest cost is scale choice. Near 0 or 1, additive contrasts are constrained; on log-odds or ratio scales, the clean decomposition no longer holds in this simple form. But moving to log-odds would obscure the central pedagogical point for a corpus audience.

Best fix: keep the notation in §02, add one sentence saying the decomposition is on the probability/frequency scale, and allow later estimators to use binomial/logit machinery while reporting marginal effects back on the additive scale.

**Q3. Foundational Citation**

For this audience and estimand-first framing, I would use the Roth/Sant’Anna/Bilinski/Poe 2023 review as the single anchor, pending verification and a local bib entry. It belongs in [§02](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:4), right after the first statement of ATT under parallel trends.

I would not use Card & Krueger 1994 as the single anchor here. It is the classic showcase, but it encourages the wrong mental model for this paper: clean policy shock, clean outcome, clean treated/control contrast. If named at all, it needs verification first and should be secondary, probably in the problem/setup section rather than the estimand keystone.