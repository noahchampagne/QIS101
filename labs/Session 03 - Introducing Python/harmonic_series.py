#!/usr/bin/env python3
# harmonic_series.py


def sum(n):
    s = 0
    for k in range(1, n + 1):
        s += 1 / k
    return s


def main():
    for terms in range(1000, 11000, 1000):
        sigma = sum(terms)
        print(f"Sum of first {terms:>7,} terms = {sigma:.14f}")


if __name__ == "__main__":
    main()
