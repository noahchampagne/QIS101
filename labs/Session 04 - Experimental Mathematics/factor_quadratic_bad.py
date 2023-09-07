#!/usr/bin/env python3
"""factor_quadratic.py"""


def factor_quadratic(h: int, i: int, j: int) -> None:
    """Displays factors of the quadratic polynomial Jx^2 + Kx + L"""

    print(f"Given the quadratic:{h}x^2 + {i}x + {j}")

    for a in range(1, h + 1):
        if h % a == 0:
            c: int = h // a
            for b in range(1, j + 1):
                if j % b == 0:
                    d: int = j // b
                    if a * d + b * c == i:
                        print(f"The factors are: ({a}x + {b})({c}x + {d})")


def main() -> None:
    factor_quadratic(115425, 3254121, 379020)


if __name__ == "__main__":
    main()
