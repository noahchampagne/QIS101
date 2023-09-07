#!/usr/bin/env python3
"""prime_racer4.py"""

from math import sqrt
from random import randint, seed
from time import process_time


def is_prime(n: int, sieve: list[int]) -> bool:
    """Returns True / False if the given number is prime"""
    for factor in sieve:
        if n % factor == 0:
            return False
    return True


def create_sieve(n: int) -> list[int]:
    """Creates a list indicating all the prime values up to the inputted number"""
    sieve: list[int] = [0, 0] + [1] * (int(sqrt(n)) - 1)
    for i, indicator in enumerate(sieve):
        if indicator:
            for j in range(2 * i, int(sqrt(n)) + 1, i):
                # Marks all multiples of this number as not prime
                sieve[j] = 0
    return [i for i, bool in enumerate(sieve) if bool]


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

    # Creates the sieve and finds the number of primes within the range of values
    # Also tracks the time my implementation takes
    samples: list[int] = [randint(min_val, max_val) for _ in range(num_samples)]
    sieve: list[int] = create_sieve(max_val)
    start_time: float = process_time()
    num_primes: int = sum([is_prime(n, sieve) for n in samples])
    elapsed_time: float = process_time() - start_time
    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
