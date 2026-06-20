1. **One-sentence summary:** Rungs 1-2 now have a teachable spine: start with the clean 2x2 counterfactual, then show why staggered scaling adds estimators faster than it adds identification.

2. **Are rungs 1-2 sound as drafted?** **Partly.** Rung 1 is basically sound and honest: treatment, comparison, estimand, composition threat, interference, placebo logic, and claim ladder are all visible. Rung 2 is pedagogically strong but not yet fully identified: it says treatment timing is selected on the same ideology that moves usage, then still leaves a bounded-estimate branch open. The missing premise is: after measured composition, shared media exposure, form-strategy differences, and a bounded ideology wave, policy timing is still plausibly orthogonal to untreated usage trajectories. If that premise cannot be defended, rung 2 should be framed as a controlled demonstration of why staggered DiD often downgrades claims, not as a route to a clean estimate.

3. **Simulation evidence:** Not buggy, but too easy if described as validation. The ladder sim is a unit test: the DGP creates a composition jump and hands the ladder an almost perfect composition proxy; interference is passed in as `wire_bleed`; waypoint drift is large and direct. That is fine for showing the ladder routes canonical cases, but it does not show the procedure will diagnose hard empirical cases. The recovery sim is a fair existence proof for measured stratum-mix drift: if the relevant composition margin is exactly observed and the target mix is known, reweighting recovers the target by construction. The unmeasured-drift arm is honest and important: it names the non-identification problem. But the toy assumes away the hardest part, which is whether the observed strata actually span the corpus-generating bias term `b`.

4. **Still wrong or missing:**
- The rung-2 ladder is not instantiated enough. “Staggered diagnostics slotted in” needs an explicit mapping from each failed diagnostic to bounded estimate / descriptive wave / not identified.
- The simulations need ambiguous and mixed cases: noisy composition proxies, partial observability, strategy-mix drift, gradual onset, treatment-effect heterogeneity, and false-positive/false-negative rates under realistic sample sizes.
- The partial-pooling prose overclaims for rung 1. The recovery sim correctly finds no 2x2 variance payoff; defer the payoff to rung 2+ or show it in a sparse group-time-cell simulation.

5. **Single most important fix:** Build one decision-ladder table for rungs 1 and 2 that names, for each possible claim, the exact inference, the required missing premise, the diagnostic evidence that would support it, and the downgrade when that premise fails.

6. **Verdict:** **Draft the rest once the central fix is made.**

Citation note: all empirical source claims and method citations should still be treated as needing final verification unless already checked against the actual sources.