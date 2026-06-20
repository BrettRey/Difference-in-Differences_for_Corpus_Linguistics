#!/usr/bin/env python3
"""
Rung-1 recovery simulation: does reweighting RECOVER the truth (not just flag the artifact),
and does partial pooling buy variance on the small variety?

Companion to rung1-ladder-sim.py (which validated detection/routing). Here the data-generating
process is stratified, so composition can drift as a shift in the MIX of an observable stratum,
which is exactly what post-stratification (reweighting) is built to undo. We control truth, so
for each arm we know the target DiD and can ask whether each estimator hits it.

Three arms:
  benign             a real population effect, no composition drift          -> all estimators recover
  malign_rate        NO real effect; the observable stratum mix drifts on CH -> naive biased, reweighting recovers
  malign_unmeasured  NO real effect; an UNOBSERVED within-stratum bias on CH -> naive AND reweighted both fail

The third arm is the honest limit: unmeasured differential drift is observationally identical to
a real effect, so reweighting cannot touch it. That is the residual assumption Section 2 declares
("no unmeasured differential drift"), shown here as a case the method is fooled by, not one it
can diagnose.

Pure standard library; deterministic.
"""
import math
import random
import statistics

YEARS = list(range(1985, 2006))
T0 = 1991
PRE = [y for y in YEARS if 1985 <= y <= 1990]
POST = [y for y in YEARS if 1991 <= y <= 1997]
STRATA = ["A", "B"]
BASE = {"A": 0.6, "B": -1.6}        # high- vs low-feminization stratum offsets (log-odds)
REF_MIX = {"A": 0.5, "B": 0.5}      # fixed reference composition for post-stratification
N = {"CH": {"A": 150, "B": 150}, "FR": {"A": 3000, "B": 3000}}   # CH small, FR large
REAL = 0.8                           # true policy effect (log-odds) when an arm has one
TOL = 0.02


def logistic(x):
    return 1.0 / (1.0 + math.exp(-x))


def wave(t):
    return -2.0 + 0.18 * (t - 1985)   # common continental trend, differenced out


def sample_prop(p, n):
    sd = math.sqrt(max(n * p * (1 - p), 1e-9))
    return min(max(p * n + random.gauss(0, sd), 0.0), float(n)) / n


def true_rate(var, t, s, arm):
    lo = wave(t) + BASE[s]
    if var == "CH" and t >= T0 and arm == "benign":   # only benign carries a real population effect
        lo += REAL
    return logistic(lo)


def obs_rate(var, t, s, arm):
    lo = wave(t) + BASE[s]
    if var == "CH" and t >= T0 and arm == "benign":
        lo += REAL
    if var == "CH" and t >= T0 and arm == "malign_unmeasured":
        lo += REAL          # unmeasured editing bias: numerically identical to a real effect
    return sample_prop(logistic(lo), N[var][s])


def mix(var, t, arm):
    if var == "CH" and arm == "malign_rate" and t >= T0:
        return {"A": 0.8, "B": 0.2}     # composition shifts toward the high-feminization stratum
    return {"A": 0.5, "B": 0.5}


def did(prop):
    return (statistics.mean(prop["CH"][y] for y in POST) - statistics.mean(prop["CH"][y] for y in PRE)) \
        - (statistics.mean(prop["FR"][y] for y in POST) - statistics.mean(prop["FR"][y] for y in PRE))


def true_did(arm):
    prop = {v: {t: sum(REF_MIX[s] * true_rate(v, t, s, arm) for s in STRATA) for t in YEARS}
            for v in ("CH", "FR")}
    return did(prop)


def estimates(arm):
    cells = {v: {t: {s: obs_rate(v, t, s, arm) for s in STRATA} for t in YEARS} for v in ("CH", "FR")}
    naive = {v: {t: sum(mix(v, t, arm)[s] * cells[v][t][s] for s in STRATA) for t in YEARS}
             for v in ("CH", "FR")}
    rew = {v: {t: sum(REF_MIX[s] * cells[v][t][s] for s in STRATA) for t in YEARS}
           for v in ("CH", "FR")}
    return did(naive), did(rew)


# ---- Part 1: recovery (averaged over reps for stable expectations) ----
random.seed(2024)
REPS = 200
print("PART 1  recovery: does each estimator hit the true DiD?\n")
print(f"{'arm':18} {'true':>7} {'naive':>7} {'reweight':>9}  {'naive biased':>12}  {'reweight recovers':>18}")
for arm in ("benign", "malign_rate", "malign_unmeasured"):
    td = true_did(arm)
    runs = [estimates(arm) for _ in range(REPS)]
    naive = statistics.mean(n for n, _ in runs)
    rew = statistics.mean(r for _, r in runs)
    print(f"{arm:18} {td:+7.3f} {naive:+7.3f} {rew:+9.3f}  {str(abs(naive-td) > TOL):>12}  "
          f"{str(abs(rew-td) <= TOL):>18}")


# ---- Part 2: partial pooling buys variance on the small variety ----
def pooled_cells(cells, var):
    out = {}
    for s in STRATA:
        for period in (PRE, POST):
            m = statistics.mean(cells[var][t][s] for t in period)
            w = N[var][s] / (N[var][s] + 600.0)   # small cells shrink harder toward the period mean
            for t in period:
                out.setdefault(t, {})[s] = w * cells[var][t][s] + (1 - w) * m
    return out


def reweighted_did(arm, pool):
    cells = {v: {t: {s: obs_rate(v, t, s, arm) for s in STRATA} for t in YEARS} for v in ("CH", "FR")}
    ch = pooled_cells(cells, "CH") if pool else {t: cells["CH"][t] for t in YEARS}
    fr = {t: cells["FR"][t] for t in YEARS}
    rw = {"CH": {t: sum(REF_MIX[s] * ch[t][s] for s in STRATA) for t in PRE + POST},
          "FR": {t: sum(REF_MIX[s] * fr[t][s] for s in STRATA) for t in PRE + POST}}
    return did(rw)


random.seed(2024)
raw = [reweighted_did("benign", False) for _ in range(REPS)]
random.seed(2024)   # identical draws, paired comparison
pooled = [reweighted_did("benign", True) for _ in range(REPS)]
print(f"\nPART 2  partial pooling (benign arm, {REPS} reps): reweighted DiD")
print(f"  raw small-variety cells : mean {statistics.mean(raw):+.3f}  SD {statistics.pstdev(raw):.4f}")
print(f"  partial-pooled cells    : mean {statistics.mean(pooled):+.3f}  SD {statistics.pstdev(pooled):.4f}")
print("  -> no SD gain here: for a 2-period DiD the pre/post averaging ALREADY pools across years,")
print("     so shrinking each year toward its period mean is a near no-op. Partial pooling earns its")
print("     keep at rung 2+, where you estimate many sparse group-time cells rather than two means.")
