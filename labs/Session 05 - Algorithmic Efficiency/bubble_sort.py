#!/usr/bin/env python3
# bubble_sort.py

import numpy as np
import time


def init_samples():
    samples = []
    for i in range(100):
        samples.append(np.random.randint(1, 101))
    return samples


def bubble_sort(samples):
    last_index = len(samples) - 1
    is_sorted = False
    while not is_sorted:
        swap_needed = False
        for i in range(last_index):
            if samples[i] > samples[i + 1]:
                temp = samples[i]
                samples[i] = samples[i + 1]
                samples[i + 1] = temp
                swap_needed = True
        if not swap_needed:
            is_sorted = True
        else:
            last_index -= 1
    return samples


def main():
    np.random.seed(2021)

    samples = init_samples()
    print(f"Unsorted: {samples}")

    samples = bubble_sort(samples)
    print(f"Sorted: {samples}")

    num_trials = 10_000
    print(f"Running {num_trials:,} trials . . .")
    start_time = time.process_time()

    for _ in range(num_trials):
        samples = init_samples()
        samples = bubble_sort(samples)

    elapsed_time = time.process_time() - start_time

    print(f"Total run time: {elapsed_time:.3f} s")


if __name__ == "__main__":
    main()
