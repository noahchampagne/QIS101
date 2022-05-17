#!/usr/bin/env python3
# quicksort.py

import numpy as np
import time


def init_samples():
    samples = np.random.randint(1, 101, 100)
    return samples


def main():
    np.random.seed(2021)

    samples = init_samples()
    print(f"Unsorted: {samples}")

    samples = np.sort(samples)
    print(f"Sorted: {samples}")

    num_trials = 10_000
    print(f"Running {num_trials:,} trials . . .")
    start_time = time.process_time()

    for _ in range(num_trials):
        samples = init_samples()
        samples = np.sort(samples)

    elapsed_time = time.process_time() - start_time

    print(f"Total run time: {elapsed_time:.3f} s")


if __name__ == "__main__":
    main()
