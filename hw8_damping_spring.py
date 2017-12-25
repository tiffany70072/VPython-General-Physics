from __future__ import division
from visual import *
from math import *

scene = display(title = 'examples', width = 600, height = 600, background = (0, 1, 1))

size = 0.03
mass = 0.4
b = 0.05
k = 40
d = 0.05

celling = box(pos = (0, 0.2 + size + 1/2 * 0.02, 0), length = 0.5, height = 0.02, width = 0.1, color = color.black)
p = box(pos = (0, -d, 0), length = 2 * size, height = 2 * size, width = 2 * size, color = color.blue, velocity = vector(0, 0, 0))
spring = helix(pos = (0, 0.2 + size, 0), axis = (0, -0.2 + p.pos.y, 0), radius = 0.02)

energy0 = 1/2*k*d**2

print "initail energy = ", energy0

t = 0
f = 0
g = 0
h = 0
while 1:
    rate(1000)
    dt = 0.001
    t += dt
    
    p_a = -b/mass*p.velocity.y - k/mass*p.pos.y
    p.velocity.y += p_a * dt
    p.pos.y += p.velocity.y * dt
    
    spring.axis = (0, -0.2 + p.pos.y, 0)
    energy = 1/2 * mass * (p.velocity.y)**2 + 1/2 * k * abs(p.pos.y)**2

    #question1
    if p.velocity.y*(p.velocity.y+p_a*dt)<0 and p.velocity.y<0 and f == 0:
        f = 1
        print "the period of the motion = ", t, "(sec)"
      
    #question2
    if p.velocity.y*(p.velocity.y + p_a * dt)<0 and abs(p.pos.y) <= 1/2 * d and g == 0:
        g = 1
        print "time for haif amplitude = ", t, "(sec)"

    #question3
    if energy <= 1/2 * energy0 and energy > 0.4999*energy0 and h == 0:
        h = 1
        print "time for half mechanical energy = ", t, "(sec)"


        
