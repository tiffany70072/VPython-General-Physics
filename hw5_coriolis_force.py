from __future__ import division
from visual import*

scene = display(width = 800, height = 800, forward = (0.5, -1, -3), background = (0, 1, 1))

i = arrow(axis = vector(300, 0, 0), shaftwidth = 15, color = color.yellow)
j = arrow(axis = vector(0, 1000, 0), shaftwidth = 15, color = color.yellow)
k = arrow(axis = vector(0, 0, 300), shaftwidth = 15, color = color.yellow)

floor = box(pos = (0, 550, -3), length = 300, height = 1200, width = 6, color = color.black)

size = 50.0
x = (0.0, 0.0, size)
g =  - 9.8
w = vector(0.0, 7.27*10**(-5), 0.0)
r = vector(0.0, 0.0, 6378100)

ball_red1 = sphere(pos = x, radius = size, color = color.red)
ball_red2 = sphere(pos = x, radius = size, color = color.red)
ball_blue1 = sphere(pos = x, radius = size, color = color.blue)
ball_blue2 = sphere(pos = x, radius = size, color = color.blue)

ball_red1.velocity = vector(0.0, 0.0, 100.0)
ball_red2.velocity = vector(0.0, 0.0, 100.0)
#ball_blue1.velocity = vector(100.0*cos(pi/4), 0.0, 100.0*sin(pi/4))
ball_blue1.velocity = vector(0.0, 100.0*cos(pi/4), 100.0*sin(pi/4))
ball_blue2.velocity = vector(0.0, 100.0*cos(pi/4), 100.0*sin(pi/4))

t = 0
dt = 0.001

while ball_red1.pos.z >= size:
    rate(10000)
    t = t + dt
    ball_red1.pos = ball_red1.pos + ball_red1.velocity*dt
    a = g*vector(0, 0, 1)
    ball_red1.velocity = ball_red1.velocity + a*dt
    t_red1 = t
print "red ball1  = ", ball_red1.pos, mag(ball_red1.pos), "(m), ", "landing time  = ", t_red1, "(s)"

while ball_red2.pos.z >= size:
    rate(10000)
    t = t + dt
    ball_red2.pos = ball_red2.pos + ball_red2.velocity*dt
    a = g * vector(0, 0, 1) - cross(w, cross(w, r)) - 2*cross(w, ball_red2.velocity)
    ball_red2.velocity = ball_red2.velocity + a*dt

    t_red2 = t - t_red1
print "red ball2  = ", ball_red2.pos, mag(ball_red1.pos), "(m), ", "landing time  = ", t_red2, "(s)"
print "delta x  = ", ball_red2.pos.x - ball_red1.pos.x, "(m)"

while ball_blue1.pos.z >= size:
    rate(10000)
    t = t + dt
    ball_blue1.pos = ball_blue1.pos + ball_blue1.velocity * dt
    a = g * vector(0, 0, 1)#*(ball_red1.pos + r)/mag(r)
    ball_blue1.velocity = ball_blue1.velocity + a * dt

    t_blue1 = t - t_red2 - t_red1
print "blue ball1  = ", ball_blue1.pos, mag(ball_blue1.pos), "(m), ", "landing time  = ", t_blue1, "(s)"

while ball_blue2.pos.z >= size:
    rate(10000)
    t = t + dt
    ball_blue2.pos = ball_blue2.pos + ball_blue2.velocity * dt
    a = g * vector(0, 0, 1) - cross(w, cross(w, r)) - 2*cross(w, ball_red2.velocity)
    ball_blue2.velocity = ball_blue2.velocity + a * dt

    t_blue2 = t - t_blue1 - t_red2 - t_red1
print "blue ball2  = ", ball_blue2.pos, mag(ball_blue1.pos), "(m), "
print "landing time  = ", t_blue2, "(s)"
print "delta x  = ", ball_blue2.pos.x - ball_blue1.pos.x, "(m), "
print "delta y  = ", ball_blue2.pos.y - ball_blue1.pos.y, "(m)"





