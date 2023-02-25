#!/usr/bin/env python3
"""bubble_sort.py"""


import time

import numpy as np


def bubble_sort(ary: np.ndarray):
    """Sorts the provided list in increasing order using the Bubble Sort algorithm"""
    last_index = len(ary) - 1
    is_sorted = False
    while not is_sorted:
        swap_needed = False
        for i in range(last_index):
            if ary[i] > ary[i + 1]:
                temp = ary[i]
                ary[i] = ary[i + 1]
                ary[i + 1] = temp
                swap_needed = True
        if not swap_needed:
            is_sorted = True
        else:
            last_index -= 1
    return ary


def main():
    np.random.seed(2016)

    samples = np.random.randint(1, 101, 100)
    print(f"Unsorted: {samples}\n")

    samples = bubble_sort(samples)
    print(f"Sorted: {samples}\n")

    num_trials = 10_000
    print(f"Running {num_trials:,} trials . . .")
    start_time = time.process_time()

    for _ in range(num_trials):
        samples = np.random.randint(1, 101, 100)
        samples = bubble_sort(samples)

    elapsed_time = time.process_time() - start_time

    print(f"Total run time: {elapsed_time:.3f} s")


if __name__ == "__main__":
    main()
