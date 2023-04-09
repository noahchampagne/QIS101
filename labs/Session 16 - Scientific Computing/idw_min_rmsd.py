#!/usr/bin/env python3
"""idw_min_rmsd.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from numba import njit  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

ocean_size: int = 390
num_intervals: int = 65
num_samples: int = 220

samples_x: NDArray[np.float_]
samples_y: NDArray[np.float_]
samples_z: NDArray[np.float_]

grid_x: NDArray[np.float_]
grid_y: NDArray[np.float_]
grid_z: NDArray[np.float_]

est_z: NDArray[np.float_]


def act_height(x: NDArray[np.float_], y: NDArray[np.float_]) -> NDArray[np.float_]:
    # Calculate the height of the "actual" ocean at (x,y)
    return np.array(
        (
            30 * np.sin(y / 40) * np.cos(x / 40)
            + 50 * np.sin(np.sqrt(x * x + y * y) / 40)
        )
        - 800
    )


def init_samples() -> None:
    np.random.seed(2016)

    global ocean_size, num_intervals, num_samples
    ocean_size = 390
    num_intervals = 65
    num_samples = 220

    global grid_x, grid_y, grid_z
    grid_x, grid_y = np.mgrid[
        # See numpy.mgrid() docs for why using complex() for step length
        0 : ocean_size : complex(0, num_intervals),  # type: ignore
        0 : ocean_size : complex(0, num_intervals),  # type: ignore
    ]
    grid_z = act_height(grid_x, grid_y)

    global samples_x, samples_y, samples_z
    samples_x = np.random.uniform(0, ocean_size, num_samples)
    samples_y = np.random.uniform(0, ocean_size, num_samples)
    samples_z = act_height(samples_x, samples_y)


@njit  # type: ignore
def calc_idw_height(xi: int, yi: int, p: float) -> float:
    sum_weight = 0.0
    sum_height_weight = 0.0
    for si in range(num_samples):
        distance = np.hypot(
            grid_x[xi, xi] - samples_x[si], grid_y[yi, yi] - samples_y[si]
        )
        if distance == 0:
            return float(samples_z[si])
        weight: float = 1.0 / np.power(distance, p)
        sum_weight += weight
        sum_height_weight += samples_z[si] * weight
    return sum_height_weight / sum_weight


def est_height(p: float) -> NDArray[np.float_]:
    global est_z
    est_z = np.zeros_like(grid_x)
    for xi in range(num_intervals):
        for yi in range(num_intervals):
            est_z[xi, yi] = calc_idw_height(xi, yi, p)
    return est_z


def calc_rmsd(p: float) -> NDArray[np.float_]:
    sum_errors = 0.0
    for xi in range(num_intervals):
        for yi in range(num_intervals):
            act: float = grid_z[xi, yi]
            est: float = calc_idw_height(xi, yi, p)
            sum_errors += (act - est) ** 2
    rmsd = np.sqrt(sum_errors / num_samples**2)
    return np.array(rmsd, dtype=np.float_)


def plot(ax: Axes) -> None:
    p: NDArray[np.float_] = np.linspace(1.0, 9.0, 50)
    calc_rmsd_vec = np.vectorize(calc_rmsd)
    rmsd = calc_rmsd_vec(p)

    min_rmsd: int = np.amin(rmsd)
    best_p: float = p[np.argmin(rmsd)]

    ax.plot(p, rmsd)
    ax.scatter(best_p, min_rmsd, color="red")

    ax.set_title("Inverse Distance Weighting (p vs RMSD)")
    ax.set_xlabel("p (Power) term")
    ax.set_ylabel("RMSD (Act vs. Est)")

    ax.text(5.0, 3.0, f"best p = {best_p:.4f}", ha="left")


def main() -> None:
    init_samples()

    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
