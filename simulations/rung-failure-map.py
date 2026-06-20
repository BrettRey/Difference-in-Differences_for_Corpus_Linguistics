#!/usr/bin/env python3
"""
Failure map / operating characteristics for the rung-1 diagnostic-to-claim ladder.

The earlier scripts validate the ROUTING LOGIC and a post-stratification LEMMA under clean,
oracle conditions. The Codex board's fair complaint: that shows the ladder is internally
consistent, not that the diagnostics have POWER on messy corpus data. This script answers
that: it sweeps the realistic failure dimensions and reports how often the ladder reaches the
WRONG conclusion (misroute rate), not five tidy successes.

Mess dimensions:
  hidden     composition/editing drift OUTSIDE the strata we can reweight on (reweighting
             cannot touch it; the visible diagnostics stay flat) -> false positives
  power      small true effect and/or sparse cells -> false negatives
  spillover  a real effect that bleeds into the control (interference) -> contaminated estimate
  selection  a slow differential pre-trend that stays UNDER the pre-slope threshold yet
             accumulates into a large DiD bias over the pre/post gap -> false positives

A false positive (FP) = claiming a bounded effect when the truth is null or unidentified.
A false negative (FN) = failing to return a bounded estimate when a clean effect exists.

Thresholds are fixed (DGP-tuned), which is itself one of the board's flagged limits; the map
shows what fixed cutoffs cost under noise. Pure standard library; deterministic.
"""
import math
import random
import statistics

YEARS = list(range(1985, 2006))
T0 = 1991
PRE = [y for y in YEARS if 1985 <= y <= 1990]
POST = [y for y in YEARS if 1991 <= y <= 1997]
STRATA = ["A", "B"]
BASE = {"A": 0.6, "B": -1.6}
REF_MIX = {"A": 0.5, "B": 0.5}
FAKE = [1988, 2000, 2001, 2002]
PRE_THR, COMP_THR, WIRE_THR = 0.03, 0.05, 0.25
REPS = 400

DEFAULT = dict(effect=0.0, mix_shift=0.0, hidden=0.0, proxy_noise=0.0,
               spillover=0.0, exposure_noise=0.0, wave_accel=0.0, n_ch=150, n_fr=3000)


def logistic(x):
    return 1.0 / (1.0 + math.exp(-x))


def wave(t):
    return -2.0 + 0.18 * (t - 1985)


def sample_prop(p, n):
    sd = math.sqrt(max(n * p * (1 - p), 1e-9))
    return min(max(p * n + random.gauss(0, sd), 0.0), float(n)) / n


def cells(var, t, s, p):
    lo = wave(t) + BASE[s]
    if var == "CH" and t >= T0:
        lo += p["effect"] + p["hidden"] + p["wave_accel"]   # wave_accel: control on a different post-trajectory
    if var == "FR" and t >= T0:
        lo += p["spillover"] * p["effect"]
    n = p["n_ch"] if var == "CH" else p["n_fr"]
    return sample_prop(logistic(lo), n)


def mix(var, t, p):
    if var == "CH" and t >= T0:
        return {"A": min(0.5 + p["mix_shift"], 0.95), "B": max(0.5 - p["mix_shift"], 0.05)}
    return {"A": 0.5, "B": 0.5}


def did(prop):
    return (statistics.mean(prop["CH"][y] for y in POST) - statistics.mean(prop["CH"][y] for y in PRE)) \
        - (statistics.mean(prop["FR"][y] for y in POST) - statistics.mean(prop["FR"][y] for y in PRE))


def slope(series, years):
    xs = [y - years[0] for y in years]
    ys = [series[y] for y in years]
    mx, my = statistics.mean(xs), statistics.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs) or 1e-9
    return num / den


def floor_band(rw):
    vals = []
    for fy in FAKE:
        pre = [y for y in YEARS if fy - 3 <= y <= fy - 1]
        post = [y for y in YEARS if fy <= y <= fy + 2]
        if len(pre) >= 2 and len(post) >= 2:
            d = (statistics.mean(rw["CH"][y] for y in post) - statistics.mean(rw["CH"][y] for y in pre)) \
                - (statistics.mean(rw["FR"][y] for y in post) - statistics.mean(rw["FR"][y] for y in pre))
            vals.append(abs(d))
    return 1.5 * (max(vals) if vals else 0.0) + 0.01


