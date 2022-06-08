#!/usr/bin/env python3
# goldbach_conjecture.py


import numpy as np
from sympy import prime
from itertools import combinations_with_replacement


def main():
    n = 100

    print(f"Verifying Goldbach's conjecture " f"for every even integer from 6 to {n}:")

    # Use a list comprehension to generate a list of first 'n' primes
    primes = [prime(n) for n in range(2, n)]

    # Generate all pairs of primes (with repetition)
    prime_pairs = [*combinations_with_replacement(primes, 2)]

    # Create sorted list containing the sum of each pairwise primes
    summed_pairs = np.sort([sum(pair) for pair in prime_pairs])

    # Determine which EVEN integers from 6 to n (inclusive)
    # are NOT in the list of summed prime pairs
    # The numpy function setdiff1d() returns any elements in the first list
    # that are not also in the second list
    violations = np.setdiff1d(range(6, n + 2, 2), summed_pairs)

    if len(violations) == 0:
        print("No Goldbach violations were found")
    else:
        print(f"Found these violations: {violations}")


if __name__ == "__main__":
    main()
