#!/usr/bin/env python3
"""random_walk_lattice.py"""

from __future__ import annotations

import os
import sys
import typing
from time import process_time

import matplotlib.pyplot as plt
import numpy as np
from numba import njit  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.gridspec import GridSpec
    from numpy.typing import NDArray


@njit()  # type: ignore
def get_avg_dist(dims: int, max_steps: int, num_walks: int) -> NDArray[np.float_]:
    # Returns the mean final distance (normalized)
    # of (num_walks) uniform random walks having length (num_steps)
    # on a unit lattice having (dim) dimensions
    avg_dist: NDArray[np.float_] = np.zeros(max_steps, dtype=np.float64)
    for step in range(max_steps):
        total_dist: float = 0.0
        for _ in range(num_walks):
            steps: NDArray[np.int_] = np.zeros(dims, dtype=np.int64)
            for _ in range(step):
                h: int = np.random.randint(0, dims)
                steps[h] += -1 if np.random.rand() < 0.5 else 1
            total_dist += np.sqrt(np.sum(np.power(steps, 2)))
        avg_dist[step] = total_dist / num_walks
    return avg_dist


def fit_linear(x: NDArray[np.float_], y: NDArray[np.float_]) -> tuple[float, float]:
    n: int = len(x)
    m: float = float(n * np.sum(x * y) - np.sum(x) * np.sum(y))
    m /= float(n * np.sum(x**2) - np.sum(x) ** 2)
    b: float = float(np.sum(y) - m * np.sum(x))
    b /= n
    return m, b


def main() -> None:
    start_time: float = process_time()

    # Number of dimensions
    dims: int = 2

    # Walks increase in length from 1 to max_steps
    max_steps: int = 200

    # Number of times a walk of each length is repeated to find its average
    num_walks: int = 50_000

    print("This might take several minutes...")

    steps: NDArray[np.float_] = np.arange(max_steps, dtype=np.float_)
    distances: NDArray[np.float_] = get_avg_dist(dims, max_steps, num_walks)
    distances_squared: NDArray[np.float_] = distances**2
    m: float
    b: float
    m, b = fit_linear(steps, distances_squared)

    fig: Figure = plt.figure(os.path.basename(sys.argv[0]))
    fig.set_size_inches(12, 5)
    gs: GridSpec = fig.add_gridspec(1, 2)

    ax: Axes = fig.add_subplot(gs[0, 0])
    ax.plot(steps, distances)
    ax.set_title(f"Uniform Random Walk on {dims}-D Unit Lattice")
    ax.set_xlabel("Number of Steps")
    ax.set_ylabel("Mean Final Distance (Normalized)")
    ax.plot()

    ax = fig.add_subplot(gs[0, 1])
    ax.plot(steps, distances_squared, color="green")
    ax.plot(steps, m * steps + b, color="red", linewidth=2)
    print(m)
    ax.set_title(rf"$Slope\;of\;Line\times{{4}}={4*m:.4f}$")
    ax.set_xlabel("Number of Steps")
    ax.set_ylabel(r"$(Mean\;Final\;Distance)^2$")
    ax.plot()

    elapsed_time: float = process_time() - start_time
    print(f"Total run time (sec): {elapsed_time:.3f}\n")

    plt.show()


if __name__ == "__main__":
    main()
