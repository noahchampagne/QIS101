#!/usr/bin/env python3
"""ifs_triangle.py"""

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
    ifs.set_base_frame(0, 0, 30, 30)

    p: float = 1 / 3

    ifs.add_mapping(0, 0, 15, 0, 0, 15, Color("blue"), p)
    ifs.add_mapping(15, 0, 30, 0, 15, 15, Color("blue"), p)
    ifs.add_mapping(7.5, 15, 22.5, 15, 7.5, 30, Color("blue"), p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="Sierpinksi Triangle",
    )
    ss.show()


if __name__ == "__main__":
    main()
