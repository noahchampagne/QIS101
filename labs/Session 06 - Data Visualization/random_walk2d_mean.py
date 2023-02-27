#!/usr/bin/env python3
"""random_walk2d_mean.py"""

import os
import sys
from time import process_time

import matplotlib.pyplot as plt
import numpy as np
from numba import njit


@njit()
def get_avg_dist(max_steps: int, num_walks: int) -> np.ndarray:
    """Return expected distance of (num_walks) 2d walks of length (num_steps)"""
    avg_dist = np.zeros(max_steps - 1, dtype=float)
    for step in range(1, max_steps):
        total_dist = 0.0
        for _ in range(num_walks):
            x, y = 0.0, 0.0
            for _ in range(step):
                theta = np.random.rand() * 2 * np.pi
                x += np.cos(theta)
                y += np.sin(theta)
            total_dist += np.sqrt(x**2 + y**2)
        avg_dist[step] = total_dist / num_walks
    return avg_dist


def fit_linear(x, y):
    n = len(x)
    m = n * np.sum(x * y) - np.sum(x) * np.sum(y)
    m /= n * np.sum(x**2) - np.sum(x) ** 2
    b = np.sum(y) - m * np.sum(x)
    b /= n
    return m, b


def main():
    start_time = process_time()

    # Walks increase in length from 1 to max_steps
    max_steps = 200

    # Number of times a walk of each length is repeated to find its average
    num_walks = 100_000

    print("This might take several minutes...")

    steps = np.arange(1, max_steps, dtype=float)
    distances = get_avg_dist(max_steps, num_walks)
    distances_squared = distances**2
    m, b = fit_linear(steps, distances_squared)

    fig = plt.figure(os.path.basename(sys.argv[0]))
    fig.set_size_inches(12, 5)
    gs = fig.add_gridspec(1, 2)

    ax = fig.add_subplot(gs[0, 0])
    ax.plot(steps, distances)
    ax.set_title("2D Random Walk")
    ax.set_xlabel("Number of Steps")
    ax.set_ylabel("Average Distance")
    ax.plot()

    ax = fig.add_subplot(gs[0, 1])
    ax.plot(steps, distances_squared, color="green")
    ax.plot(steps, m * steps + b, color="red", linewidth=2)
    ax.set_title(rf"$Slope\;of\;Line\times{{4}}={4*m:.2f}$")
    ax.set_xlabel("Number of Steps")
    ax.set_ylabel(r"$(Average\;Distance)^2$")
    ax.plot()

    elapsed_time = process_time() - start_time
    print(f"Total run time (sec): {elapsed_time:.3f}\n")

    plt.show()


if __name__ == "__main__":
    main()
