#!/usr/bin/env python3
"""prime_racer2.py"""

from random import randint, seed
from time import process_time


def is_prime(n: int) -> bool:
    """Returns True/False if the given number is prime"""
    if n % 2 == 0:
        return False
    return all(n % factor != 0 for factor in range(3, n, 2))


def main():
    seed(2016)

    num_samples, min_val, max_val = int(1e4), int(1e5), int(1e6)

    print(
        f"Counting the number of primes in {num_samples:,} random samples\n"
        f"with each sample having a value between {min_val:,} "
        f"and {max_val:,} inclusive . . .",
    )

    samples = [randint(min_val, max_val) for _ in range(num_samples)]

    start_time = process_time()
    num_primes = [is_prime(n) for n in samples].count(True)
    elapsed_time = process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
