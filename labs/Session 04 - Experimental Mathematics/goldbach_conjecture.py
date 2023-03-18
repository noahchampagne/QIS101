#!/usr/bin/env python3
"""goldbach_conjecture.py"""

from __future__ import annotations

import typing
from itertools import combinations_with_replacement
from typing import cast

import numpy as np
from numpy.typing import ArrayLike  # type: ignore
from sympy import prime  # type: ignore

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


def main() -> None:
    """Demonstrate Goldbach's Conjecture"""
    test_limit: int = 100

    print("Verifying Goldbach's conjecture for every even ", end="")
    print(f"integer from 6 to {test_limit} inclusive:")

    # Use a list comprehension to generate a list of first 'n' primes
    primes: list[int] = cast(list[int],
                              [prime(n) for n in range(2, test_limit)])  # type: ignore

    # Generate all pairs of primes (with repetition)
    prime_pairs: list[tuple[int, ...]] = [
        *combinations_with_replacement(primes, 2)  # type: ignore
    ]

    # Create sorted list containing the sum of each pairwise primes
    summed_pairs: NDArray[np.float_] = np.sort(
        cast(ArrayLike, [sum(pair) for pair in prime_pairs])
    )

    # Determine which EVEN integers from 6 to n (inclusive)
    # are NOT in the list of summed prime pairs
    # The numpy function setdiff1d() returns any elements in the first list
    # that are not also in the second list
    violations: NDArray[np.int_] = np.setdiff1d(
        range(6, test_limit + 2, 2), summed_pairs
    )

    if len(violations) == 0:
        print("No Goldbach violations were found")
    else:
        print(f"Found these violations: {violations}")


if __name__ == "__main__":
    main()
