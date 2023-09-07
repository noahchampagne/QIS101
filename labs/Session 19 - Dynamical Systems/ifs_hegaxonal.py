#!/usr/bin/env python3
"""ifs_hexagonal.py"""

from ifs import IteratedFunctionSystem
from pygame import Color
from simple_screen import SimpleScreen
import numpy as np

ifs = IteratedFunctionSystem()


def plot_ifs(ss: SimpleScreen) -> None:
    """Transforms the new space and recursively plots the points"""
    iterations = 200_000
    x: float = 0.0
    y: float = 0.0
    clr: Color

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)

    # Now draw each pixel in the stable orbit
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)


def main() -> None:
    """Maps the hexagons new start locations in the ifs function"""
    ifs.set_base_frame(0, 0, 30, 30)

    # Labels the vertices of the hexagon in the pattern shown
    p: float = 1 / 6
    y_offset: float = 10 * np.cos(np.pi / 5)
    a: tuple[float, float] = (10, 15 - y_offset)
    b: tuple[float, float] = (20, 15 - y_offset)
    c: tuple[float, float] = (25, 15)
    e: tuple[float, float] = (10, 15 + y_offset)
    d: tuple[float, float] = (20, 15 + y_offset)
    f: tuple[float, float] = (5, 15)
    o: tuple[float, float] = (15, 15)

    ifs.add_mapping(c[0], c[1], o[0], o[1], d[0], d[1], Color("blue"), p)
    ifs.add_mapping(d[0], d[1], o[0], o[1], e[0], e[1], Color("blue"), p)
    ifs.add_mapping(e[0], e[1], o[0], o[1], f[0], f[1], Color("blue"), p)
    ifs.add_mapping(f[0], f[1], o[0], o[1], a[0], a[1], Color("blue"), p)
    ifs.add_mapping(a[0], a[1], o[0], o[1], b[0], b[1], Color("blue"), p)
    ifs.add_mapping(b[0], b[1], o[0], o[1], c[0], c[1], Color("blue"), p)

    # Generates the transformations
    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS Square",
    )
    ss.show()


if __name__ == "__main__":
    main()