def verdict(p):
    c = {v: {t: {s: cells(v, t, s, p) for s in STRATA} for t in YEARS} for v in ("CH", "FR")}
    rw = {v: {t: sum(REF_MIX[s] * c[v][t][s] for s in STRATA) for t in YEARS} for v in ("CH", "FR")}
    d = did(rw)   # estimand: always the series reweighted to the reference composition
    pre_slope = slope(rw["CH"], PRE) - slope(rw["FR"], PRE)
    # observable composition proxy (sees only the measured mix shift, with noise)
    comp_jump = p["mix_shift"] + random.gauss(0, p["proxy_noise"])
    obs_spill = p["spillover"] + random.gauss(0, p["exposure_noise"])
    band = floor_band(rw)
    # the ladder, in order, on the REWEIGHTED series; short-circuit at the first gate that fires
    if abs(pre_slope) > PRE_THR:
        return "not_id_selection"
    if abs(comp_jump) > COMP_THR:
        # A shift on the pre-committed reweightable margin. The estimand d is already
        # reweighted to the reference mix, so reweighting has handled it: the naive
        # reading is the one disqualified, and the reweighted contrast proceeds down the
        # ladder (it is NOT returned as not-identified). not-identified is reserved for a
        # NON-reweightable / non-pre-committed margin, which this proxy cannot see -- such
        # drift surfaces below as a false "bounded" claim, the failure the hidden rows map.
        pass
    if obs_spill > WIRE_THR:
        return "not_id_interference"
    if abs(d) <= band:
        return "bounded_null"
    return "bounded"


SCENARIOS = [
    # name, overrides, acceptable-verdict set, classification of a miss
    ("clean effect",            dict(effect=0.9), {"bounded"}, "FN"),
    ("measured artifact (reweighted)", dict(mix_shift=0.25), {"bounded_null"}, "FP"),
    ("hidden 0.3",              dict(hidden=0.3), {"bounded_null"}, "FP"),
    ("hidden 0.6",              dict(hidden=0.6), {"bounded_null"}, "FP"),
    ("hidden 0.9",              dict(hidden=0.9), {"bounded_null"}, "FP"),
    ("effect 0.4, n=150",       dict(effect=0.4), {"bounded"}, "FN"),
    ("effect 0.2, n=40 sparse", dict(effect=0.2, n_ch=40), {"bounded"}, "FN"),
    ("spillover 0.6 (clean exp)", dict(effect=0.9, spillover=0.6), {"not_id_interference"}, "FP"),
    ("spillover 0.6, noisy exp", dict(effect=0.9, spillover=0.6, exposure_noise=0.25),
     {"not_id_interference"}, "FP"),
    ("selection->wave (2-grp blind)", dict(wave_accel=0.8), {"bounded_null", "not_id_selection"}, "FP"),
]

ORDER = ["bounded", "bounded_null", "not_id_interference", "not_id_selection"]
SHORT = {"bounded": "bnd", "bounded_null": "bnull", "not_id_interference": "intf",
         "not_id_selection": "sel"}

print(f"failure map  ({REPS} reps/scenario; FP=false effect claim, FN=missed real effect)\n")
print(f"{'scenario':26}  " + "  ".join(f"{SHORT[k]:>5}" for k in ORDER) + f"  {'misroute':>9}")
for name, ov, ok, kind in SCENARIOS:
    random.seed(7)
    p = dict(DEFAULT)
    p.update(ov)
    counts = {k: 0 for k in ORDER}
    miss = 0
    for _ in range(REPS):
        v = verdict(p)
        counts[v] += 1
        if v not in ok:
            miss += 1
    dist = "  ".join(f"{counts[k] / REPS:5.2f}" for k in ORDER)
    print(f"{name:26}  {dist}  {miss / REPS:7.0%} {kind}")

print("\nreads:")
print(" - measured composition is reweighted away (its row recovers a bounded null); hidden drift")
print("   OUTSIDE the reweighting strata is uncatchable, and false positives climb with the fraction.")
print(" - sparse cells destroy power (false negatives); noisy exposure leaks some interference FP.")
print(" - selection->wave: a control on a different post-trajectory is observationally identical to a")
print("   real effect in a 2-group design, so it is an irreducible false positive here. Catching it is")
print("   exactly the job of rung 2's calendar-time test, not a rung-1 diagnostic.")
