from __future__ import division
from visual import*

ran = 1.5E-8
scene = display(title = 'Lorentz force', width = 600, height = 600, 
              background = (0.2, 0.6, 0.6), range = (ran, ran, ran))

q     = 1.6E-19
dt    = 5E-12
A     = 1E-10
mass  = 1.67E-27
Bcharge = 1E-16
BNP   = vector(0, -1E-8, 0)
BSP   = vector(0, 1E-8, 0)


a1_pos = vector(0, 0, 1E-8)
a2_pos = vector(0, 0, 1E-8)
#different initial velocity
a1_v   = vector(2E-2, 1E-3, 0)
a2_v   = vector(3E-2, 9E-2, 0)

pink  = vector(1, 0.3, 0.3)
red   = vector(1, 0, 0)
atom1 = sphere(pos = a1_pos, radius = A, color = (1, 0.9, 0.1))
atom2 = sphere(pos = a2_pos, radius = A, color = pink)
atom1trail  = curve(color = atom1.color)
atom2trail  = curve(color = atom2.color)
N     = sphere(pos = BNP, radius = 1E-9, color = color.blue)
S     = sphere(pos = BSP, radius = 1E-9, color = color.red)

L = 1E-8
LL = 4*1E-8
plane1 = box(pos = (0, 0, 0.6*L), width = 0.01*L, height = LL, length = LL, opacity = 0.1)
plane2 = box(pos = (0, 0, 0.3*L), width = 0.01*L, height = LL, length = LL, opacity = 0.1)
plane3 = box(pos = (0, 0, 0.0*L), width = 0.01*L, height = LL, length = LL, opacity = 0.1)
plane4 = box(pos = (0, 0, -0.3*L), width = 0.01*L, height = LL, length = LL, opacity = 0.1)
plane5 = box(pos = (0, 0, -0.6*L), width = 0.01*L, height = LL, length = LL, opacity = 0.1)

def B1(r):
    B = vector(0, 1, 0)
    return B

def B2(r):
    B = Bcharge*(norm(r-BNP)*mag(r-BNP)**(-2)-norm(r-BSP)*mag(r-BSP)**(-2))
    return B

s = 1
ss = 0
n = 0
t = 0

while True:
    rate(10000000)
    # question 1
    if s == 0:
        a1 = q * cross(a1_v, B1(a1_pos))/mass
        a1_v += a1*dt
        a1_pos += a1_v*dt
        atom1.pos = a1_pos
        atom1trail.append(pos = a1_pos)

    # question 2
    a2 = q * cross(a2_v, B2(a2_pos))/mass
    a2_v += a2*dt
    a2_pos += a2_v*dt
    atom2.pos = a2_pos
    atom2trail.append(pos = a2_pos)

    t += dt
    if a2_pos.y*(a2_pos + a2_v*dt).y < 0 and ss == 0:
        ss = 1
        t = 0
    if a2_pos.y*(a2_pos + a2_v*dt).y < 0 and ss == 1 and t != 0:
        n += 1
        print "time = ", t/(n/2), "(s)"
    
