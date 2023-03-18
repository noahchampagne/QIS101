#!/usr/bin/env python3
"""harmonic_series.py"""


def sigma(n: int) -> float:
    """Sum the reciprocal of each integer from 1 to n inclusive"""
    s: float = 0.0
    for k in range(1, n + 1):
        s += 1 / k
    return s


def main() -> None:
    for num_terms in range(1000, 11000, 1000):
        series_sum: float = sigma(num_terms)
        print(f"Sum of first {num_terms:>7,} terms = {series_sum:.14f}")


if __name__ == "__main__":
    main()
