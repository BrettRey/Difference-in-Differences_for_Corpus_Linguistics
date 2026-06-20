1. The plan’s core idea is to make DiD usable for corpus linguistics by translating the parallel-trends design from an econometric slogan into concrete corpus questions about shocks, comparison series, measurement, and composition.

2. Strengths

- The plan correctly frames DiD as an identification design, not merely as a before/after regression with controls. The six core questions are the right discipline: treatment, unit, outcome, counterfactual comparison, threat, diagnostic.
- The corpus-specific threat list is exactly where this paper can contribute: register drift, author turnover, topic shocks, and measurement drift are not nuisances after identification; they are direct threats to parallel trends.
- Separating “estimand,” “identification threats,” and “diagnostics” is promising because corpus readers need to see that pre-trend plots are evidence, not proof.

3. Weaknesses / risks

- The plan needs to say, early and repeatedly, that parallel trends is the identifying assumption: absent the shock, treated and comparison corpus outcomes would have changed similarly. If this is softened into “the pre-period lines look similar,” the paper will teach the wrong lesson.
- Pre-trend diagnostics are especially treacherous here. In corpora, pre-period composition can drift while the measured frequency remains parallel, so flat pre-trends can mask offsetting changes in authors, topics, registers, or platforms. The diagnostic section should explicitly distinguish testing observed pre-period outcome equality from defending the unobserved post-period counterfactual.
- The outline risks making diagnostics sound like a checklist. For each diagnostic, the paper should say what identifying threat it can expose and what it cannot. A placebo outcome, balance plot, event-study pre-period coefficient, or composition decomposition is not a validation of parallel trends; it is a stress test of one failure mode.

4. DiD vs. multilevel model

DiD buys a clear counterfactual contrast: a treated corpus series is interpreted relative to a comparison series under a named parallel-trends assumption, yielding a design-based estimand rather than just a fitted temporal pattern. A multilevel model of the whole corpus time series buys richer structure: author/register/topic hierarchies, partial pooling, nonlinear trajectories, measurement error, and heterogeneous diffusion. But without a credible untreated comparison path, that model mostly gives disciplined smoothing or forecasting, not causal identification. The best framing is not “DiD instead of multilevel modeling,” but “DiD supplies the identifying comparison; multilevel modeling may be needed to measure the corpus outcome and account for hierarchy before or within that design.” DiD is the right tool only when the comparison series makes the untreated counterfactual plausible; otherwise it is a weaker special case of descriptive time-series modeling with causal language attached.

5. The single question I would most want answered before drafting begins

What exact corpus comparison makes the untreated counterfactual credible, and why should its post-shock change represent what would have happened to the treated corpus outcome absent the shock despite composition drift?

6. Verdict

Promising but needs reframing: the foundation is sound only if the paper makes parallel trends the explicit burden of proof and treats pre-trends as limited diagnostics, not as evidence that the assumption “holds.”