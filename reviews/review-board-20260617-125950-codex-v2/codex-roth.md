**Jonathan Roth Review**

1. **One-Sentence Summary**  
v2 uses feminization of profession nouns as a progressive DiD teaching sequence: Swiss French vs France as the clean two-group baseline, then staggered francophone varieties, then trilingual Switzerland, with each rung exposing a different identification, interference, measurement, or inference problem.

2. **Does v2 Resolve the Round-3 Concern?**  
**Partly.** v2 gets the main move right: it stops pretending the ideology wave is a nuisance you can wish away and instead asks whether policy-time divergence remains after calendar-time movement is accounted for. That is the right teaching frame.

But it does **not** fully identify the policy effect. The missing premise is: absent the Swiss policy, Suisse romande would have followed France through the shared ideology wave after composition adjustment, and shared-media channels would not transmit treatment-relevant shocks across units. With AFP/shared francophone media in play, the policy-time vs calendar-time contrast is a diagnostic, not by itself an identified test.

Rambachan-Roth in breakdown mode is the honest response. It also concedes the important point: if a discrete ideology shock can arrive at the treatment date with no pre-period footprint, the data do not point-identify the policy effect. Breakdown analysis tells the reader how large that violation must be to overturn the result; if that size is plausible, the correct conclusion is “unidentified,” not “robust.”

3. **Still Wrong or Underspecified**

- **Wave-as-parallel-trend needs an explicit premise.** Committing to the policy date makes the estimand legible: policy effect over and above the shared wave. It does not make the wave a valid parallel trend. The missing premise is equal untreated exposure to the ideology wave across Suisse romande and France.

- **Interference estimand is not defined.** If shared media transmits norms across the Swiss-France boundary, what is the target: direct Swiss policy effect excluding shared media, or total effect including diffusion? The AFP diagnostic in [DESIGN-SPEC.md](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/DESIGN-SPEC.md:139) is useful, but the design needs a decision rule for when interference downgrades the claim to “not identified.”

- **The randomization null is overclaimed.** With one treated variety and one control, label permutation has essentially no design-based inferential content unless the assignment mechanism is credible. Shuffling dates is a placebo/pipeline check, not “the right inference.” The sentence in [sections/08-worked-example.tex](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:19) should be softened sharply.

4. **Is Rung 1 Sound as Drafted?**  
**Almost, but not as drafted.** It is a good teaching baseline because it states treatment/control, separates edited-standard from population use, names composition bias, and foregrounds interference. The problem is that [section 08](/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Difference-in-Differences_for_Corpus_Linguistics/sections/08-worked-example.tex:15) makes the policy-time contrast sound more identified than it is, and line 19 turns a useful null diagnostic into inferential machinery it cannot support with two units.

5. **Single Most Important Fix**  
Rewrite rung 1 around an explicit decision rule:

- policy-time divergence survives composition and shared-media diagnostics, and breakdown values exceed plausible ideology shocks: bounded policy-time evidence;
- calendar-time co-movement dominates: shared wave, not policy;
- interference/composition diagnostics fail, or plausible Rambachan-Roth violations overturn the estimate: effect not identified.

6. **Verdict**  
**Draft once the central fix is made.** v2 is now a strong methods-teaching design, but rung 1 must not teach that two-unit permutation plus breakdown sensitivity identifies what the design itself says may be unidentified.

Verification flag: before drafting the methods claims, verify the exact Rambachan-Roth sensitivity classes and the cited BDM/randomization-inference implications.