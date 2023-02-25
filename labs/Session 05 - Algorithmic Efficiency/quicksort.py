#!/usr/bin/env python3
"""quicksort.py"""


import time

import numpy as np


def main():
    np.random.seed(2016)

    samples = np.random.randint(1, 101, 100)
    print(f"Unsorted: {samples}\n")

    samples = np.sort(samples)
    print(f"Sorted: {samples}\n")

    num_trials = 10_000
    print(f"Running {num_trials:,} trials . . .")
    start_time = time.process_time()

    for _ in range(num_trials):
        samples = np.random.randint(1, 101, 100)
        samples = np.sort(samples)

    elapsed_time = time.process_time() - start_time

    print(f"Total run time: {elapsed_time:.3f} s")


if __name__ == "__main__":
    main()
