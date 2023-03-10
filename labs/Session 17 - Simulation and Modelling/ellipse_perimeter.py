#!/usr/bin/env python3
# ellipse_perimeter.py

import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def d_s(theta, a, b):
    return np.sqrt(np.power(a * np.sin(theta), 2) + np.power(b * np.cos(theta), 2))


def ramanujan_estimate(a, b):
    h = (a - b) / (a + b)
    return (a + b) * (1 + 3 * h / (10 + np.sqrt(4 - 3 * h))) * np.pi


def fit_quadratic(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)  # Make a column vector
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(vec_x)
    vec_x_ = transformer.transform(vec_x)
    lr = LinearRegression()
    model = lr.fit(vec_x_, vec_y)
    b, a = model.coef_
    c = model.intercept_
    return a, b, c


def plot_p(ax, p, r):
    ax.plot(range(len(p)), p, label="Integral")
    ax.plot(range(len(r)), r, label="Ramanujan")
    ax.set_title("Numerical Ellipse Perimeter Estimate")
    ax.set_xlabel("b")
    ax.set_ylabel("Perimeter")
    ax.legend(loc="best")
    ax.set_xlim(1, len(p) - 1)


def plot_err(ax, e):
    ax.scatter(range(len(e)), e, color="red")
    ax.set_title("Ramanujan's Estimate Relative Error")
    ax.set_xlabel("b")
    ax.set_ylabel("Relative Error")
    ax.set_xlim(1, len(e) - 1)


def plot_fit(ax, e, fa, fb, fc):
    ax.scatter(range(len(e)), e, color="red")
    x = np.linspace(0, len(e) - 1, 500)
    ax.plot(x, fa * x**2 + fb * x + fc)
    ax.set_title("Ramanujan's Error (Quadratic Fit)")
    ax.set_xlabel("b")
    ax.set_ylabel("Relative Error")
    ax.set_xlim(1, len(e) - 1)


def plot_fix(ax, p, f):
    ax.plot(range(len(p)), p, label="Integral")
    ax.plot(range(len(f)), f, label="Adjusted")
    ax.set_title("Ramanujan's Perimeter Estimate (Adjusted)")
    ax.set_xlabel("b")
    ax.set_ylabel("Perimeter")
    ax.legend(loc="best")
    ax.set_xlim(1, len(f) - 1)


def main():
    a = 100
    peri, ram, err, adj = np.zeros(21), np.zeros(21), np.zeros(21), np.zeros(21)

    for b, _ in enumerate(peri):
        peri[b] = scipy.integrate.quad(d_s, 0, 2 * np.pi, args=(a, b))[0]
        ram[b] = ramanujan_estimate(a, b)
        err[b] = np.abs((ram[b] - peri[b]) / ram[b])

    fit_a, fit_b, fit_c = fit_quadratic(np.arange(len(err)), err)
    print("Quadratic Error Adjuster:")
    print(f"{fit_a:.5f}x^2 + {fit_b:.5f}x + {fit_c:.5f}")

    print(f"{'b':>3}{'Perimeter':>10}{'Ramanujan':>11}{'Error':>10}{'Adjusted':>10}")
    for b, _ in enumerate(peri):
        adj[b] = ram[b] - ram[b] * (fit_a * b**2 + fit_b * b + fit_c)
        print(f"{b:>3}{peri[b]:>10.3f}{ram[b]:>11.3f}{err[b]:>10.6f}{adj[b]:>10.3f}")

    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)
    gs = fig.add_gridspec(2, 2)

    plot_p(fig.add_subplot(gs[0, 0]), peri, ram)
    plot_err(fig.add_subplot(gs[0, 1]), err)
    plot_fit(fig.add_subplot(gs[1, 0]), err, fit_a, fit_b, fit_c)
    plot_fix(fig.add_subplot(gs[1, 1]), peri, adj)

    plt.show()


if __name__ == "__main__":
    main()
