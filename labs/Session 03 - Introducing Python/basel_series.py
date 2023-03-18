#!/usr/bin/env python3
"""basel_series.py"""

from math import sqrt


def sigma(n: int) -> float:
    """Sum the reciprocal of each integer squared from 1 to n inclusive"""
    s: float = 0.0
    for k in range(1, n + 1):
        s += 1 / k**2
    return s


def main() -> None:
    num_terms: int = 1_000_000
    series_sum: float = sigma(num_terms)
    print(f"Sum of first {num_terms:>7,} terms = {series_sum:.14f}")
    print(f"Magic number = {sqrt(series_sum * 6.0):.7f}")


if __name__ == "__main__":
    main()
