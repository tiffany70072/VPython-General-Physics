from visual import *

size = 0.03
x_1 = (0.0, 0.0, 0.0)
x_2 = (-1.0, -1.0, 0.0)
v_1 = vector(-0.3, 0.0, 0.0)
v_2 = vector(0.2, 0.5, 0.0)
m1 = 1
m2 = 1000

def af_col_v(m1, m2, v1, v2, x1, x2):
    #v1_prime = v1+(x1-x2)*dot(v2-v1, x1-x2)/dot(x1-x2, x1-x2)
    #v2_prime = v2+(x2-x1)*dot(v1-v2, x2-x1)/dot(x2-x1, x2-x1)
    v1_prime = v1+(x1-x2)*dot(v2-v1, x1-x2)/dot(x1-x2, x1-x2)*2*m2/(m1+m2)
    v2_prime = v2+(x2-x1)*dot(v1-v2, x2-x1)/dot(x2-x1, x2-x1)*2*m1/(m1+m2)
    return(v1_prime, v2_prime)

b_0 = sphere(pos = (0, 0, 0), radius = 0.05, color = color.red)
b_1 = sphere(pos = x_1, radius = size, color = color.yellow)
b_2 = sphere(pos = x_2, radius = size, color = color.green)
b_1.velocity = v_1
b_2.velocity = v_2

t = 0
dt = 0.0001
while t < 5:
    rate(10000)

    t = t + dt
    b_1.pos = b_1.pos + b_1.velocity*dt
    b_2.pos = b_2.pos + b_2.velocity*dt

    if abs(b_1.pos - b_2.pos) <= 2*size:
        #(b_1.velocity, b_2.velocity) = af_col_v(b_1.velocity, b_2.velocity, b_1.pos, b_2.pos)
        (b_1.velocity, b_2.velocity) = af_col_v(m1, m2, b_1.velocity, b_2.velocity, b_1.pos, b_2.pos)
        print b_1.velocity, b_2.velocity, dot(b_1.velocity, b_2.velocity)
