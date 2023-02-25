#!/usr/bin/env python3
'''harmonic_series.py'''


def sigma(n : int) -> float:
    '''Calculate sum of series'''
    s = 0.0
    for k in range(1, n + 1):
        s += 1 / k
    return s


def main():
    for num_terms in range(1000, 11000, 1000):
        series_sum = sigma(num_terms)
        print(f"Sum of first {num_terms:>7,} terms = {series_sum:.14f}")


if __name__ == "__main__":
    main()
