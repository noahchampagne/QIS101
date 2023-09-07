#!usr/bin/env python3
"""ladder_problem.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def find_max(
    trials: int,
) -> tuple[NDArray[np.float_], NDArray[np.float_], float, float]:
    """Returns data for the max latter length vs the angles and the max length"""
    angles: NDArray[np.float_] = np.linspace(0, np.pi / 2, trials)
    lengths: NDArray[np.float_] = np.zeros(trials)
    max_length = max_angle = np.inf  # type: ignore
    # Enumerates through angle measures 0 -> pi/2
    for i, theta in enumerate(angles):
        # Accounts for the case when the angle is 0 or pi/2
        if i == 0 or i == len(angles) - 1:
            lengths[i] = None
            continue
        dx: float = 2 / np.tan(theta)
        hypotenuse: float = 2 / np.sin(theta)
        length: float = hypotenuse * (1 + 1 / dx)
        lengths[i] = length
        # Making sure max length is only possible lengths throughout the rotation
        if length <= max_length:
            max_length = length
            max_angle = theta
    return angles, lengths, max_length, max_angle


def plot(ax: Axes) -> None:
    """Plots the angle measure vs possible length of the latter for angles 0 -> pi/2"""
    angles, lengths, max_length, max_angle = find_max(1000)  # type: ignore

    # Plots the angles vs length
    ax.plot(angles, lengths)

    # Marks the greatest possible length of the ladder and the asymptote
    ax.annotate(
        f"Max Length = ~{max_length:>.3f} m",
        xy=(max_angle, max_length),
        xytext=(max_angle, 50 * max_length),
        arrowprops={"facecolor": "black", "shrink": 0.05, "width": 0.5},
    )
    ax.hlines(max_angle, 0, np.pi / 2, color="red", linestyles="dotted")

    ax.set_title("Length of Ladder vs Angle Measure")
    ax.set_xlabel("Angles (Radians)")
    ax.set_ylabel("Length (m)")

    # Prints the max length of the ladder
    print(f"Max Possible Ladder Length = {max_length:>.3f} m")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
