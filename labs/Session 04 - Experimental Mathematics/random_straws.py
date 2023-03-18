#!/usr/bin/env python3
"""random_straws.py"""

import math
from random import random


def run_trial() -> int:
    """Returns number of random length straws with length > 1.0"""
    total_length: float = 0.0
    num_straws: int = 0
    while total_length <= 1.0:
        total_length += random()
        num_straws += 1
    return num_straws


def main() -> None:
    num_trials: int = int(1e7)

    print(f"Performing {num_trials:,} trials...")

    total_straws: int = 0

    for _ in range(0, num_trials):
        total_straws += run_trial()

    mean_length: float = total_straws / num_trials

    print(f"Mean straws per trial     : {mean_length:.6f}")
    print(f"Base of natural logarithm : {math.e:.6f}")


if __name__ == "__main__":
    main()
