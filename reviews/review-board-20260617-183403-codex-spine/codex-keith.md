I read the requested draft files and treated only `references-local.bib` as verified. No edits made.

**Structured Review**

1. **Contribution:** The paper translates DiD from “before/after corpus contrast” into an estimand-and-measurement problem: the target is a latent population rate `pi`, while observed corpus frequency `f` is filtered through composition and measurement.

2. **Strengths:**
- The estimand spine in [sections/02-did-estimand.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:6) is strong: `f = pi + b` makes clear that corpus frequency is not automatically the population quantity.
- The DAG/threat inventory in [sections/05-identification-threats.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/05-identification-threats.tex:28) correctly separates population rate, composition, and coding/transcription, and it avoids pretending the graph identifies the effect.
- The worked example’s decision ladder in [sections/08-worked-example.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:24) is exactly the right discipline: bounded estimate, descriptive only, shared wave, or not identified.

3. **Weaknesses:**
- The target population for `pi` needs to be fixed earlier. [Section 02](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:6) says “community uses the form,” while [Section 08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:14) narrows the estimand to edited written standard. That is not just wording: it changes whether corpus composition is nuisance bias or part of the target population.
- The example still risks mixing text used to measure the outcome with text that indexes composition/confounding. In [Section 08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:10), “Madame” is treated as an independent cue for female reference, but honorific usage may itself vary by register, outlet, period, and policy ideology. Add a validation step or a role table: outcome cue, denominator cue, composition variable, mediator, confounder.
- The threats section should explicitly connect to text-as-confounder / text-as-proxy work rather than reinventing it. Possible anchors from my lane include Keith/Jensen/O’Connor-style causal text framing and Veitch/Sridhar/Blei-style text adjustment work, but these are **not in `references-local.bib` and need verification before use**.

4. **Key Question:** For each rung, what is the exact population generating `pi`, and which textual features are allowed to define the outcome versus adjust for composition without conditioning on mediators or measurement artifacts?

5. **Design Verdict:** **Sound-with-revisions**: the spine is sound, but the text-as-measurement/text-as-confounder boundary needs to be made operational.

**Q1. Four-Unit Taxonomy**

Carry aggregation as a distinct design choice, and probably as a fifth “unit” if the taxonomy is meant to prevent common corpus mistakes. Aggregation is not clustering. Aggregation is where counts are summed before estimation: token, document, outlet-month, title-variety-year, polity-year. Clustering is where residual dependence is handled for uncertainty.

This matters because aggregation changes the estimand and the weighting. A token-level proportion, a document-level average, and a title-month cell estimate different quantities even before standard errors enter. My recommendation: keep the four-way taxonomy, but add “aggregation unit” as a fifth row in the design table. Do not fold it into clustering.

**Q2. `f = pi + b`**

Keep `f = pi + b`, but define it as a bias decomposition on the frequency scale, not as a homoskedastic additive error model. If `b := f - pi`, the linear claim `DiD(f) = DiD(pi) + DiD(b)` is exact on that scale. The approximation enters only when readers infer that `b` behaves like independent noise or that the same conclusion would hold on a log-odds/ratio scale.

The honest cost: the assumption is scale-dependent, bounded outcomes constrain possible `b`, and near 0 or 1 the additive presentation can hide meaningful asymmetries. But moving to log-odds would obscure the paper’s core pedagogical point for this audience. I would add one sentence: “This is a decomposition on the frequency scale, not a claim that corpus bias is classical additive error.”

**Q3. Foundational Citation**

For this paper, I would cite the Roth/Sant’Anna/Bilinski/Poe 2023 review as the single foundational DiD anchor, **pending verification and exact BibTeX details**. Put it in [Section 02](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/02-did-estimand.tex:4), where ATT and parallel trends are first introduced.

I would not use Card & Krueger 1994 as the sole anchor here. It is historically iconic, but it would make the paper look example-led. The review better supports the estimand-first, assumptions-first framing for non-econometricians.