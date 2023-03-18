#!/usr/bin/env python3
"""perfect_numbers.py"""


def is_perfect_number(n: int) -> bool:
    """Determine if n is a perfect number"""
    sum_of_factors: int = 1
    for factor in range(2, n):
        if n % factor == 0:
            sum_of_factors += factor
    return sum_of_factors == n


def main() -> None:
    for n in range(2, 10_000):
        if is_perfect_number(n):
            print(f"{n:,} is a perfect number")


if __name__ == "__main__":
    main()
