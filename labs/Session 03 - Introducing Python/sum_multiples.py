#!/usr/bin/env python3
"""sum_multiples.py"""


def main() -> None:
    """Sums the multiples of 7 and 11 from n=1 to n=18999"""
    total = 0
    for n in range(19_000):
        if (n % 7) == 0 and (n % 11) == 0:
            total += n
    print(f"{total:,}")


if __name__ == "__main__":
    main()
