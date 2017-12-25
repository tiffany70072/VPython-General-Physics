from __future__ import division
from visual import * 
from math import * 

A = 3.0
k = 3.0
m = 1.0
d = 1.0
b = 0.1
T1 = 20
T2 = 10
N = 2000
Nshow = 80
Nbuffer = 100
bradius = 0.3
sl = d - 2 * bradius

scene = display(title = 'Spring Wave', width = 1600, height = 200, background = (0.5, 0.5, 0))
t = 0
dt = 0.03
ball = []
b_v = []
s_l = []
ballshow = []
springshow = []

ball2 = []
b_v2 = []
s_l2 = []
ballshow2 = []
springshow2 = []
y =  - 5

b80 = 0
b300 = 0
b1900 = 0
b2_80 = 0
b2_300 = 0
b2_1900 = 0
ball_1 =  - (Nshow - 1)/2 * d

O = sphere(pos = (d * (-Nshow/2), y/2, 0), size = 0.5, color = color.red)

# question 1
for i in range(N):
    ball.append(d * (i - (Nshow - 1)/2.0))
    b_v.append(0)
    if i < Nshow:
        ballshow.append(sphere(pos = (ball[i], 0, 0), radius = bradius, color = color.white))
                        
for i in range(N-1):
    s_l.append(ball[i+1] - ball[i] - 2 * bradius)
    if i < Nshow - 1:
        springshow.append(helix(pos = (s_l[i], 0, 0), radius = 0.08, thickness = 0.05))

# question 2
for i in range(N):
    ball2.append(d * (i - (Nshow - 1)/2.0))
    b_v2.append(0)
    if i < Nshow:
        ballshow2.append(sphere(pos = (ball2[i], y, 0), radius = bradius, color = color.white))
                        
for i in range(N-1):
    s_l2.append(ball2[i+1] - ball2[i] - 2 * bradius)
    if i < Nshow - 1:
        springshow2.append(helix(pos = (s_l2[i], y, 0), radius = 0.08, thickness = 0.05))

while 1:
    rate(50000)
    # question 1
    for i in range(N):
        if i == 0:
            ball[i] = d * (i - (Nshow - 1)/2.0) + A * sin(2 * pi/T1 * t)
        else:
            if i == N - 1:
                a = k/m * (-1) * (s_l[i-1] - sl) - b/m * b_v[i]
            elif i > N - Nbuffer:
                a = k/m * ((s_l[i] - sl) - (s_l[i-1] - sl)) - b/m * b_v[i]
            else:
                a = k/m * ((s_l[i] - sl) - (s_l[i-1] - sl))
            b_v[i] += a * dt
            ball[i] += b_v[i] * dt

            if b_v[79] != 0 and b80 == 0:
                b80 = 1
                print "v1_80 = ", (ball[79] - ball_1)/t, "m/s"
            if b_v[299] != 0 and b300 == 0:
                b300 = 1
                print "v1_300 = ", (ball[299] - ball_1)/t, "m/s"
            if b_v[1899] != 0 and b1900 == 0:
                b1900 = 1
                print "v1_1900 = ", (ball[1899] - ball_1)/t, "m/s"
 

        if i < Nshow:
            ballshow[i].x = ball[i]

    for i in range(N-1):
        s_l[i] = ball[i+1] - ball[i] - 2 * bradius

        if i < Nshow - 1:
            springshow[i].x = ballshow[i].x + bradius
            springshow[i].axis = (s_l[i], 0, 0)
    # question 2
    for i in range(N):
        if i == 0:
            ball2[i] = d * (i - (Nshow-1)/2.0) + A * sin(2*pi/T2*t)
        else:
            if i == N - 1:
                a = k/m * (-1) * (s_l2[i-1] - sl) - b/m * b_v2[i]
            elif i > N - Nbuffer:
                a = k/m * (s_l2[i] - sl) - (s_l2[i-1] - sl) - b/m * b_v2[i]
            else:
                a = k/m * ((s_l2[i] - sl) - (s_l2[i-1] - sl))
            b_v2[i] += a * dt
            ball2[i] += b_v2[i] * dt

            if b_v[79] != 0 and b2_80 == 0:
                b2_80 = 1
                print "v2_80 = ", (ball[79] - ball_1)/t, "m/s"
            if b_v[299] != 0 and b2_300 == 0:
                b2_300 = 1
                print "v2_300 = ", (ball[299] - ball_1)/t, "m/s"
            if b_v[1899] != 0 and b2_1900 == 0:
                b2_1900 = 1
                print "v2_1900 = ", (ball[1899] - ball_1)/t, "m/s"
 

        if i < Nshow:
            ballshow2[i].x = ball2[i]

    for i in range(N - 1):
        s_l2[i] = ball2[i+1] - ball2[i] - 2 * bradius

        if i < Nshow - 1:
            springshow2[i].x = ballshow2[i].x + bradius
            springshow2[i].axis = (s_l2[i], 0, 0)

    t += dt
           
    
    



                          
