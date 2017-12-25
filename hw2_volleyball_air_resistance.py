from __future__ import division
from visual import * 

display(center = (0, 10, 0), background = (0.6, 0.8, 1), width = 500, length = 500)

g = 9.8
m = 1
size = 1
x = vector(-15, 1.25, 0)
ra = 10000

co = 0.4
power = 1.1

vv = 25
pis = pi/18    #10 degrees
ma = 0

ball = sphere(pos = x,  radius = size,  color = (1, 0.3, 0.3))
floor = box(pos = (5, 0, 0), length = 50, height = 0.5, width = 4, color = (1, 1, 0.8))

#theta = pi/4
#v = vector(vv*cos(theta), vv*sin(theta), 0.0)
#a = vector(-co/m*vv**power*cos(theta), -co/m*vv**power*sin(theta)-g, 0.0)
#u = mag(v)*0.9

dt = 0.001
t = 0

# 10 degrees
for theta in arange(0*pis, pi/2, pis):
    print "theta = ", theta * 180/pi, 
    th = theta
    x = vector(-15, 1.25, 0)
    v = vector(vv * cos(theta), vv * sin(theta), 0.0)
    while x.y> = size:
        rate(ra)
        theta = acos(v.x/mag(v))
        a = vector(-co/m * vv**power * cos(theta), -co/m * vv**power * sin(theta)-g, 0.0)
        v = v + a * dt
        x += v * dt
        ball.pos = x
    if x.x + 15>ma:
        ma = x.x + 15
        big = th
        
    print ", pos = ", x.x + 15
print "\n1. max = ", ma, ",  as", big * 180/pi, "(degrees)"

# 1 degree
ma = 0
for theta in arange(big-pi/18, big + pi/18, pi/180):
    print "theta = ", theta * 180/pi, 
    th = theta
    x = vector(-15, 1.25, 0)
    v = vector(vv * cos(theta), vv * sin(theta), 0.0)
    while x.y >= size:
        rate(ra)
        theta = acos(v.x/mag(v))
        a = vector(-co/m * vv**power * cos(theta), -co/m * vv**power * sin(theta)-g, 0.0)
        v = v + a * dt
        x += v * dt
        #ball.pos = x
    if x.x + 15 > ma:
        ma = x.x + 15
        big = th
        
    print ", pos = ", x.x + 15
print "\n2. max = ", ma, ",  as", big*180/pi, "(degrees)"

# max distance
x = vector(-15, 1.25, 0)
theta = big
v = vector(vv * cos(theta), vv * sin(theta), 0.0)
dt = 0.0001
while x.y> = size:
    rate(10000)

    theta = acos(v.x/mag(v))
    a = vector(-co/m * vv**power * cos(theta), -co/m * vv**power * sin(theta)-g, 0.0)
    v = v + a * dt
    x += v * dt
    ball.pos = x
    ball.trail = True

    """if v.y<0 and t> = 0.02:
        print t, mag(v)
        t = 0
    t += dt"""
    
#find the final position
print "3. final position  =  ", x.x + 15, "(m)"
    