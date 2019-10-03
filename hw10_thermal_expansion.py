import random

from math import *
from visual import *


scene = display(title='Thermal Expansion', width=1600, height=400, background=(0.5, 0.5, 0))

A = 0.5
k = 3.0
m = 1.0
d = 1.0
b = 0.1
N = 30
size = 0.3
sl = d - 2 * size
x_0 = (N - 1) * d
line1 = curve(pos=((-d * N / 2, 4, 0), (-d * N / 2, -4, 0)), radius=0.03, color=color.red)
line2 = curve(pos=((+d * N / 2, 4, 0), (+d * N / 2, -4, 0)), radius=0.03, color=color.red)
c = 3

# Time
t = 0
dt = 0.01
times = 0

# List
ran = []
x = []
ball = []
v = []
s_l = []
spring = []
deltax = [0, 0, 0, 0]
totalx = [0, 0, 0, 0]
xx = []
dx = []


for j in range(4):
    x.append([])
    ball.append([])
    v.append([])
    s_l.append([])
    spring.append([])

    
for i in range(N):
    ran.append(random.uniform(-1, 1))
    x[0].append(d * (i - (N - 1) / 2) + 1 * A * (ran[i]))
    x[1].append(d * (i - (N - 1) / 2) + c * A * (ran[i]))
    x[2].append(d * (i - (N - 1) / 2) + 1 * A * (ran[i]))
    x[3].append(d * (i - (N - 1) / 2) + c * A * (ran[i]))
    for j in range(4):   
        v[j].append(0)
        ball[j].append(sphere(pos=(x[j][i], -2 * j + 3, 0), radius=size, color=color.white))

for i in range(N - 1):
    for j in range(4): 
        s_l[j].append(x[j][i+1] - x[j][i] - 2 * size)
        spring[j].append(helix(pos=(x[j][i] + size, -2 * j + 3, 0), axis=(s_l[j][i], 0, 0), radius=0.08, thickness=0.05))
    
while True:
    rate(50000)
    t += dt
    times += 1
    for j in range(4):
        for i in range(N):
            if i == 0:
                if j == 0 or j == 1:
                    a = k * (s_l[j][i] - sl) / m
                if j == 2 or j == 3:
                    a = k * (s_l[j][i] - sl) / m - b * (s_l[j][i] - sl) ** 2 / m
            elif i == N - 1:
                if j == 0 or j == 1:
                    a = -k * (s_l[j][i - 1] - sl) / m
                if j == 2 or j == 3:
                    a = -(k * (s_l[j][i - 1] - sl) / m - b * (s_l[j][i - 1] - sl) ** 2 / m)
            else:
                if j == 0 or j == 1:
                    a = k * (s_l[j][i] - sl) / m - k * (s_l[j][i - 1] - sl) / m
                if j == 2 or j == 3:
                    a = (k * ((s_l[j][i] - sl) - (s_l[j][i - 1] - sl)) - b * ((s_l[j][i] - sl) ** 2 - (s_l[j][i - 1] - sl) ** 2)) / m
            v[j][i] += a * dt
            x[j][i] += v[j][i] * dt
            ball[j][i].x = x[j][i]

        for i in range(N - 1):
            s_l[j][i] = x[j][i+1] - x[j][i] - 2*size
            spring[j][i].x = x[j][i] + size
            spring[j][i].axis = (s_l[j][i], 0, 0)

    for j in range(4):
        deltax[j] = x[j][N-1] - x[j][0]
        totalx[j] += deltax[j]
        
    if times == 1000:
        for j in range(4):
            xx.append(totalx[j] / 1000)
            dx.append(xx[j] - 29)
            
        print xx
        print dx[1] / dx[0], dx[3] / dx[2]
        print "(dx[3]/dx[2])/(dx[1]/dx[0]) = ", (dx[3 ] /dx[2]) / (dx[1] / dx[0])
        print c
            
        times = 0
        totalx = [0, 0, 0, 0]
        xx = []
        dx = []
