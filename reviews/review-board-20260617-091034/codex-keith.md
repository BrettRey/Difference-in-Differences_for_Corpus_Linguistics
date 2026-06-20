1. The plan’s core idea is to make DiD usable for corpus linguistics by translating causal assumptions into questions about corpus composition, measurement validity, and counterfactual comparison series.

2. Strengths
- It correctly treats corpus composition as a first-order identification problem, not a nuisance variable.
- The six core questions are strong because they force separation among treatment, unit, outcome, counterfactual, threat, and diagnostic.
- The plan is promisingly non-tutorial: the value is methodological hygiene for causal claims from text, not explaining DiD to linguists.

3. Weaknesses / risks
- The plan must separate outcome text from confounding text. If the same textual stream defines the outcome and encodes the changing population composition, the estimand is not identified without an explicit measurement model or design restriction.
- “Corpus frequency” is not automatically a population quantity. The missing premise is that corpus inclusion, author turnover, register mix, and topic prevalence are either stable, modeled, or irrelevant to the target population.
- The threats section risks reinventing text-as-confounder work. It should explicitly connect corpus composition threats to known results on text as proxy, confounder, and noisy measurement instrument; verify specific citations before drafting.

4. DiD vs multilevel model
DiD buys a design-based counterfactual: it asks whether a comparison series can stand in for the untreated trajectory of the treated corpus after a shock. That is useful when the research question is explicitly about a discrete shock and when there is a defensible untreated comparison. A multilevel time-series model buys partial pooling, richer heterogeneity, smoother temporal structure, author/register/topic variation, and clearer uncertainty about measurement. I would prefer the multilevel model if the “shock” is diffuse, adoption is gradual, or the main problem is estimating latent population language use from a changing corpus. DiD is not wrong, but it is justified only if the paper can name the comparison series and defend parallel counterfactual movement after conditioning on corpus composition. Otherwise DiD becomes a weaker special case of a fuller measurement-and-change model.

5. Single question
What is the exact target quantity: a change in language use in a population, a change in language use among corpus contributors, or a change in the textual composition of the corpus?

6. Verdict
Promising but needs reframing: the foundation is sound only if the paper foregrounds text-as-measurement and corpus-composition confounding before presenting DiD as the design.