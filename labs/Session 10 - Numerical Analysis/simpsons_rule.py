#!/usr/bin/env python3
# simpsons_rule.py


def f(x):
    # This is the function we are numerically integrating
    return (x + 9) * (x + 4) * (x + 1) * (x - 5) * (x - 11)


def F(x):
    # This is the exact analytic integral of our function
    return (
        1 / 6 * pow(x, 6)
        - 2 / 5 * pow(x, 5)
        - 30 * pow(x, 4)
        + 22 / 3 * pow(x, 3)
        + 2119 / 2 * pow(x, 2)
        + 1980 * x
    )


def left_hand_rule(f, a, b, intervals):
    dx = (b - a) / intervals
    area = 0
    for i in range(0, intervals):
        area += f(a + i * dx)
    return dx * area


def simpsons_rule(f, a, b, intervals):
    dx = (b - a) / intervals
    area = f(a) + f(b)
    for i in range(1, intervals):
        area += f(a + i * dx) * (2 * (i % 2 + 1))
    return dx / 3 * area


def main():
    a, b = -10.0, 12.0
    intervals = int(1e6)

    print("Integrating " "x^5 - 2x^4 - 120x^3 + 22x^2 + 2199x + 1980")
    print(f" over [{a}, {b}] using {intervals:,} intervals\n")

    area_actual = F(b) - F(a)
    print(f"Analytic (Exact) : {area_actual:.14f}\n")

    area_left_hand = left_hand_rule(f, a, b, intervals)
    print(f"Left-hand Rule   : {area_left_hand:.14f}")
    print(
        f"% Rel Error      : "
        f"{(area_left_hand - area_actual) / area_actual * 100:.14f}\n"
    )

    area_simpsons = simpsons_rule(f, a, b, intervals)
    print(f"Simpson's Rule   : {area_simpsons:.14f}")
    print(
        f"% Rel Error      : "
        f"{(area_simpsons - area_actual) / area_actual * 100:.14f}"
    )


if __name__ == "__main__":
    main()
