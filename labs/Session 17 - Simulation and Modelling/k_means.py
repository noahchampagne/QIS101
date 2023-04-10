#!/usr/bin/env python3
"""k_means.py"""

from __future__ import annotations

import typing
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.markers import MarkerStyle
from pathlib import Path

if typing.TYPE_CHECKING:
    from typing import Any

    from matplotlib.axes import Axes
    from numpy.typing import NDArray

K_CLUSTERS: int = 3
INCLUDE_OUTLIERS: bool = False
MEAN_MULTIPLE: int = 0

COLMAP: tuple[str, ...] = ("red", "blue", "green", "purple", "yellow", "orange")


@dataclass
class DataPoint:
    x: float = 0.0
    y: float = 0.0
    cluster: Any = None


@dataclass
class Cluster:
    index: int = 0
    color: str = ""
    x: float = 0.0
    y: float = 0.0
    population: int = 0
    mean_distance: float = 0.0


def init_clusters(k: int) -> list[Cluster]:
    clusters: list[Cluster] = [Cluster(index=i, color=COLMAP[i]) for i in range(k)]
    return clusters


def init_points(data_file: Path) -> list[DataPoint]:
    samples: NDArray[np.float_] = np.genfromtxt(data_file, delimiter=",")
    points: list[DataPoint] = []
    for s in samples:
        point = DataPoint(s[0], s[1])
        points.append(point)
    return points


def init_assign(points: list[DataPoint], clusters: list[Cluster]) -> None:
    k: int = len(clusters)
    for idx, p in enumerate(points):
        c: Cluster = clusters[idx % k]
        p.cluster = c
        c.population += 1


def reassign(points: list[DataPoint], clusters: list[Cluster]) -> bool:
    # Phase I: Calculate the new geometric mean of each
    # cluster based upon current data point assignments
    converged = True
    c: Cluster
    for c in clusters:
        new_x: float = 0.0
        new_y: float = 0.0
        for p in points:
            if p.cluster == c:
                new_x += p.x
                new_y += p.y
        new_x /= c.population
        new_y /= c.population

        if c.x != new_x or c.y != new_y:
            c.x, c.y = new_x, new_y
            converged = False

    # Phase II: Assign data points to nearest cluster
    for p in points:
        dist_min: np.float64 = np.finfo(np.float64).max
        nearest_cluster: Cluster = Cluster()
        for c in clusters:
            dist = np.hypot(p.x - c.x, p.y - c.y)
            if dist < dist_min:
                dist_min = dist
                nearest_cluster = c
        if nearest_cluster != p.cluster and p.cluster.population > 1:
            p.cluster.population -= 1
            p.cluster = nearest_cluster
            p.cluster.population += 1
            converged = False

    # Phase III - Evict any point too far away from its cluster's center
    if converged and MEAN_MULTIPLE > 0:
        # Calculate mean distance from each cluster's center
        # to the assigned points for that cluster
        for c in clusters:
            total_distance = 0.0
            for p in points:
                if p.cluster == c:
                    total_distance += np.hypot(p.x - c.x, p.y - c.y)
            c.mean_distance = total_distance / c.population

        # Only keep points where the distance to its assigned cluster's
        # center is less than a multiple of that cluster's mean distance
        # to its assigned points
        new_points: list[DataPoint] = []
        for p in points:
            c = p.cluster
            dist = np.hypot(p.x - c.x, p.y - c.y)
            if dist < c.mean_distance * MEAN_MULTIPLE:
                new_points.append(p)
            else:
                if c.population > 1:
                    print(f"Evicted DataPoint({p.x}, {p.y}) from Cluster {c.index}")
                    c.population -= 1
                    converged = False
        points[:] = new_points

    return converged


def plot(ax: Axes, points: list[DataPoint], clusters: list[Cluster]) -> None:
    ax.set_aspect("equal")
    ax.set_xlim(-5, 45)
    ax.set_ylim(-5, 45)
    ax.set_title(f"k-Means Clustering (k={K_CLUSTERS})")

    for p in points:
        ax.scatter(p.x, p.y, color=p.cluster.color, alpha=0.5, edgecolor="black")

    for c in clusters:
        ax.scatter(c.x, c.y, color=c.color, marker=MarkerStyle("s"))


def on_key_press(  # type: ignore
    event,  # type: ignore
    ax: Axes,
    points: list[DataPoint],
    clusters: list[Cluster],  # type: ignore
) -> None:
    if event.key == "n":
        if reassign(points, clusters):
            print("Cluster has converged!")
        ax.clear()
        plot(ax, points, clusters)
        plt.draw()


def main() -> None:
    plt.figure(__file__)

    ax: Axes = plt.axes()

    plt.gcf().canvas.mpl_connect(
        "key_press_event",
        lambda event: on_key_press(event, ax, points, clusters),  # type: ignore
    )

    clusters: list[Cluster] = init_clusters(K_CLUSTERS)

    data_file: Path = Path(__file__).parent.joinpath("cluster_samples.csv")
    points: list[DataPoint] = init_points(data_file)

    if not INCLUDE_OUTLIERS:
        points.pop()

    init_assign(points, clusters)

    plot(ax, points, clusters)

    plt.show()


if __name__ == "__main__":
    main()
