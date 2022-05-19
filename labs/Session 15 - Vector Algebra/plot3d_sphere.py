#!/usr/bin/env python3
# plot3d_sphere.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def plot(ax):
    u = np.linspace(0, np.pi, 30)  # poloidal angle
    v = np.linspace(0, 2 * np.pi, 30)  # toroidal angle

    x = np.outer(np.sin(u), np.sin(v))
    y = np.outer(np.sin(u), np.cos(v))
    z = np.outer(np.cos(u), np.ones_like(v))

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # TODO: Uncomment the following lines one-by-one
    ax.scatter(x, y, z)
    # ax.plot_wireframe(x, y, z)
    # ax.plot_surface(x, y, z)


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
