#!/usr/bin/env python3
# collatz_conjecture.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from numba import numba, jit, prange
import sys
import os


@jit(nopython=True)
def stop_time(n):
    counter = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        counter += 1
    return counter


@jit(nopython=True, parallel=True)
def stop_times(max_n):
    y = np.zeros(max_n, dtype=numba.int64)
    for i in prange(max_n):
        y[i] = stop_time(i)
    return y


def plot(ax):
    max_n = 1_000_000

    print(
        "Calculating the Collatz stopping time for"
        f" the first {max_n:,} natural numbers . . ."
    )

    y = stop_times(max_n)

    ax.set_title(f"Collatz Conjecture (n < {max_n:,})")
    ax.set_xlabel("Stopping Time")
    ax.set_ylabel("Count")

    ax.hist(y, bins=500, color="blue")

    ax.yaxis.set_minor_locator(AutoMinorLocator())


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
