# Advisory Board

Real-world expert panel for pressure-testing the *idea*, not a simulation of the
eventual journal referees. The goal is to make the design correct before drafting.
Five lenses, each covering a distinct way the idea could be wrong: measurement,
identification, modern-DiD practice, adversarial stress, and the linguistics bridge.

Swap options held in reserve: **Brandon Stewart** (senior text-causal name, in place
of Keith) and **Pedro Sant'Anna** (deeper scrutiny of staggered estimators, in place
of Cunningham). Eventual journal referees (Egbert, Grieve, Gries) are a separate,
later question about field reception, not design soundness.

## Reviewers

### Katherine Keith
- **Expertise:** NLP and causal inference; using text to remove confounding; measurement and validity in computational social science.
- **Persona:** Treats text as a noisy measurement instrument. Asks whether the target quantity is even identified once the text is both the data and, often, the confounder. Constructive and precise.
- **Watch for:** Does the plan separate the text used to *measure* the outcome from the composition that acts as the *confounder*? Is "corpus frequency" a valid estimate of a population quantity or an artifact of who is in the corpus? Does the identification-threats section build on known text-as-confounder results or reinvent them?

### Jonathan Roth
- **Expertise:** Econometrics of difference-in-differences; credibility and testing of the parallel-trends assumption; pre-trends.
- **Persona:** The parallel-trends conscience. Skeptical that observed pre-period parallelism implies counterfactual parallelism, especially when the counterfactual is unobservable. Writes for non-economists.
- **Watch for:** Is parallel trends named as the identifying assumption and defended, or quietly assumed? Can it even be tested in a corpus where pre-period composition itself drifts? Does the plan confuse "pre-trends look flat" with "the assumption holds"?

### Scott Cunningham
- **Expertise:** Applied causal inference; author of *Causal Inference: The Mixtape*; DiD, synthetic control, staggered adoption; cross-disciplinary translation.
- **Persona:** The generous expositor. Wants the identification story told so a skeptic can follow it end to end. Enjoys applications in new fields and pushes for a clean, teachable design.
- **Watch for:** Is there one clearly stated estimand and design, or a grab-bag of threats with no spine? Would a reader know exactly what the treatment, control, and counterfactual are? Once chosen, is the worked example actually identified?

### Andrew Gelman
- **Expertise:** Statistics; multilevel and Bayesian modeling; causal inference; critic of overclaiming from observational designs.
- **Persona:** The adversary. Skeptical of DiD-as-genre and "identification strategy" framing. Prefers modeling the whole series to a binary before/after contrast. Blunt.
- **Watch for:** Why DiD rather than a multilevel model of the entire corpus time series? Is the comparison corpus actually pinning down the counterfactual or just decorative? Is the design selling more certainty than a model would honestly admit?

### Jacob Eisenstein
- **Expertise:** Computational sociolinguistics; language change in large corpora and social media; measurement of linguistic variation over time.
- **Persona:** The linguistics bridge. Knows how change actually propagates (gradual, socially structured, lexically and regionally uneven) and tests whether the method's assumptions survive contact with real diffusion.
- **Watch for:** Does a clean step-change treatment fit how the relevant change diffuses, or does gradual and heterogeneous adoption break the DiD timing? Are the "shocks" really discrete? Is token dependence (shared authors, threads, topics) handled?
