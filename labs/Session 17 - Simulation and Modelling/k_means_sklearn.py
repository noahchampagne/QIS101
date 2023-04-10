#!/usr/bin/env python3
"""k_means_sklearn.py"""

from __future__ import annotations

import typing
import os
import sys

import numpy as np
from matplotlib.markers import MarkerStyle
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

K_CLUSTERS: int = 3


def plot(ax: Axes) -> None:
    ax.set_title(f"k-Means Clustering (k={K_CLUSTERS})")
    ax.set_xlim(-5, 45)
    ax.set_ylim(-5, 45)
    ax.set_aspect("equal")

    file_name: str = os.path.dirname(sys.argv[0]) + "/cluster_samples.csv"
    points: NDArray[np.float_] = np.genfromtxt(file_name, delimiter=",")
    points = points[:-1, :]

    np.random.seed(2016)
    kmeans = KMeans(K_CLUSTERS)
    kmeans.fit(points)

    y_kmeans: NDArray[np.float_] = kmeans.predict(points)
    ax.scatter(points[:, 0], points[:, 1], c=y_kmeans)

    centers: NDArray[np.float_] = kmeans.cluster_centers_
    ax.scatter(centers[:, 0], centers[:, 1], c="black", marker=MarkerStyle("s"))


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
