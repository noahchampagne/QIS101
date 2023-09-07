#!/usr/bin.env python3
"""benfords_law.py"""

from __future__ import annotations

import random
import typing
import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def law() -> NDArray[np.float_]:
    """Estimates the probabilities of each digit being the first digit of large numbers"""
    trials: int = 100_000
    # Keeps track of each digit's frequency
    prob: NDArray[np.float_] = np.zeros(9)
    # Runs through all the trials with various random large numbers
    for _ in range(trials):
        num: int = random.randint(1, 1_000_000) ** 100
        first: int = num // (10 ** int(math.log(num, 10)))
        # Deals with the inadequacy of the log function
        if first == 10:
            prob[0] += 1
        else:
            prob[first - 1] += 1
    return prob / trials


def plot(ax: Axes) -> None:
    """Plots the probability of each digit appearing as the MSD"""
    # Gets the probabilities from Benford's function
    prob: NDArray[np.float_] = law()

    # Plot the graph on the main axes
    plt.bar(range(1, 10), prob)

    # Sets the equation title for the graph and labels the axes
    ax.set_title("Benford's Law of Anomalous Numbers")
    ax.set_xlabel("Digit")
    ax.set_ylabel("Probability")

    ax.xaxis.set_major_locator(MultipleLocator(1))


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
