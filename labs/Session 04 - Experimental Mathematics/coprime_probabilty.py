#!/usr/bin/env python3
# coprime_probability.py

import numpy as np


def main():
    np.random.seed(2021)

    num_coprime_pairs = 0

    for _ in range(1_000_000):
        a = np.random.randint(100_000)
        b = np.random.randint(100_000)
        if np.gcd(a, b) == 1:
            num_coprime_pairs += 1

    p = num_coprime_pairs / 1_000_000

    print(f"Coprime Probability = {p:.4f}")
    print(f"Hidden constant     = {np.sqrt(6 / p):.4f}")


if __name__ == "__main__":
    main()
