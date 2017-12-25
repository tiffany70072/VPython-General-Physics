from __future__ import division
from visual import *

scene = display(title = "equipotential", width = 700, height = 700, 
              range = (1.5, 1.5, 1.5), background = (0, 0.2, 0.3))

n = 100                         # cut rod into n pieces
N = 200                         # cut circle into 4N pieces
Nj = 6                          # how many equipotential lines
ne = 20                         # how many electric field lines

L = 1.0
R = 2                           # the radius of initial circle
ball_r = L/200
E0 = 8.854E-12
k = 1/(4*pi*E0)

x = -L/2
dx = L/n

rod = cylinder(pos = (x, 0, 0), axis = (L, 0, 0), radius = L/30, color = color.cyan)

# list 
p = []              # position of the point
pin = []
pout = []
ball = []           # balls in 1st quadrant
ball2 = []          # balls in 2, 3, 4 quadrants
v = []
dv = []
v0 = []
lam = []

v0.append(14000)
v0.append(12000)
v0.append(10000)
v0.append(7500)
v0.append(5000)
v0.append(3000)
    
for j in range(Nj):
    p.append([])
    pin.append([])
    pout.append([])
    ball.append([])
    ball2.append([])
    v.append([])
    dv.append([])

    for i in range(N):
        p[j].append(vector(cos((2*pi/4)*i/N), sin((2*pi/4)*i/N), 0)*R)
        pin[j].append(vector(0, 0, 0))
        pout[j].append(p)
        v[j].append(0)
        dv[j].append(0)
        ball[j].append(sphere(pos = p[j][i], radius = ball_r, color = color.white))
    for i in range(3*N):
        ball2[j].append(sphere(radius = ball_r, color = color.orange))


# electric field lines
t = 0
dt = 0.0000002
pe = []               # the point to calculate electric field lines
dot = []              # the ball to calculate electric field lines
dE = []
E = []

for i in range(ne):
    if i < ne/2:
        pe.append(vector(-L/2 + L*(i/(ne/2-1)), L/50, 0))
    else:
        pe.append(vector(-L/2-L*((ne/2)/(ne/2-1)) + L*(i/(ne/2-1)), -L/50, 0))
    dot.append(sphere(pos = pe[i], color = color.green, radius = L/200, make_trail = True))
    dE.append(vector(0, 0, 0))
    E.append(vector(0, 0, 0))     

while 1:
# while x <= L/2:
    rate(1000)

    # calculate volt
    if x <= L/2:
        for j in range(Nj):
            for i in range(N):
                lam = (1E-6)*(sin(pi*x/L))**2
                dv[j][i] = (k*lam*dx/((p[j][i].x-x)**2 + p[j][i].y**2)**(1/2))
                v[j][i] += dv[j][i]
        x += dx
        
    # move ball       
    else:
        for j in range(Nj):
            for i in range(N):
                if v[j][i] < v0[j] and abs(v[j][i]-v0[j])>10:
                    pout[j][i] = p[j][i]
                    p[j][i] = (p[j][i] + pin[j][i])/2
                    v[j][i] = 0
                elif v[j][i] >= v0[j] and abs(v[j][i]-v0[j])>10:
                    pin[j][i] = p[j][i]
                    p[j][i] = (p[j][i] + pout[j][i])/2
                    v[j][i] = 0
                elif abs(v[j][i]-v0[j]) <= 10:
                    ball[j][i].color = color.red
                ball[j][i].pos = p[j][i]
        x = -L/2
        
    # do symmetry
    for j in range(Nj):
        for i in range(3*N):
            if i < N:
                ball2[j][i].pos = (-ball[j][i-0*N].pos.x,  + ball[j][i-0*N].pos.y, 0)
            elif i < 2*N:
                ball2[j][i].pos = (-ball[j][i-1*N].pos.x, -ball[j][i-1*N].pos.y, 0)
            else:
                ball2[j][i].pos = ( + ball[j][i-2*N].pos.x, -ball[j][i-2*N].pos.y, 0)
    
    # calculate electric field lines
    rate(1000000)
    for i in range(ne):
        if x <= L/2:
            lam = (1E-6)*(sin(pi*x/L))**2
            dE[i] = k*lam*dx/mag2(pe[i]-(x, 0, 0))*norm(pe[i]-(x, 0, 0))
            E[i] += dE[i]
            x += dx

        else:
            pe[i] += E[i]*dt
            E[i] = vector(0, 0, 0)
            x = -L/2
            t += dt
            dot[i].pos = pe[i]
              
