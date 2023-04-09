#!/usr/bin/env python3
"""idw.py"""

from __future__ import annotations

import typing

import numpy as np
import mayavi.mlab as mlab  # type: ignore
from numba import njit  # type: ignore

if typing.TYPE_CHECKING:
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


def plot(idw_plot_type: int) -> None:
    if idw_plot_type == 1:
        mlab.surf(grid_x, grid_y, grid_z, colormap="ocean")  # type: ignore

    if idw_plot_type == 2:
        mlab.surf(grid_x, grid_y, est_z, colormap="ocean")  # type: ignore

    # fmt: off
    if idw_plot_type == 3:
        mlab.surf(grid_x, grid_y, grid_z, # type: ignore
                  colormap="Blues", representation="wireframe")

        mlab.surf(grid_x, grid_y, est_z, # type: ignore
                  colormap="Reds", representation="wireframe")

    if idw_plot_type == 1 or idw_plot_type == 2:
        mlab.points3d(samples_x, samples_y, samples_z, # type: ignore
                      scale_factor=3, color=(1, 0, 0))
    #fmt: off        

    mlab.show()  # type: ignore


def main() -> None:
    init_samples()
    # TODO: Adjust the p (power) value in the following line
    est_height(p=2)
    # TODO: Change the plot type (1,2,3) in the following line
    plot(idw_plot_type=1)


if __name__ == "__main__":
    main()
