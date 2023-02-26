#!/usr/bin/env python3
"""random_straws.py"""

import math
from random import random


def run_trial() -> int:
    """Returns number of random length straws with length > 1.0"""
    length, straws = 0.0, 0
    while length <= 1.0:
        length += random()
        straws += 1
    return straws


def main():
    num_trials = int(1e7)

    print(f"Performing {num_trials:,} trials...")

    total_straws = 0

    for _ in range(0, num_trials):
        total_straws += run_trial()

    mean = total_straws / num_trials

    print(f"Mean straws per trial     : {mean:.6f}")
    print(f"Base of natural logarithm : {math.e:.6f}")


if __name__ == "__main__":
    main()
