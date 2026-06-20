1. The plan’s core idea is to make DiD usable for corpus linguistics by translating its identifying assumptions into concrete corpus problems: composition, diffusion, topic shocks, author dependence, and measurement drift.

2. Strengths
- The plan correctly treats DiD as an identification problem, not just a before/after regression template.
- The six core questions are the right spine: treatment, unit, outcome, comparison series, threat, diagnostic.
- The proposed threat list is unusually well matched to corpus data, especially author turnover, register drift, topic shocks, and token dependence.

3. Weaknesses / risks
- The plan still risks assuming shocks are discrete when linguistic change is often gradual, socially stratified, regionally uneven, and lexically uneven. The paper needs a section distinguishing “external event at time T” from “linguistic adoption begins at time T.” Those are not the same premise.
- The worked example is currently the fatal hinge. If the example has pre-existing diffusion, staggered uptake, or endogenous attention/topic change, then the DiD contrast will estimate a mixture of diffusion timing, corpus composition, and treatment response.
- Token dependence cannot be treated as a technical standard-error issue only. Shared authors, threads, events, and topics can define the actual identifying unit. If the design claims token-level evidence while identification lives at author, region, platform, or event level, the estimand is mislabeled.

4. DiD vs multilevel model
A multilevel time-series model is the more natural default for corpus change: it can represent gradual diffusion, author and region structure, lexical heterogeneity, topic shifts, and partial pooling across sparse cells. DiD buys something narrower but valuable: a transparent counterfactual contrast anchored in an external shock and a comparison series, with assumptions that can be stated and attacked. The cost is that DiD can flatten diffusion into a binary before/after timing story and hide heterogeneity unless extended into event-study or heterogeneous-treatment designs. I would frame DiD not as the general model of corpus time series, but as a special design for cases where an external discontinuity plus a credible comparison series makes a causal contrast sharper than a descriptive dynamic model.

5. Single question before drafting
What exact kind of causal estimand is the paper willing to defend: a shock-induced change in corpus frequencies, a change in language use by a population, or an acceleration/redirection of an already ongoing diffusion process?

6. Verdict: Promising but needs reframing.  
The foundation is strong, but the paper must foreground diffusion and heterogeneous adoption as central threats to the DiD timing assumption, not as afterthoughts in diagnostics.