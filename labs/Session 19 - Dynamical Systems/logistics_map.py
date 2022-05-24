#!/usr/bin/env python3
# logistics_map.py

import numpy as np
from simple_screen import SimpleScreen


def plot_logistics_map(ss):
    for sx in range(ss.screen_width):
        x = ss.world_x(sx)
        y = np.random.random()

        # Iterate (but don't draw) to reach a stable orbit
        for i in range(500):
            y = x * y * (1 - y)

        for i in range(500):
            y = x * y * (1 - y)
            ss.set_world_pixel(x, y, "blue")


def main():
    ss = SimpleScreen(
        world_rect=((2.5, 0), (4.0, 1)),
        draw_function=plot_logistics_map,
        screen_size=(900, 900),
        title="Logistics Map",
    )
    ss.show()


if __name__ == "__main__":
    main()
