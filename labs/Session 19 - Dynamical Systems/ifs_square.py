#!/usr/bin/env python3
"""ifs_square.py"""

from ifs import IteratedFunctionSystem
from pygame import Color
from simple_screen import SimpleScreen

ifs = IteratedFunctionSystem()


def plot_ifs(ss: SimpleScreen) -> None:
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
    ifs.set_base_frame(0, 0, 4, 4)

    p: float = 1 / 4

    ifs.add_mapping(0, 0, 2, 0, 0, 2, Color("blue"), p)
    ifs.add_mapping(2, 0, 4, 0, 2, 2, Color("yellow"), p)
    ifs.add_mapping(0, 2, 2, 2, 0, 4, Color("red"), p)
    ifs.add_mapping(2, 2, 4, 2, 2, 4, Color("green"), p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((-2, -2), (6, 6)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS Square",
    )
    ss.show()


if __name__ == "__main__":
    main()
