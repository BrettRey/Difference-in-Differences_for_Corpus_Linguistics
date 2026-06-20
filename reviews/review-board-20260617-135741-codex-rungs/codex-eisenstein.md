**1. One-Sentence Summary**  
Rungs 1-2 are methodologically promising and mostly honest, but the simulations currently validate a clean teaching toy, not the hard corpus-identification problem under diffusion, interference, and messy composition drift.

**2. Are Rungs 1-2 Sound As Drafted?**  
**Partly.** Rung 1 is the stronger draft: it states the edited-standard estimand, refuses a population claim from press data, names composition bias, treats permutation as falsification rather than inference, and carries the onset-vs-acceleration warning into prose.

Rung 2 is directionally right but under-specified. It says “four polities are not four independent experiments,” but it does not fully cash out the SUTVA violation for staggered DiD. Callaway-Sant’Anna-style not-yet-treated controls need potential outcomes for untreated units that are not changed by treated units’ policies, media flows, AFP copy, or Paris norm authority. That missing premise is exactly what the example makes doubtful.

**3. Does The Simulation Evidence Support The Claims?**  
It supports the **decision-ladder logic**, not yet the broader methodological claim.

The ladder sim is useful: each arm routes to the intended verdict, and the malign composition arm usefully shows a spurious DiD about the same size as the benign effect. But the diagnostics are too oracle-like. The composition proxy directly encodes the composition jump, and the interference verdict receives `wire_bleed` as known truth. Real corpora give noisy AFP exposure, outlet dependence, republication, topic mix, and norm-deference proxies, not the spillover parameter.

The recovery sim is fair as a minimal post-stratification demo, but too clean as a stand-in for real corpus drift. It bakes in the condition under which reweighting should work: known stable strata, known reference mix, no measurement error in strata, no treatment-induced margins, and parallel within-stratum trends. The measured/unmeasured distinction is honest, but the inference needs its missing premise named: reweighted DiD identifies the target only if the measured strata exhaust differential composition drift and there is no unmeasured within-stratum differential drift.

The missing interference arm in the recovery sim matters **only if** the paper uses that sim as evidence for the whole rung-1 apparatus. If it is explicitly scoped to “composition recovery conditional on no interference,” it is fine. But as written, the simulation spine still owes an arm where reweighting succeeds on measured composition yet fails because the control is partially treated by diffusion.

Also: the spec says test acceleration, not level shift; both scripts still mostly test level/log-odds jumps plus a pre-slope flag. The prose has the onset-vs-acceleration point; the simulations have not caught up.

**4. Still Wrong Or Missing**

- Rung 2 needs an explicit exposure/interference estimand: direct policy effect net of shared media, total diffusion effect, or exposure-conditioned effect. Without that, “not-yet-treated control” is pretending SUTVA holds where the paper knows it probably does not.

- Composition reweighting needs a mediator/collider warning. Profession mix, female-referent share, and topic mix may themselves be changed by policy or ideology; reweighting them can remove part of the effect, not just remove bias.

- The simulation spine still lacks the hard arms promised by the spec: interference plus reweighting, morphological strategy-mix drift, and an actual acceleration/slope/hazard estimand.

**5. Single Most Important Fix**  
Align the estimand across prose and simulations: define the effect as a policy-timed change in adoption acceleration under an explicit media-exposure/interference mapping, then update the recovery simulation so reweighting is tested both with and without cross-unit exposure.

**6. Verdict**  
**Draft the rest once the central fix is made.**

Citation note: every cited source/date claim should remain verification-marked unless already fully checked, especially Dawes 2003, Moreau 1991, Fujimura 2005, the policy dates, and the modern DiD citations.