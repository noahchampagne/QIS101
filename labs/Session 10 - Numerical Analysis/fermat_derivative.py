#!/usr/bin/env python3
# fermat_derivative.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import sys
import os


def f(x):
    return np.cos(x)


def f_prime(x, h):
    return (f(x + h) - f(x)) / h


def plot(ax):
    a = -4 * np.pi
    b = 4 * np.pi
    n = 500

    x = np.linspace(a, b, n)

    y = f(x)
    y_prime = f_prime(x, (b - a) / n)

    ax.plot(x, y, label="y")
    ax.plot(x, y_prime, label=r"$\frac{dy}{dx}$")

    ax.set_title(r"$y = cos(x)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    ax.legend(loc="upper right")

    ax.axhline(0, color="black", linestyle="-")
    ax.axvline(0, color="black", linestyle="-")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
