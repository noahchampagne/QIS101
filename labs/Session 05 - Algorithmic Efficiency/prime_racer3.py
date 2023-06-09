#!/usr/bin/env python3
"""prime_racer3.py"""

from math import sqrt
from random import randint, seed
from time import process_time


def is_prime(n: int) -> bool:
    """Returns True/False if the given number is prime"""
    if n % 2 == 0:
        return False
    return all(n % factor != 0 for factor in range(3, int(sqrt(n)), 2))


def main() -> None:
    seed(2016)

    num_samples: int = 10_000
    min_val: int = 100_000
    max_val: int = 1_000_000

    print(
        (
            f"Counting the number of primes in {num_samples:,} random samples\n"
            f"with each sample having a value between {min_val:,} "
            f"and {max_val:,} inclusive . . ."
        )
    )

    samples: list[int] = [randint(min_val, max_val) for _ in range(num_samples)]

    start_time: float = process_time()
    num_primes: int = [is_prime(n) for n in samples].count(True)
    elapsed_time: float = process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
