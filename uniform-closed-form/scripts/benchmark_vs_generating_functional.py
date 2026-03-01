#!/usr/bin/env python3
"""
scripts/test_performance_benchmark.py

V&V: Performance benchmark of closed-form vs generating-functional implementation.
Writes results to data/performance_benchmark_results.csv.
"""

import os
import sys
import time
import csv

# —————————————————————————————————————————————————————————
# set up imports for both repos
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# this repo
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
sys.path.insert(0, REPO_ROOT)

# generating-functional repo: assume sibling folder of this repo
BASE_DIR = os.path.abspath(os.path.join(REPO_ROOT, os.pardir))
GF_PROJ  = os.path.join(BASE_DIR, "su2-3nj-generating-functional", "project")
sys.path.insert(0, GF_PROJ)
# —————————————————————————————————————————————————————————

# now import the two entry points
from su2_3nj import generate_3nj
from project.su2_3nj_closed_form import closed_form_3nj

# the spin‐tuple we’ll benchmark
js = (10, 10, 10, 10, 10, 10)

def main():
    # prepare data directory
    DATA_DIR = os.path.join(REPO_ROOT, "data")
    os.makedirs(DATA_DIR, exist_ok=True)
    OUT_CSV  = os.path.join(DATA_DIR, "performance_benchmark_results.csv")

    # time the generating‐functional implementation
    t0 = time.time()
    generate_3nj(*js)
    t_gen = time.time() - t0

    # time the closed‐form implementation
    t0 = time.time()
    closed_form_3nj(*js)
    t_closed = time.time() - t0

    # record whether closed‐form is faster
    closed_is_faster = t_closed < t_gen

    # write out a CSV
    with open(OUT_CSV, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "spins",
            "time_generate_functional_s",
            "time_closed_form_s",
            "closed_form_faster"
        ])
        writer.writerow([
            ",".join(map(str, js)),
            f"{t_gen:.6f}",
            f"{t_closed:.6f}",
            closed_is_faster
        ])

    # print a summary
    print(f"generate_3nj: {t_gen:.6f}s")
    print(f"closed_form_3nj: {t_closed:.6f}s")
    if closed_is_faster:
        print("PASS: closed-form is faster")
        sys.exit(0)
    else:
        print("FAIL: closed-form is not faster")
        sys.exit(1)

if __name__ == "__main__":
    main()
