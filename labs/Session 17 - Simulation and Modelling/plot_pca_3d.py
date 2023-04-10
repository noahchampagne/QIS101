#!/usr/bin/env python3
"""plot_pca_3d.py"""


from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.markers import MarkerStyle
from scipy import stats
from sklearn.decomposition import PCA

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def pdf(x: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.array(
        (
            stats.norm(scale=0.25 / np.e).pdf(x)
            + stats.norm(scale=4 / np.e).pdf(x)  # type: ignore
        )
        * 0.5
    )


def main() -> None:
    np.random.seed(4)
    x: NDArray[np.float_] = np.random.normal(scale=0.5, size=(30000))
    y: NDArray[np.float_] = np.random.normal(scale=0.5, size=(30000))
    z: NDArray[np.float_] = np.random.normal(scale=0.1, size=len(x))

    density: NDArray[np.float_] = pdf(x) * pdf(y)
    pdf_z: NDArray[np.float_] = pdf(5 * z)

    density *= pdf_z

    a: NDArray[np.float_] = x + y
    b: NDArray[np.float_] = 2 * y
    c: NDArray[np.float_] = a - b + z

    norm = np.sqrt(a.var() + b.var())
    a /= norm
    b /= norm

    plt.figure(__file__)
    ax: Axes = plt.axes(projection="3d", elev=-40, azim=-80)

    # Draw every 10th point
    ax.scatter(
        a[::10], b[::10], c[::10], c=density[::10], marker=MarkerStyle("+"), alpha=0.4
    )

    # Translates slice objects to concatenation along the second axis.
    Y: NDArray[np.float_] = np.c_[a, b, c]
    pca = PCA(n_components=3)
    pca.fit(Y)

    V: NDArray[np.float_] = pca.components_.T
    x_pca_axis: NDArray[np.float_]
    y_pca_axis: NDArray[np.float_]
    z_pca_axis: NDArray[np.float_]
    x_pca_axis, y_pca_axis, z_pca_axis = 3 * V

    x_pca_plane: NDArray[np.float_]
    y_pca_plane: NDArray[np.float_]
    z_pca_plane: NDArray[np.float_]

    x_pca_plane = np.r_[x_pca_axis[:2], -x_pca_axis[1::-1]]
    y_pca_plane = np.r_[y_pca_axis[:2], -y_pca_axis[1::-1]]
    z_pca_plane = np.r_[z_pca_axis[:2], -z_pca_axis[1::-1]]
    x_pca_plane.shape = (2, 2)
    y_pca_plane.shape = (2, 2)
    z_pca_plane.shape = (2, 2)

    # ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane) # type: ignore

    plt.show()


if __name__ == "__main__":
    main()
