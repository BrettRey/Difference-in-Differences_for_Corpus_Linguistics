#!/usr/bin/env python3
"""Speaker-pool composition audit, Swiss Nationalrat, from the Federal Assembly's
open OData service. Standard library only. No key or registration required.

This is not a simulation. It measures a real composition margin of a real archive,
to show that the confound Section 8 names is present and steep across the 1991
treatment date.

Why MemberCouncilHistory and not MemberCouncil: MemberCouncil carries one row per
person per council with a single mandate's dates, so a member who served several
terms is invisible at reference dates outside the stored mandate. Reconstructing
sitting membership from it undercounts badly and increasingly with age of the
reference date (168, 142, 113, 75, 56 against a 200-seat chamber). Mandate history
carries every mandate; deduplicating on PersonNumber then recovers the chamber.

Validation built in: the Nationalrat has had 200 seats since 1963, so post-1963
reference dates should return 200 or a little under (mid-term vacancies). The 2019
election returned 84 women of 200, which the 2020 row should reproduce.
"""
import datetime
import json
import re
import urllib.request

SERVICE = "https://ws.parlament.ch/odata.svc/MemberCouncilHistory"
FIELDS = "PersonNumber,GenderAsString,DateJoining,DateLeaving,CouncilAbbreviation"
YEARS = [1971, 1975, 1980, 1985, 1990, 1991, 1995, 2000, 2010, 2020]


def fetch():
    rows, skip = [], 0
    while True:
        url = (f"{SERVICE}?$filter=Language%20eq%20'DE'&$select={FIELDS}"
               f"&$format=json&$top=1000&$skip={skip}")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        batch = json.load(urllib.request.urlopen(req, timeout=120))["d"]
        if not batch:
            return rows
        rows += batch
        skip += 1000


def as_date(v):
    m = re.search(r"-?\d+", v) if v else None
    return datetime.date(1970, 1, 1) + datetime.timedelta(milliseconds=int(m.group())) if m else None


def main():
    raw = fetch()
    mandates = [(r["PersonNumber"], r["GenderAsString"], as_date(r["DateJoining"]),
                 as_date(r["DateLeaving"]), r["CouncilAbbreviation"]) for r in raw]
    print(f"mandate records retrieved: {len(raw)}\n")
    print("Share of women in the Nationalrat, sitting members on 31 December")
    print("  year  women  seats   share")
    for y in YEARS:
        ref = datetime.date(y, 12, 31)
        sitting = {p: g for p, g, join, leave, council in mandates
                   if council == "NR" and join and join <= ref and (leave is None or leave > ref)}
        women = sum(1 for g in sitting.values() if g == "f")
        n = len(sitting)
        print(f"  {y}  {women:5d}  {n:5d}   {women / n * 100:5.1f}%")
    print("\nValidation: seats should be 200 or slightly under after 1963;")
    print("2020 should give 84 of 200, matching the 2019 federal election result.")


if __name__ == "__main__":
    main()
