**Jonathan Roth Review**

1. The contribution is a corpus-specific DiD hygiene framework: observed corpus frequency is separated from latent language-use rate, so parallel trends must be defended for both usage and corpus bias.

2. Strengths:
- [§02](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:6) makes the right estimand move: ATT on latent `pi`, not observed `f`.
- [§05](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/05-identification-threats.tex:28) wisely frames the DAG as a threat inventory, not an identification graph.
- [§08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:24) has the right disciplinary instinct: diagnostics must be allowed to downgrade the claim.

3. Weaknesses:
- [§02](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:4) says “under a single assumption” before explaining that the assumption is unobservable. For non-economists, add immediately: pre-trends can falsify some stories, but cannot prove counterfactual parallel trends.
- [§08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:18) and [§08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:26) still risk sounding like “pre-period slopes plus checks license identification.” Recast as: checks can disqualify; bounded estimates require a stated sensitivity restriction.
- [§08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:16) needs an operational rule for which composition margins are safe to reweight. “Not policy-moved” is right, but the paper must say how the analyst decides that before seeing the result.

4. Key question:
What observation would convince you that policy-time alignment is not just an ideology wave selecting treatment timing? If the answer is “flat observed pre-trends,” that is not enough.

5. Verdict on design:
**Sound-with-revisions**: the spine is credible, but only if diagnostics are never treated as proof of parallel trends.

**Q1. Four-Unit Taxonomy**

Add aggregation as a distinct fifth unit, preferably called the **aggregation cell** or **estimation cell**. It is not the same as clustering. Aggregation determines how token counts become observations and weights; clustering determines the dependence structure for uncertainty. Folding aggregation into clustering will confuse exactly the issue corpus readers need help with.

**Q2. `f = pi + b`**

Keep it. If `b` is defined as `f - pi` on the rate scale, the decomposition is exact, not a homoskedastic error model. The honest cost is scale dependence: the clean linear identity holds for rate-scale DiD, not automatically for log-odds or ratios. Add one sentence saying `b` is a reduced-form discrepancy, not a structural additive data-generating model.

**Q3. Foundational Citation**

For this audience, I would cite the Roth/Sant’Anna/Bilinski/Poe 2023 review after verification and keying, near the first paragraph of §02 where the ATT and parallel-trends logic is introduced. Do not use Card and Krueger 1994 as the main anchor here; it is a classic application, but it will not teach this audience the estimand/pre-trends caution the paper depends on. Both candidate cites need verification because neither key is visible in `references-local.bib`.