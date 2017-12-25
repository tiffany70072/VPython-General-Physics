from __future__ import division
from visual import *
from random import random

rang = 0.5E-4
L = 1E-5


scene = display(title = "drift velocity", background = (0, 0.3, 0.3), width = 800, height = 500, 
        center = (L/2, L/2, -5*L), range = (rang, rang, rang), forward = (-1, 0, -1))
E0 = 8.854E-12
k = 1/(4*pi*E0)

q = -1E-12
m = 1E-8
r = 5E-7
E = 1E-2*vector(0, 0, 1)
v = vector(0, 0, 0)

box = box(pos = (L/2, L/2, -5*L), width = 10*L, height = L, length = L, 
        color = color.white, opacity = 0.2)
p = vector(r + (L-2*r)*random(), r + (L-2*r)*random(), 0)        #the position of the charge
charge = sphere(pos = p, color = color.red, radius = 5E-7, make_trail = True)

#list
ball = []
for j in range(99):
    ball.append([])
    for i in range(5):
        ball[j].append(sphere(pos = (r+(L-2*r)*random(), r+(L-2*r)*random(), 
                                   -((j+1)*L/10+r+(L/10-2*r)*random())), 
                              radius = r, color = (1, 1, 1)))
        #color = (1, j/99, j/99)))

def collision(v1, x1, x2):
    #v1f = norm((v1+(x2-x1)*dot(-v1, x2-x1)/dot(x2-x1, x2-x1)))*mag(v1)*2**(-0.5)
    #v1f = norm(v1-2*(x2-x1)*(dot(v1, x2-x1)/mag2(x2-x1)))*mag(v1)*2**(-0.5)
    v_p = dot(v1, x1 - x2)*v1/mag2(v1)
    v_v = v1 - v_p
    v1f = norm(v_v - v_p)*abs(v1)*2**(-0.5)
    return (v1f)
N = 1   
t = 0
dt = 0.001
#charge zero
while p.z >= -10*L: 
    rate(1000)
    v += q * E/m * dt
    p = p + v*dt

    for j in range(99):
        for i in range(5):
            if mag(p - ball[j][i].pos) <= 2 * r:
                v1 = v
                x1 = p
                x2 = ball[j][i].pos
                v = collision(v1, x1, x2)
                ball[j][i].color = color.red
                N += 1
    if (p.x <= r and v.x < 0) or (p.x >= L - r and v.x > 0):
        v = vector(-v.x, v.y, v.z)
    if (p.y <= r and v.y < 0) or (p.y >= L - r and v.y > 0):
        v = vector(v.x, -v.y, v.z)

    charge.pos = p
    scene.center = (p.x, p.y, p.z + 8*L/10)   

    t += dt

T = t/N
print "dt = ", dt
print "N", N
print "t = ", t, "(s)"
print "Vd = ", vector(0, 0, -1)*10*L/t, "(m/s)"
print "Vd in theory = ", abs(q)*E/m*T, "(m/s)"


t = 0
dt = 0.002

#1~100 charges
n = 1
t = 0
N = 0                  #the times of collision
T = 0
T_total = 0            #mean free time
t_total = 0            #the average time to through the box
Vdi_total = vector(0, 0, 0)
scene.center = (L, 0, -5*L)
scene.forward = (-1, 0, 0)
while n <= 100:
    rate(1000000)
    
    if p.z <= -10*L:
        if N! = 0:
            T = t/N
        else:
            T = t
        T_total += T
        t_total += t
        #print n, t, T_total
        #print n, N
        t = 0
        N = 0
        n += 1
        p = vector(r+(L-2*r)*random(), r+(L-2*r)*random(), 0)
        #print p
        
    else:
        v += q*E/m*dt
        p = p+v*dt

        if (p.x <= r and v.x<0) or (p.x >= L-r and v.x > 0):
            v = vector(-v.x, v.y, v.z)
        if (p.y <= r and v.y<0) or (p.y >= L-r and v.y > 0):
            v = vector(v.x, -v.y, v.z)
            
        for j in range(99):
            for i in range(5):
                if mag(p-ball[j][i].pos) <= 2*r:
                    v1 = v
                    x1 = p
                    x2 = ball[j][i].pos
                    v = collision(v1, x1, x2)
                    N += 1
                    ball[j][i].color = color.orange
                    #ball[j][i].color = ball[j][i].color+(0, -0.1, -0.1)
        t += dt
        
ta = t_total/100
Ta = T_total/100
#print "n", n
print "dt", dt
print "t_ave", ta
print "T_ave", Ta
print "Vd_ave", vector(0, 0, -1)*10*L*100/t_total
print "Vd in theory = ", q*E/m*Ta, "(m/s)"

   
    
