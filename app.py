#! /usr/bin/env python3

import time
import gr
import numpy as np
from math import tau

def main():
    print("Hello from gr-tutorial!")

    # Pendulum parameters
    L: float = 1  # length of pendulum
    m: float = 1  # mass of pendulum
    b: float = 1
    g: float = 9.81
    dt: float = 0.01

    d2theta: float = 0
    d1theta: float = 0
    theta: float = tau * 0.25

    gr.setwindow(-2, 2, -2, 2)
    gr.setviewport(0, 1, 0, 1)
    print(gr.inqwindow())  # print (-2, 2, -2, 2)

    gr.setfillcolorind(gr.inqcolorfromrgb(0, 0, 0))
    gr.setfillintstyle(gr.INTSTYLE_SOLID)
    gr.fillrect(*gr.inqwindow())

    def draw_pendulum(theta: float):
        alpha = theta - 0.25 * tau

        x0 = L * np.cos(alpha)
        y0 = L * np.sin(alpha)

        gr.setfillcolorind(gr.inqcolorfromrgb(0, 0, 0))
        gr.setfillintstyle(gr.INTSTYLE_SOLID)
        gr.fillrect(*gr.inqwindow())

        # sets the color to be gray
        gr.setlinecolorind(gr.inqcolorfromrgb(1, 1, 1))
        gr.setmarkercolorind(gr.inqcolorfromrgb(0, 0, 1))
        gr.setmarkersize(2)
        gr.setmarkertype(gr.MARKERTYPE_SOLID_CIRCLE)

        gr.polyline([0, x0], [0, y0])
        gr.polymarker([x0], [y0])

    def update_pendulum():
        nonlocal d2theta, d1theta, theta

        d2theta = -m * g * np.sin(theta) - b * d1theta
        d1theta += d2theta * dt
        theta += d1theta * dt


    draw_pendulum(theta)


    N = int(10 // dt)

    # For for 10 seconds of simulation time.
    for _ in range(N):
        t0 = time.perf_counter()

        while time.perf_counter() - t0 < dt:
            pass

        update_pendulum()

        gr.clearws()
        draw_pendulum(theta)
        gr.updatews()

    _ = input()


if __name__ == "__main__":
    main()
