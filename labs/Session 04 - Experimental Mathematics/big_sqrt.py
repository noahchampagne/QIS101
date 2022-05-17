#!/usr/bin/env python3
# big_sqrt.py

# From http://mpmath.org
from mpmath import mp, mpf, nstr


def square_root(x):
    lowEnd = mpf(0)
    highEnd = mpf(x)

    estimate = mpf(highEnd + lowEnd / 2)
    estimateSquared = mpf(estimate * estimate)

    epsilon = mpf(1e-14)

    while abs(estimateSquared - x) > epsilon:
        if estimateSquared > x:
            highEnd = estimate
        else:
            lowEnd = estimate

        estimate = (highEnd + lowEnd) / 2
        estimateSquared = estimate * estimate

        if highEnd == lowEnd:
            break

    return estimate


def main():
    mp.dps = 200  # dps = decimal places

    x = 33590351381261822622218163873528556813698947665687615688767589021060440979380129292322236643684251591

    x_sqrt = square_root(x)

    print(f"Estimated square root of \n {x}")
    print(f"is \n {nstr(x_sqrt, 100)}")


if __name__ == "__main__":
    main()
