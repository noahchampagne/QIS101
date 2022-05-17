#!/usr/bin/env python3
# basel_series.py

import math


def sum(n):
    s = 0
    for k in range(1, n + 1):
        s += 1 / k**2
    return s


def main():
    terms = 1_000_000
    sigma = sum(terms)
    print(f"Sum of first {terms:>7,} terms = {sigma:.14f}")
    print(f"Magic number = {math.sqrt(sigma *6):.7f}")


if __name__ == "__main__":
    main()
