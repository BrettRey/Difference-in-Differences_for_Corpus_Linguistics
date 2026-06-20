**1. Summary**  
The paper’s contribution is to translate DiD from “compare treated and control trends” into a corpus-design problem where the target is a latent population rate, observed frequency is contaminated by corpus construction, and identification depends on both the linguistic counterfactual and the corpus-production counterfactual.

**2. Strengths**

- The estimand spine is clear and teachable: Section 02 separates the target rate `pi` from observed corpus frequency `f` and makes the key move that DiD on `f` identifies DiD on `pi` only if the bias term also trends in parallel.
- The four-unit taxonomy in [sections/02-did-estimand.tex:12](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:12) is exactly the right kind of hygiene for corpus readers. It prevents “millions of tokens” from being mistaken for “many treated units.”
- The worked example has a real design logic rather than a methods grab bag. The rung structure and decision ladder in [sections/08-worked-example.tex:24](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:24) make clear when the design earns only a bounded claim, a descriptive claim, a shared-wave claim, or no identified claim.

**3. Weaknesses**

- The treatment in rung 1 still needs one sharper sentence. In [sections/08-worked-example.tex:8](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:8), “1991 Swiss endorsement versus near-null 1986 France” is plausible, but the exact treatment is doing too much: official endorsement, enforcement, media uptake, and ideological timing are all nearby. Section 03 needs to define the treatment as the policy event whose ATT is being estimated, and Section 08 should restate the rung-1 estimand in one sentence.
- Section 02 slightly overpromises what diagnostics can do. [sections/02-did-estimand.tex:14](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:14) says diagnostics are “how that price is checked.” I would soften that: diagnostics discipline, bound, and falsify parts of the assumption; they do not verify parallel trends in either `pi` or `b`.
- The simulation claims in [sections/08-worked-example.tex:49](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:49) are strong enough that they need a visible design skeleton. “False-positive rate climbs past half” and “missed more than nine times in ten” are useful, but the reader needs the data-generating process, parameters, and verdict rule before those numbers can carry weight.

**4. Key Question**

What is the one worked-example estimand: the effect of Swiss policy on edited written usage in Suisse romande from 1991-1997, net of francophone diffusion and transcription change, or a broader effect of policy endorsement on public-language norms? The design becomes much cleaner once that sentence is fixed.

**5. Design Verdict**

Sound-with-revisions: the design spine is strong, but the treatment/counterfactual sentence and the diagnostic-versus-assumption language need tightening before the worked example is fully identified.

**Q1. Four-Unit Taxonomy**

Do not fold aggregation into clustering. They are different design objects.

Clustering is about dependence and standard errors. Aggregation is about the level at which tokens become an outcome: token, document, outlet-month, title-variety-year, polity-period, and so on. That choice changes weights, denominators, sparse-cell behavior, and sometimes the estimand itself.

I would keep the four-way taxonomy because it carves the conceptual joints well, but add an explicit fifth row called “aggregation cell” or “analysis cell.” I would not call it merely clustering. Corpus readers need to see that “we count tokens,” “we estimate outlet-month rates,” and “we cluster by polity” are three different statements.

**Q2. `f = pi + b`**

Keep `f = pi + b`.

The honest defense is that this is an accounting identity on the rate scale: define `b = f - pi`. It is not claiming homoskedastic additive error, normality, or unconstrained outcomes. It says the observed corpus rate differs from the target population rate by a residual wedge made of composition and measurement.

The cost is that the estimand is explicitly on the level/proportion scale. If the real scientific claim is about odds ratios or relative changes, then the linear decomposition no longer carries over cleanly. But for a DiD exposition aimed at corpus linguists, the additive version is the right pedagogical move because it makes the central point exact: `DiD(f) = DiD(pi) + DiD(b)` by linearity.

Add one sentence: “Here `b` is not a classical error term; it is the difference between the corpus rate and the target rate on the same probability scale.”

**Q3. Foundational Citation**

For this paper, I would use the Roth, Sant’Anna, Bilinski, and Poe 2023 review as the single Section 02 anchor, placed after the ATT/parallel-trends sentence in [sections/02-did-estimand.tex:4](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:4).

Reason: the paper is estimand-first and modern-design-aware. Card and Krueger 1994 is a wonderful teaching example, but it would pull the reader toward “classic applied labor example” rather than “here is the identifying structure.” The review gives non-econometrician readers a doorway into the current DiD literature without making the paper a tutorial.

Source-grounding flag: that review is not in `references-local.bib`, so the exact key, title, venue, and metadata need verification before use.