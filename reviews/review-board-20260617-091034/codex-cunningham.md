1. The plan’s core idea is to make DiD usable for corpus linguists by forcing every claimed “language changed after shock X” result through a clear treatment-control-counterfactual design.

2. Strengths

- The six core questions are exactly the right spine: treatment, identifying variation, outcome, comparison series, threat, diagnostic. If the paper keeps returning to those, it can avoid becoming a generic DiD tutorial.
- The corpus-specific threats are real identification threats, not just nuisance issues: author turnover, register drift, topic shocks, and measurement drift can all create fake treatment effects.
- The proposed structure wisely separates estimand, treatments, outcomes, threats, diagnostics, and modern DiD complications; that could teach non-econometricians the design logic without drowning them in estimator taxonomy.

3. Weaknesses / risks

- The plan does not yet name one estimand tightly enough. “Linguistic change after shocks” is too broad. The paper needs a canonical estimand such as: the average effect of a shock on a defined corpus outcome for exposed corpus units, relative to their untreated counterfactual trend.
- The worked example is currently a fatal missing premise. Until it exists, we cannot tell whether the paper is about an identified DiD design or a checklist for why corpus DiD is hard.
- Section 07 should not become a modern-DiD survey. For this audience, staggered adoption and heterogeneity-robust estimators should enter only after the paper has taught the simple two-group/two-period logic and shown how corpus composition can break it.

4. DiD vs. multilevel model

DiD is worth using when the paper can defend a comparison series as the untreated counterfactual for the treated series. What DiD buys is not flexibility; it buys a teachable identification claim: absent the shock, treated and control corpus outcomes would have moved in parallel after accounting for the design. A multilevel time-series model can use more data, represent author/register/topic heterogeneity, and model gradual diffusion better, but it does not by itself identify the causal effect of the shock. It replaces the DiD counterfactual assumption with model-based assumptions about trends, pooling, and functional form. If the worked example lacks a credible control series, I would prefer a hierarchical interrupted time-series or synthetic-control style design. But if the comparison is credible, DiD is the cleaner pedagogical tool because it makes the counterfactual premise visible.

5. Single question before drafting

What is the worked example, stated as treatment, treated units, control units, time window, corpus outcome, and the reason the control series approximates the treated series’ untreated counterfactual?

6. Verdict

Promising but needs reframing: the foundation is strong, but the paper must be organized around one identified design rather than a catalogue of corpus-specific threats.