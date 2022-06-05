#!/usr/bin/env python3
# euler_line.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def radline_y(rl, x):
    theta, d = rl
    return (d - x * np.cos(theta)) / np.sin(theta)


def radline_connect(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    # Prevent divide by zero due to a vertical line
    if y2 == y1:
        theta = np.pi / 4
    else:
        theta = np.arctan((x1 - x2) / (y2 - y1))
        # Ensure theta remains within the interval [0, pi)
        if theta < 0:
            theta += np.pi
    d = x1 * np.cos(theta) + y1 * np.sin(theta)
    return (theta, d)


def radline_tangent(rl, pt):
    theta, d = rl
    # Rotate radon line by 90 degrees, while ensuring
    # theta remains within the interval [0, pi)
    if theta < np.pi / 2:
        theta += np.pi / 2
    else:
        theta -= np.pi / 2
    x, y = pt
    d = x * np.cos(theta) + y * np.sin(theta)
    return (theta, d)


def radline_intersect(rl1, rl2):
    theta1, d1 = rl1
    theta2, d2 = rl2
    # If two radon lines have the same theta, then
    # they are parallel and can never intersect
    if theta1 == theta2:
        return np.nan, np.nan
    z = np.sin(theta2 - theta1)
    x = (d1 * np.sin(theta2) - d2 * np.sin(theta1)) / z
    y = (d2 * np.cos(theta1) - d1 * np.cos(theta2)) / z
    return x, y


def plot_triangle(ax):
    # Generate three random vertices
    global ptA, ptB, ptC
    ptA = np.random.uniform(-10, 10, 2)
    ptB = np.random.uniform(-10, 10, 2)
    ptC = np.random.uniform(-10, 10, 2)

    # Formulate the radon line connecting the adjacent vertices
    global rlAB, rlAC, rlBC
    rlAB = radline_connect(ptA, ptB)
    rlAC = radline_connect(ptA, ptC)
    rlBC = radline_connect(ptB, ptC)

    # Plot the edges
    x = np.linspace(ptA[0], ptB[0], 100)
    ax.plot(x, radline_y(rlAB, x), color="purple", linewidth=3, label="Edges")
    x = np.linspace(ptA[0], ptC[0], 100)
    ax.plot(x, radline_y(rlAC, x), color="purple", linewidth=3)
    x = np.linspace(ptB[0], ptC[0], 100)
    ax.plot(x, radline_y(rlBC, x), color="purple", linewidth=3)

    # Plot the extended edges
    x = np.linspace(-100, 100, 100)
    ax.plot(x, radline_y(rlAB, x), color="purple", linestyle="dotted")
    ax.plot(x, radline_y(rlAC, x), color="purple", linestyle="dotted")
    ax.plot(x, radline_y(rlBC, x), color="purple", linestyle="dotted")

    # Calculate the centroid, which is the mean value
    # of the cartesian coordinates of every vertex
    ptCentroid = (ptA + ptB + ptC) / 3

    # Plot the centroid point
    marker_size = 100 * ((72 / ax.figure.dpi) ** 2)
    ax.scatter(
        ptCentroid[0], ptCentroid[1], color="black", s=marker_size, label="Centroid"
    )


def plot_orthocenter(ax):
    # Formulate the radon lines describing each altitude, which is a line
    # extending from each vertex that is perpendicular to the opposite edge
    rlA_alt = radline_tangent(rlBC, ptA)
    rlB_alt = radline_tangent(rlAC, ptB)
    rlC_alt = radline_tangent(rlAB, ptC)

    # Plot the altitudes
    x = np.linspace(-100, 100, 100)
    ax.plot(
        x, radline_y(rlA_alt, x), color="blue", linestyle="dotted", label="Altitudes"
    )
    ax.plot(x, radline_y(rlB_alt, x), color="blue", linestyle="dotted")
    ax.plot(x, radline_y(rlC_alt, x), color="blue", linestyle="dotted")

    # Calculate the orthocenter which is the intersection of the altitudes
    global ptOrtho
    ptOrtho = radline_intersect(rlA_alt, rlB_alt)
    marker_size = 100 * ((72 / ax.figure.dpi) ** 2)

    # Plot the orthocenter point
    ax.scatter(ptOrtho[0], ptOrtho[1], color="blue", s=marker_size, label="Orthocenter")


def plot_circumcenter(ax):
    # Calculate the midpoints of each edge
    ptAB_mid = (ptA + ptB) / 2
    ptAC_mid = (ptA + ptC) / 2
    ptBC_mid = (ptB + ptC) / 2

    # Calculate the radon line that is the
    # perpendicular bisector of each edge
    rlA_bis = radline_tangent(rlBC, ptBC_mid)
    rlB_bis = radline_tangent(rlAC, ptAC_mid)
    rlC_bis = radline_tangent(rlAB, ptAB_mid)

    # Plot the perpendicular bisectors
    x = np.linspace(-100, 100, 100)
    ax.plot(
        x,
        radline_y(rlA_bis, x),
        color="green",
        linestyle="dotted",
        label="Perpendicular Bisectors",
    )
    ax.plot(x, radline_y(rlB_bis, x), color="green", linestyle="dotted")
    ax.plot(x, radline_y(rlC_bis, x), color="green", linestyle="dotted")

    # Calculate the circumcenter, which is the intersection
    # of the perpendicular bisectors for each edge
    global ptCircum
    ptCircum = radline_intersect(rlA_bis, rlB_bis)

    # Plot the circumcenter point
    marker_size = 100 * ((72 / ax.figure.dpi) ** 2)
    ax.scatter(
        ptCircum[0], ptCircum[1], color="green", s=marker_size, label="Circumcenter"
    )


def plot_euler_Line(ax):
    # Plot the Euler line, which intersects the orthocenter,
    # the circumcenter, and the centroid of every triangle
    x = np.linspace(-100, 100, 100)
    rlEuler = radline_connect(ptOrtho, ptCircum)
    ax.plot(x, radline_y(rlEuler, x), color="black", linewidth=2, label="Euler line")


def plot_incenter(ax):
    # Find the length of each edge
    dAB = np.sqrt((ptA[0] - ptB[0]) ** 2 + (ptA[1] - ptB[1]) ** 2)
    dAC = np.sqrt((ptA[0] - ptC[0]) ** 2 + (ptA[1] - ptC[1]) ** 2)
    dBC = np.sqrt((ptB[0] - ptC[0]) ** 2 + (ptB[1] - ptC[1]) ** 2)

    # Assume the angle bisectors are the sample mean of each adjacent edge
    theta_bis_a = (rlAB[0] + rlAC[0]) / 2
    d_bis_a = ptA[0] * np.cos(theta_bis_a) + ptA[1] * np.sin(theta_bis_a)
    rlA_inctr = theta_bis_a, d_bis_a

    theta_bis_b = (rlAB[0] + rlBC[0]) / 2
    d_bis_b = ptB[0] * np.cos(theta_bis_b) + ptB[1] * np.sin(theta_bis_b)
    rlB_inctr = theta_bis_b, d_bis_b

    theta_bis_c = (rlAC[0] + rlBC[0]) / 2
    d_bis_c = ptC[0] * np.cos(theta_bis_c) + ptC[1] * np.sin(theta_bis_c)
    rlC_inctr = theta_bis_c, d_bis_c

    # Find the points where the angle bisectors intersect
    ptAB = radline_intersect(rlA_inctr, rlB_inctr)
    ptAC = radline_intersect(rlA_inctr, rlC_inctr)
    ptBC = radline_intersect(rlB_inctr, rlC_inctr)

    # Find the distance between each vertex and the intersection point of
    # its own angle bisector and the angle bisector of its adjacent vertices
    dA_AB = np.sqrt((ptA[0] - ptAB[0]) ** 2 + (ptA[1] - ptAB[1]) ** 2)
    dB_AB = np.sqrt((ptB[0] - ptAB[0]) ** 2 + (ptB[1] - ptAB[1]) ** 2)
    dA_AC = np.sqrt((ptA[0] - ptAC[0]) ** 2 + (ptA[1] - ptAC[1]) ** 2)
    dC_AC = np.sqrt((ptC[0] - ptAC[0]) ** 2 + (ptC[1] - ptAC[1]) ** 2)
    dB_BC = np.sqrt((ptB[0] - ptBC[0]) ** 2 + (ptB[1] - ptBC[1]) ** 2)
    dC_BC = np.sqrt((ptC[0] - ptBC[0]) ** 2 + (ptC[1] - ptBC[1]) ** 2)

    # Rotate by 90 degrees any bisector which results in bisector intersection
    # points that fall outside the triangle, as the incenter must be in the triangle
    # If a rotation is necessary, recalculate the Radon Line for that bisector
    if dB_BC <= dBC and dC_BC <= dBC:
        theta_bis_a -= np.pi / 2
        d_bis_a = ptA[0] * np.cos(theta_bis_a) + ptA[1] * np.sin(theta_bis_a)
        rlA_inctr = theta_bis_a, d_bis_a
    elif dA_AC <= dAC and dC_AC < dAC:
        theta_bis_b -= np.pi / 2
        d_bis_b = ptB[0] * np.cos(theta_bis_b) + ptB[1] * np.sin(theta_bis_b)
        rlB_inctr = theta_bis_b, d_bis_b
    elif dA_AB < dAB and dB_AB < dAB:
        theta_bis_c -= np.pi / 2
        d_bis_c = ptC[0] * np.cos(theta_bis_c) + ptC[1] * np.sin(theta_bis_c)
        rlC_inctr = theta_bis_c, d_bis_c

    # Plot the angle bisectors of each vertex
    x = np.linspace(-100, 100, 100)
    ax.plot(
        x,
        radline_y(rlA_inctr, x),
        color="red",
        label="Angle Bisectors",
        linestyle="dotted",
    )
    ax.plot(x, radline_y(rlB_inctr, x), color="red", linestyle="dotted")
    ax.plot(x, radline_y(rlC_inctr, x), color="red", linestyle="dotted")

    # Plot the incenter, which is the intersection of the
    # angle bisectors of every vertex
    ptIncenter = radline_intersect(rlA_inctr, rlB_inctr)
    marker_size = 100 * ((72 / ax.figure.dpi) ** 2)
    ax.scatter(
        ptIncenter[0], ptIncenter[1], color="red", s=marker_size, label="Incenter"
    )


def plot(ax):
    plot_triangle(ax)
    plot_circumcenter(ax)
    plot_orthocenter(ax)
    plot_euler_Line(ax)

    # Note: the triangle incenter is falls on the
    # Euler line if and only if the triangle is isosceles
    # plot_incenter(ax)

    ax.set_title(f"Euler Line (seed={prng_seed})")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal")
    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)
    ax.legend(loc="upper right")
    ax.grid()


def main():
    seeds = (2017, 2018, 2020, 2021)
    seeds_index = 0

    global prng_seed
    prng_seed = seeds[seeds_index]
    np.random.seed(prng_seed)

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
