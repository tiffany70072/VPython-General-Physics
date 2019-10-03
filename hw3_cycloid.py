from math import *
from visual import *


# Define physics coefficients.
g = 9.8 
pi = 3.14
R = 1.0
size = 0.03

zero_to_halfpi = [0.005 * t for t in range(0, 314)]
# longboard = [0.01 * t for t in range(0, 100)]

under_board = [(-(R + size) * cos(theta), -(R + size) * sin(theta)) for theta in zero_to_halfpi]
# under_board = [(-(R + size) + x, -x) for x in longboard]

straight = [(0, 0, 0), (0, 0, -1.25)]
extrusion(pos=straight, shape=under_board, color=color.yellow)

# initial_pos = [1.0, 0.75, 0.5, 0.25]
initial_pos = [0.0, 0.125, 0.25, 0.375]

# Start simulation.
for frac in initial_pos:
    # ball = sphere(pos=(-frac * R, -1.0 + frac, -frac), radius=size, color=color.red)
    ball = sphere(pos=(-R * cos(frac * pi), -R * sin(frac * pi), frac * 2 - 1.0), radius=size, color=color.red)
    ball.velocity = vector(0.0, 0.0, 0.0)

    t = 0
    dt = 0.0001

    while ball.pos.x < 0.0:
        rate(5000)

        t = t + dt
        ball.pos = ball.pos + ball.velocity * dt

        th = acos(-ball.pos.x / R)
        acc = vector(mag(ball.velocity) ** 2 * cos(th) / R, mag(ball.velocity) ** 2 * sin(th) / R, 0)
        gcom = vector(g * cos(th) * sin(th), -g * cos(th) ** 2, 0)

        # th = pi / 4.0
        # acc = vector(0, 0, 0)
        # gcom = vector(g * cos(th) * sin(th), -g * cos(th) ** 2, 0)

        total_a = acc + gcom
        ball.velocity = ball.velocity + total_a * dt

    print "time", t
