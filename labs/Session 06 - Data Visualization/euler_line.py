#!/usr/bin/env python3
"""euler_line.py"""

from __future__ import annotations

import typing
from dataclasses import dataclass
from random import randint, seed

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


@dataclass
class Point2D:
    x: float
    y: float


@dataclass
class RadLine:
    theta: float
    d: float


# Initialize global variables
ptA: Point2D = Point2D(x=0.0, y=0.0)
ptB: Point2D = Point2D(x=0.0, y=0.0)
ptC: Point2D = Point2D(x=0.0, y=0.0)
ptOrtho: Point2D = Point2D(x=0.0, y=0.0)
ptCircum: Point2D = Point2D(x=0.0, y=0.0)

rlineAB: RadLine = RadLine(theta=0.0, d=0.0)
rlineAC: RadLine = RadLine(theta=0.0, d=0.0)
rlineBC: RadLine = RadLine(theta=0.0, d=0.0)

prng_seed: int = 2018


def radline_y(rline: RadLine, x: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.array(
        (rline.d - x * np.cos(rline.theta)) / np.sin(rline.theta), np.float_
    )


def radline_connect(pt1: Point2D, pt2: Point2D) -> RadLine:
    # Prevent divide by zero due to a vertical line
    theta: float
    if pt2.y == pt1.y:
        theta = np.pi / 4
    else:
        theta = np.arctan((pt1.x - pt2.x) / (pt2.y - pt1.y))
        # Ensure theta remains within the interval [0, pi)
        if theta < 0:
            theta += np.pi
    d: float = pt1.x * np.cos(theta) + pt1.y * np.sin(theta)
    return RadLine(theta, d)


def radline_tangent(rline: RadLine, pt: Point2D) -> RadLine:
    theta: float = rline.theta
    d: float = rline.d
    # Rotate radon line by 90 degrees, while ensuring
    # theta remains within the interval [0, pi)
    if theta < np.pi / 2:
        theta += np.pi / 2
    else:
        theta -= np.pi / 2
    d = pt.x * np.cos(theta) + pt.y * np.sin(theta)
    return RadLine(theta, d)


def radline_intersect(rline1: RadLine, rline2: RadLine) -> Point2D:
    theta1: float = rline1.theta
    d1: float = rline1.d
    theta2: float = rline2.theta
    d2: float = rline2.d
    # If two radon lines have the same theta, then
    # they are parallel and can never intersect
    if theta1 == theta2:
        return Point2D(np.nan, np.nan)
    z: float = float(np.sin(theta2 - theta1))
    x: float = float((d1 * np.sin(theta2) - d2 * np.sin(theta1)) / z)
    y: float = float((d2 * np.cos(theta1) - d1 * np.cos(theta2)) / z)
    return Point2D(x, y)


def random_pt() -> Point2D:
    x: int = randint(-10, 10)
    y: int = randint(-10, 10)
    return Point2D(x, y)


def plot_triangle(ax: Axes) -> None:
    # Generate three random vertices
    global ptA, ptB, ptC
    ptA = random_pt()
    ptB = random_pt()
    ptC = random_pt()

    # Formulate the radon line connecting the adjacent vertices
    global rlineAB, rlineAC, rlineBC
    rlineAB = radline_connect(ptA, ptB)
    rlineAC = radline_connect(ptA, ptC)
    rlineBC = radline_connect(ptB, ptC)

    # Plot the edges
    x: NDArray[np.float_] = np.linspace(ptA.x, ptB.x, 100, dtype=np.float_)
    ax.plot(x, radline_y(rlineAB, x), color="purple", linewidth=3, label="Edges")
    x = np.linspace(ptA.x, ptC.x, 100, dtype=np.float_)
    ax.plot(x, radline_y(rlineAC, x), color="purple", linewidth=3)
    x = np.linspace(ptB.x, ptC.x, 100, dtype=np.float_)
    ax.plot(x, radline_y(rlineBC, x), color="purple", linewidth=3)

    # Plot the extended edges
    x = np.linspace(-100, 100, 100)
    ax.plot(x, radline_y(rlineAB, x), color="purple", linestyle="dotted")
    ax.plot(x, radline_y(rlineAC, x), color="purple", linestyle="dotted")
    ax.plot(x, radline_y(rlineBC, x), color="purple", linestyle="dotted")

    # Calculate the centroid, which is the mean value
    # of the cartesian coordinates of every vertex
    ptCentroid: Point2D = Point2D(
        x=(ptA.x + ptB.x + ptC.x) / 3.0, y=(ptA.y + ptB.y + ptC.y) / 3.0
    )

    # Plot the centroid point
    marker_size: float = 100 * ((72 / ax.figure.dpi) ** 2)  # type: ignore
    ax.scatter(
        ptCentroid.x, ptCentroid.y, color="purple", s=marker_size, label="Centroid"
    )


def plot_orthocenter(ax: Axes) -> None:
    # Formulate the radon lines describing each altitude, which is a line
    # extending from each vertex that is perpendicular to the opposite edge
    rlineA_alt: RadLine = radline_tangent(rlineBC, ptA)
    rlineB_alt: RadLine = radline_tangent(rlineAC, ptB)
    rlineC_alt: RadLine = radline_tangent(rlineAB, ptC)

    # Plot the altitudes
    x: NDArray[np.float_] = np.linspace(-100, 100, 100, dtype=np.float_)
    ax.plot(
        x, radline_y(rlineA_alt, x), color="blue", linestyle="dotted", label="Altitudes"
    )
    ax.plot(x, radline_y(rlineB_alt, x), color="blue", linestyle="dotted")
    ax.plot(x, radline_y(rlineC_alt, x), color="blue", linestyle="dotted")

    # Calculate the orthocenter which is the intersection of the altitudes
    global ptOrtho
    ptOrtho = radline_intersect(rlineA_alt, rlineB_alt)
    marker_size: float = 100 * ((72 / ax.figure.dpi) ** 2)  # type: ignore

    # Plot the orthocenter point
    ax.scatter(ptOrtho.x, ptOrtho.y, color="blue", s=marker_size, label="Orthocenter")


def plot_circumcenter(ax: Axes) -> None:
    # Calculate the midpoints of each edge
    ptAB_mid: Point2D = Point2D(x=(ptA.x + ptB.x) / 2.0, y=(ptA.y + ptB.y) / 2.0)
    ptAC_mid: Point2D = Point2D(x=(ptA.x + ptC.x) / 2.0, y=(ptA.y + ptC.y) / 2.0)
    ptBC_mid: Point2D = Point2D(x=(ptB.x + ptC.x) / 2.0, y=(ptB.y + ptC.y) / 2.0)

    # Calculate the radon line that is the
    # perpendicular bisector of each edge
    rlineA_bis: RadLine = radline_tangent(rlineBC, ptBC_mid)
    rlineB_bis: RadLine = radline_tangent(rlineAC, ptAC_mid)
    rlineC_bis: RadLine = radline_tangent(rlineAB, ptAB_mid)

    # Plot the perpendicular bisectors
    x: NDArray[np.float_] = np.linspace(-100, 100, 100, dtype=np.float_)
    ax.plot(
        x,
        radline_y(rlineA_bis, x),
        color="green",
        linestyle="dotted",
        label="Perpendicular Bisectors",
    )
    ax.plot(x, radline_y(rlineB_bis, x), color="green", linestyle="dotted")
    ax.plot(x, radline_y(rlineC_bis, x), color="green", linestyle="dotted")

    # Calculate the circumcenter, which is the intersection
    # of the perpendicular bisectors for each edge
    global ptCircum
    ptCircum = radline_intersect(rlineA_bis, rlineB_bis)

    # Plot the circumcenter point
    marker_size: float = 100 * ((72 / ax.figure.dpi) ** 2)  # type: ignore
    ax.scatter(
        ptCircum.x, ptCircum.y, color="green", s=marker_size, label="Circumcenter"
    )


def plot_euler_Line(ax: Axes) -> None:
    # Plot the Euler line, which intersects the orthocenter,
    # the circumcenter, and the centroid of every triangle
    x: NDArray[np.float_] = np.linspace(-100, 100, 100, dtype=np.float_)
    rlineEuler: RadLine = radline_connect(ptOrtho, ptCircum)
    ax.plot(x, radline_y(rlineEuler, x), color="black", linewidth=3, label="Euler line")


def plot_incenter(ax: Axes) -> None:
    # Find the length of each edge
    dAB: float = np.sqrt((ptA.x - ptB.x) ** 2 + (ptA.y - ptB.y) ** 2)
    dAC: float = np.sqrt((ptA.x - ptC.x) ** 2 + (ptA.y - ptC.y) ** 2)
    dBC: float = np.sqrt((ptB.x - ptC.x) ** 2 + (ptB.y - ptC.y) ** 2)

    # Assume the angle bisectors are the sample mean of each adjacent edge
    theta_bis_a: float = (rlineAB.theta + rlineAC.theta) / 2.0
    d_bis_a: float = ptA.x * np.cos(theta_bis_a) + ptA.y * np.sin(theta_bis_a)
    rlineA_inctr: RadLine = RadLine(theta_bis_a, d_bis_a)

    theta_bis_b: float = (rlineAB.theta + rlineBC.theta) / 2.0
    d_bis_b: float = ptB.x * np.cos(theta_bis_b) + ptB.y * np.sin(theta_bis_b)
    rlineB_inctr: RadLine = RadLine(theta_bis_b, d_bis_b)

    theta_bis_c: float = (rlineAC.theta + rlineBC.theta) / 2.0
    d_bis_c: float = ptC.x * np.cos(theta_bis_c) + ptC.y * np.sin(theta_bis_c)
    rlineC_inctr: RadLine = RadLine(theta_bis_c, d_bis_c)

    # Find the points where the angle bisectors intersect
    ptAB: Point2D = radline_intersect(rlineA_inctr, rlineB_inctr)
    ptAC: Point2D = radline_intersect(rlineA_inctr, rlineC_inctr)
    ptBC: Point2D = radline_intersect(rlineB_inctr, rlineC_inctr)

    # Find the distance between each vertex and the intersection point of
    # its own angle bisector and the angle bisector of its adjacent vertices
    dA_AB: float = np.sqrt((ptA.x - ptAB.x) ** 2 + (ptA.y - ptAB.y) ** 2)
    dB_AB: float = np.sqrt((ptB.x - ptAB.x) ** 2 + (ptB.y - ptAB.y) ** 2)
    dA_AC: float = np.sqrt((ptA.x - ptAC.x) ** 2 + (ptA.y - ptAC.y) ** 2)
    dC_AC: float = np.sqrt((ptC.x - ptAC.x) ** 2 + (ptC.y - ptAC.y) ** 2)
    dB_BC: float = np.sqrt((ptB.x - ptBC.x) ** 2 + (ptB.y - ptBC.y) ** 2)
    dC_BC: float = np.sqrt((ptC.x - ptBC.x) ** 2 + (ptC.y - ptBC.y) ** 2)

    # Rotate by 90 degrees any bisector which results in bisector intersection
    # points that fall outside the triangle, as the incenter must be in the triangle
    # If a rotation is necessary, recalculate the Radon Line for that bisector
    if dB_BC <= dBC and dC_BC <= dBC:
        theta_bis_a -= np.pi / 2
        d_bis_a = ptA.x * np.cos(theta_bis_a) + ptA.y * np.sin(theta_bis_a)
        rlineA_inctr = RadLine(theta_bis_a, d_bis_a)
    elif dA_AC <= dAC and dC_AC < dAC:
        theta_bis_b -= np.pi / 2
        d_bis_b = ptB.x * np.cos(theta_bis_b) + ptB.y * np.sin(theta_bis_b)
        rlineB_inctr = RadLine(theta_bis_b, d_bis_b)
    elif dA_AB < dAB and dB_AB < dAB:
        theta_bis_c -= np.pi / 2
        d_bis_c = ptC.x * np.cos(theta_bis_c) + ptC.y * np.sin(theta_bis_c)
        rlineC_inctr = RadLine(theta_bis_c, d_bis_c)

    # Plot the angle bisectors of each vertex
    x: NDArray[np.float_] = np.linspace(-100, 100, 100, dtype=np.float_)
    ax.plot(
        x,
        radline_y(rlineA_inctr, x),
        color="red",
        label="Angle Bisectors",
        linestyle="dotted",
    )
    ax.plot(x, radline_y(rlineB_inctr, x), color="red", linestyle="dotted")
    ax.plot(x, radline_y(rlineC_inctr, x), color="red", linestyle="dotted")

    # Plot the incenter, which is the intersection of the
    # angle bisectors of every vertex
    ptIncenter: Point2D = radline_intersect(rlineA_inctr, rlineB_inctr)
    marker_size: float = 100 * ((72 / ax.figure.dpi) ** 2)  # type: ignore
    ax.scatter(ptIncenter.x, ptIncenter.y, color="red", s=marker_size, label="Incenter")


def plot(ax: plt.Axes) -> None:
    plot_triangle(ax)
    plot_circumcenter(ax)
    plot_orthocenter(ax)
    plot_euler_Line(ax)

    # Note: the triangle incenter is falls on the Euler Line
    # if and only if the triangle is isosceles
    # plot_incenter(ax)

    ax.set_title(f"Euler Line (seed={prng_seed})")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal")
    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)
    ax.legend(loc="upper right")
    ax.grid()


def main() -> None:
    seed(prng_seed)

    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
