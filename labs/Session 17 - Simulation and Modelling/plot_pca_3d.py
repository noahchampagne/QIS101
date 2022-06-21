#!/usr/bin/env python3
# plot_pca_3d.py

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import os
import sys


def pdf(x):
    return 0.5 * (
        stats.norm(scale=0.25 / np.e).pdf(x) + stats.norm(scale=4 / np.e).pdf(x)
    )


def plot():
    x = np.random.normal(scale=0.5, size=(30000))
    y = np.random.normal(scale=0.5, size=(30000))
    z = np.random.normal(scale=0.1, size=len(x))

    density = pdf(x) * pdf(y)
    pdf_z = pdf(5 * z)

    density *= pdf_z

    a = x + y
    b = 2 * y
    c = a - b + z

    norm = np.sqrt(a.var() + b.var())
    a /= norm
    b /= norm

    elev = -40
    azim = -80
    ax = Axes3D(plt.gcf(), rect=[0, 0, 0.95, 1], elev=elev, azim=azim)

    ax.scatter(a[::10], b[::10], c[::10], c=density[::10], marker="+", alpha=0.4)

    Y = np.c_[a, b, c]
    pca = PCA(n_components=3)
    pca.fit(Y)

    V = pca.components_.T
    x_pca_axis, y_pca_axis, z_pca_axis = 3 * V

    x_pca_plane = np.r_[x_pca_axis[:2], -x_pca_axis[1::-1]]
    y_pca_plane = np.r_[y_pca_axis[:2], -y_pca_axis[1::-1]]
    z_pca_plane = np.r_[z_pca_axis[:2], -z_pca_axis[1::-1]]
    x_pca_plane.shape = (2, 2)
    y_pca_plane.shape = (2, 2)
    z_pca_plane.shape = (2, 2)

    # ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane)


def main():
    np.random.seed(4)
    plt.figure(os.path.basename(sys.argv[0]))
    plot()
    plt.show()


if __name__ == "__main__":
    main()
