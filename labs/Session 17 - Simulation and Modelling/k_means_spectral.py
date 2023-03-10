#!/usr/bin/env python3
# k_means_spectral.py


import os
import sys

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.datasets import make_moons


def plot_kmeans(ax, x):
    ax.set_title("k-Means Clustering")
    k_means = KMeans(2, n_init="auto", random_state=0)
    labels = k_means.fit_predict(x)
    ax.scatter(x[:, 0], x[:, 1], c=labels, s=50, cmap="viridis")


def plot_spectral(ax, x):
    ax.set_title("Spectral Clustering")
    model = SpectralClustering(
        n_clusters=2, affinity="nearest_neighbors", assign_labels="kmeans"
    )
    labels = model.fit_predict(x)
    ax.scatter(x[:, 0], x[:, 1], c=labels, s=50, cmap="viridis")


def main():
    x, _ = make_moons(200, noise=0.05, random_state=0)

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(2, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot_kmeans(ax, x)

    ax = fig.add_subplot(gs[1, 0])
    plot_spectral(ax, x)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
