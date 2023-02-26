#!/usr/bin/env python3
"""basel_series.py"""

from math import sqrt


def sigma(n: int) -> float:
    """Sum the reciprocal of each integer squared from 1 to n inclusive"""
    s = 0.0
    for k in range(1, n + 1):
        s += 1 / k**2
    return s


def main():
    num_terms = 1_000_000
    series_sum = sigma(num_terms)
    print(f"Sum of first {num_terms:>7,} terms = {series_sum:.14f}")
    print(f"Magic number = {sqrt(series_sum *6):.7f}")


if __name__ == "__main__":
    main()
