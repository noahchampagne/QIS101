#!/usr/bin/env python3
"""sum_squares.py"""


def main() -> None:
    """Prints the sum of the squares from n=1 to n=1000 compared to the guassian sum"""
    n: int = 1_000
    total: int = 0
    # Adds the squared values to total
    for i in range(n + 1):
        total += i**2
    print(f"{total:,}")
    guassian_sum: int = int(((2 * n**3) + (3 * n**2) + n) / 6)
    print(f"{guassian_sum:,}")


if __name__ == "__main__":
    main()
