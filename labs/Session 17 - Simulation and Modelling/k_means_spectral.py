#!/usr/bin/env python3
"""k_means_spectral.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.datasets import make_moons  # type: ignore

if typing.TYPE_CHECKING:
    import numpy as np
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot_kmeans(ax: Axes, x: NDArray[np.float_]) -> None:
    ax.set_title("k-Means Clustering")
    k_means = KMeans(2, n_init="auto", random_state=0)
    labels: NDArray[np.int_] = k_means.fit_predict(x)
    ax.scatter(x[:, 0], x[:, 1], c=labels, s=50, cmap="viridis")


def plot_spectral(ax: Axes, x: NDArray[np.float_]) -> None:
    ax.set_title("Spectral Clustering")
    model = SpectralClustering(
        n_clusters=2, affinity="nearest_neighbors", assign_labels="kmeans"
    )
    labels: NDArray[np.int_] = model.fit_predict(x)
    ax.scatter(x[:, 0], x[:, 1], c=labels, s=50, cmap="viridis")


def main() -> None:
    x: NDArray[np.float_] = make_moons(200, noise=0.05, random_state=0)[0]

    plt.figure(__file__, constrained_layout=True)
    plot_kmeans(plt.subplot(211), x)
    plot_spectral(plt.subplot(212), x)
    plt.show()


if __name__ == "__main__":
    main()
