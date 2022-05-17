#!/usr/bin/env python3
# newton_sqrt.py


def square_root(x):
    lowEnd = 0
    highEnd = x

    estimate = (highEnd + lowEnd) / 2
    estimateSquared = estimate * estimate

    epsilon = 1e-14

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
    x = 168923

    x_sqrt = square_root(x)

    print(f"Estimated square root of \n {x:,}")
    print(f"is \n {x_sqrt:.14f}")


if __name__ == "__main__":
    main()
