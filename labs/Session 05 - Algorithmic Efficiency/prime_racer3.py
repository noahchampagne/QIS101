#!/usr/bin/env python3
# prime_racer3.py

import numpy as np
import random
import time


def init_samples(num_samples, min_sample, max_sample):
    samples = [None] * num_samples
    for idx, _ in enumerate(samples):
        samples[idx] = random.randint(min_sample, max_sample)
    return samples


def is_prime(n):
    if n % 2 == 0:
        return False
    for factor in range(3, int(np.sqrt(n)), 2):
        if n % factor == 0:
            return False
    return True


def count_primes(samples):
    num_primes = 0
    for _, val in enumerate(samples):
        if is_prime(val):
            num_primes += 1
    return num_primes


def main():
    random.seed(2016)

    num_samples = int(1e4)
    min_sample_val = int(1e5)
    max_sample_val = int(1e6)

    samples = init_samples(num_samples, min_sample_val, max_sample_val)

    print(
        f"Counting the number of primes in {num_samples:,} random samples\n"
        f"with each sample having a value between {min_sample_val:,} "
        f"and {max_sample_val:,} inclusive . . .",
    )

    start_time = time.process_time()
    num_primes = count_primes(samples)
    elapsed_time = time.process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
