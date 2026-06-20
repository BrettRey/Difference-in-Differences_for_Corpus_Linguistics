**(1) One-Sentence Summary**
Rungs 1-2 are mostly honest as a methods-teaching scaffold, but the simulations currently validate post-stratification under known measured composition, not the central DiD problem of endogenous timing and untreated-potential-outcome parallel trends.

**(2) Are Rungs 1-2 Sound As Drafted?**
**Partly.** Rung 1 is sound as a bounded edited-standard contrast if its premises are stated as premises: France is a usable 1991-1997 counterfactual, Swiss 1991 is not merely a waypoint, interference is limited or estimand-specific, and both untreated `π` trends and bias `b` trends are parallel enough. The draft is admirably honest on these points.

Rung 2 is sound as a cautionary lesson, but not yet as a staggered-identification design. The missing premise is: conditional on observed covariates and calendar time, policy timing is not selected on latent ideology/adoption trajectories. The draft correctly says no estimator fixes selection into timing, but then still leans on policy-time alignment as if it distinguishes policy effects from ideology. It does not: local ideology can cause both adoption timing and usage jumps.

The France-1986 placebo is useful, but narrower than drafted. It tests whether the pipeline finds a jump at a weak/near-null French policy date. It does not validate the not-yet-treated parallel trends assumption for Switzerland, Québec, or Belgium. It also depends on source verification that 1986 and 1998 differ mainly by ideology/implementation rather than measurement, salience, or corpus coverage.

**(3) Simulation Evidence**
The recovery simulation is not rigged in a bad-faith sense, but it is too easy for the identification claim. It proves a post-stratification lemma: if the relevant composition margin is observed, stratum-specific counterfactual trends are common, and treatment timing is exogenous, reweighting removes mix-shift bias. That is worth showing.

But it assumes away the hard DiD problem by construction. In [rung1-recovery-sim.py](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/simulations/rung1-recovery-sim.py:52), all untreated population trends share the same `wave(t)`; the only measured-bias case is a clean observed stratum mix shift; and the unmeasured case is represented as an opaque within-stratum post jump. Good toy, not identification validation.

The ladder simulation is a unit test for the decision rule, not evidence the diagnostics will work in real data. The composition jump, wire bleed, and waypoint are made large and observable enough to route correctly.

**(4) Still Wrong Or Missing**
- The paper needs to split the identifying assumptions: parallel trends in untreated population use `π^0` and parallel trends in measurement/composition bias `b`. “Parallel trends in `b`, not `π`” is an overcorrection.
- Rung 2 needs a selection-into-timing failure mode: no policy effect, adoption dates triggered by latent ideology, event-time estimates show policy-date jumps, and reweighting cannot fix it.
- France 1986 needs a stricter interpretation: negative-control/placebo for one mechanism, not proof of staggered DiD validity. Historical claims around B&B/Fujimura/Dawes/Moreau still need source verification unless already fully checked.

**(5) Single Most Important Fix**
Add a rung-2 simulation arm where policy timing is selected by latent adoption pressure and show that Callaway-Sant’Anna/event-time logic can produce policy-aligned effects with zero causal policy effect. The ladder should route that case to descriptive/not identified unless an explicit exogeneity or sensitivity premise survives.

**(6) Verdict**
**Draft the rest once the central fix is made.**