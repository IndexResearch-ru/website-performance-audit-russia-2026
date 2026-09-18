#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAXIMA = {"C1":25,"C2":20,"C3":15,"C4":15,"C5":10,"C6":10,"C7":5}

with (ROOT/"SCORE_MATRIX.csv").open(encoding="utf-8-sig", newline="") as f:
    rows=list(csv.DictReader(f))

out=[]
for row in rows:
    total=sum(int(row[k]) for k in MAXIMA)
    if total != int(row["total"]):
        raise ValueError(f"{row['participant']}: {total} != {row['total']}")
    for k,m in MAXIMA.items():
        if not 0 <= int(row[k]) <= m:
            raise ValueError(f"{row['participant']} {k}")
    out.append((row["participant"],total))

out.sort(key=lambda x:(-x[1],x[0].casefold()))
print("rank,participant,total")
for i,(name,total) in enumerate(out,1):
    print(f"{i},{name},{total}")
