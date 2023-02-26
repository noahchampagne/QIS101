#!/usr/bin/env python3
"""coprime_probability.py"""

from math import gcd, sqrt
from random import randint


def main():
    num_pairs = 1_000_000
    num_coprime_pairs = 0

    for _ in range(num_pairs):
        a = randint(1, 100_000)
        b = randint(1, 100_000)
        if gcd(a, b) == 1:
            num_coprime_pairs += 1

    probability = num_coprime_pairs / num_pairs

    print(f"Coprime Probability = {probability:.4f}")
    print(f"Hidden constant     = {sqrt(6 / probability):.4f}")


if __name__ == "__main__":
    main()
