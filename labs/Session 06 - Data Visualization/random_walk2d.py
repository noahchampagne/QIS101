#!/usr/bin/env python3
"""random_walk2d.py"""

import os
import sys

import matplotlib.pyplot as plt
import numpy as np


def plot(ax: plt.Axes):
    np.random.seed(2016)

    num_steps = 10000

    theta = np.random.random(num_steps) * 2 * np.pi
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)

    for i in range(1, num_steps):
        x[i] = x[i - 1] + np.cos(theta[i])
        y[i] = y[i - 1] + np.sin(theta[i])

    ax.plot(x, y)

    ax.plot(x[0], y[0], color="green", marker="o")
    ax.plot(x[-1], y[-1], color="red", marker="o")
    ax.arrow(
        x[0],
        y[0],
        x[-1] - x[0],
        y[-1] - y[0],
        color="black",
        linestyle="--",
        width=0.3,
        head_width=1,
        length_includes_head=True,
        zorder=3,
    )

    ax.set_title("Uniform 2D Random Walk")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
