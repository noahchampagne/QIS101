#!/usr/bin/env python3
# random_straws.py

import numpy as np


def run_trial():
    length = straws = 0.0
    while length <= 1.0:
        length += np.random.random()
        straws += 1
    return straws


def main():
    np.random.seed(2016)

    num_trials = int(1e7)

    print(f"Performing {num_trials:,} trials...")

    total_straws = 0

    for _ in range(0, num_trials):
        total_straws += run_trial()

    mean = total_straws / num_trials

    print(f"Mean straws per trial     : {mean:.6f}")
    print(f"Base of natural logarithm : {np.e:.6f}")


if __name__ == "__main__":
    main()
