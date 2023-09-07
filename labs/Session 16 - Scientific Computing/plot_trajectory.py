#!/usr/bin/env/python 3
"""plot_trajectory.py"""

from __future__ import annotations

import os
import sys
import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def load_trajectory(file_name: str) -> NDArray[np.float_]:
    """Returns a np array of the information from the inputted file"""
    ray: NDArray[np.float_] = np.genfromtxt(file_name, delimiter=",", dtype=float)
    return ray


def plot(ax: Axes, ray: NDArray[np.float_]) -> None:
    """Plots the ray as a function of height and time"""
    # Slices the array to gain a separate time and height array
    times: NDArray[np.float_] = ray[:, 0]
    heights: NDArray[np.float_] = ray[:, 1]

    # Plots the ray
    ax.plot(times, heights, linewidth=4)
    ax.set_title("Cosmic Ray Height vs. Time")
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Height (cm)")

    # Generates the line of best fit and plots it alongside the ray
    slope, intercept = np.polyfit(times, heights, 1)  # type: ignore
    ax.plot(times, slope * times + intercept, color="red", linestyle="--", linewidth=2)

    # Finds the initial height of the array and prints it
    init_height: float = -slope * 174300 + intercept
    print(f"The initial height was {init_height} cm or {init_height / 100000} km")


def main() -> None:
    # Obtain the file name and use the load_trajectory fn to make the information from the file into a np array
    file_name: str = os.path.dirname(sys.argv[0]) + "/ray.csv"
    ray: NDArray[np.float_] = load_trajectory(file_name)
    plt.figure(__file__)
    plot(plt.axes(), ray)
    plt.show()


if __name__ == "__main__":
    main()
