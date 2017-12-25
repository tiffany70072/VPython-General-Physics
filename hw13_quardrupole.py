from __future__ import division
from visual import *


# electric field lines of quadrupole
scene = display(title = "quadrupole", background = (0, 0, 0), width = 600, height = 600, range = (2.5, 2, 2))

k = 8.987E9
Q = 1E-5
q = 1E-12
m = 1E-6
rad_c = 0.10       # radius of charges
rad_b = 0.01       # radius of ball
x = rad_c+rad_b    # initial position of ball

ball1_pos = vector(1, 0, 0)   # type the position of the ball here
ball2_pos = vector(-1, 0, 0)

po1 = sphere(pos = (1, 0, 0), color = color.red, radius = 0.10)
ne1 = sphere(pos = (0, 1, 0), color = color.blue, radius = 0.10)
po2 = sphere(pos = (-1, 0, 0), color = color.red, radius = 0.10)
ne2 = sphere(pos = (0, -1, 0), color = color.blue, radius = 0.10)


# list
ball = []
r_po1 = []
r_ne1 = []
r_po2 = []
r_ne2 = []
E = []
v = []

N = 8
for i in range(6*N):
    v.append(vector(0, 0, 0))             # velocity of ball
    r_po1.append(0)
    r_ne1.append(0)
    r_po2.append(0)
    r_ne2.append(0)
    E.append(0)
    
    if i < 3 * N:
        ball.append(sphere(pos = ball1_pos, color = color.yellow, 
                           radius = rad_b, make_trail = True))
        if i < N:
            ball[i].pos += x*vector(cos(i*2*pi/N), sin(i*2*pi/N), 0)
        elif i < 2*N:
            ball[i].pos += x*vector(0, cos(i*2*pi/N), sin(i*2*pi/N))
        else:
            ball[i].pos += x*vector(cos(i*2*pi/N), 0, sin(i*2*pi/N))
            
    else:
        ball.append(sphere(pos = ball2_pos, color = color.green, 
                           radius = rad_b, make_trail = True))
        if i < 4 * N:
            ball[i].pos += x * vector(cos(i*2*pi/N), sin(i*2*pi/N), 0)
        elif i < 5 * N:
            ball[i].pos += x * vector(0, cos(i*2*pi/N), sin(i*2*pi/N))
        else:
            ball[i].pos += x * vector(cos(i*2*pi/N), 0, sin(i*2*pi/N))


t = 0
n = 0
dt = 0.1E-7

while 1:
    rate(10000)
    
    # calculation
    for i in range(6*N):
        r_po1[i] = ball[i].pos - po1.pos
        r_ne1[i] = ball[i].pos - ne1.pos
        r_po2[i] = ball[i].pos - po2.pos
        r_ne2[i] = ball[i].pos - ne2.pos

        if mag(r_ne1[i]) > 0.1 and mag(r_ne2[i]) > 0.1:
            E[i] = k * Q * (norm(r_po1[i])/(mag(r_po1[i])**2) + norm(r_po2[i])/(mag(r_po2[i])**2)
                  - norm(r_ne1[i])/(mag(r_ne1[i])**2) - norm(r_ne2[i])/(mag(r_ne2[i])**2))
            v[i] = E[i]
            ball[i].pos += v[i] * dt
            
    
    t += dt
    n += 1
