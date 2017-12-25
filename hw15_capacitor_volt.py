from __future__ import division
from visual import * 

rang = 0.007
scene = display(title = "capacitor", width = 700, height = 500, background = (0.1, 0.1, 0.1), 
              center = (0.005, 0.001, 0), range = (rang, rang, rang))
E0 = 8.854E-12
k = 1/(4 * pi * E0)
sigma = 1E-2
L = 0.01
d = 0.2 * L                      # distance between two plates
x = 0
N = 100                        # cut surface into 30 * N pieces
dx = L/N
dz = L/30
ds = L/600

plate_p = box(pos = (0.5 * L, d, -0.75 * L), width = 1.5 * L, length = L, height = 0.01 * L, 
            color = color.red, material = materials.plastic)
plate_n = box(pos = (0.5 * L, 0, -0.75 * L), width = 1.5 * L, length = L, height = 0.01 * L, 
            color = color.blue, material = materials.plastic)
#  x_axis = arrow(pos = (0, 0, -0.05 * L), axis = (1.5 * L, 0, 0), shaftwidth = 0.01 * L, color = color.white)
#  y_axis = arrow(pos = (0, 0, -0.05 * L), axis = (0, 0.8 * L, 0), shaftwidth = 0.01 * L, color = color.white)
wall = box(pos = (0.5 * L, d/2, -dz-0.005 * L), width = 0.01 * L, length = 1.2 * L, height = 3 * d, 
         color = (1, 1, 1), opacity = 0.2)


# electric field lines
eflp = [vector(-1E-6, d, -dz/2)]
efl = []
efl2 = []               # symmetry
dE = []
E = []
n1 = 20                 # how many electric field lines

for i in range(n1):
    if i >= 1:
        eflp.append(vector((i-1) * L/2/(n1-1.5), 0.195 * L, -dz/2))
    efl.append(sphere(pos = eflp[i], color = color.cyan, radius = L/200, make_trail = True))
    efl2.append(sphere(pos = (-eflp[i].x+L, eflp[i].y, eflp[i].z), 
                       color = color.cyan, radius = L/200, make_trail = True))
    dE.append(vector(0, 0, 0))
    E.append(vector(0, 0, 0))


while eflp[0].y>-1E-2 and eflp[0].x<1E-5:
    rate(100000)
    if x <= L:
        for i in range(n1):
            r_p = eflp[i]-(x, d, -dz/2)
            r_n = eflp[i]-(x, 0, -dz/2)
            dE[i] = k * sigma * (dx * dz) * (norm(r_p)/mag2(r_p)-norm(r_n)/mag2(r_n))
            E[i] += dE[i]
        x += dx
        
    if x > L:
        for i in range(n1):
            eflp[i] += norm(E[i]) * ds
            efl[i].pos = eflp[i]
            efl2[i].pos = (-eflp[i].x+L, eflp[i].y, eflp[i].z)
            E[i] = vector(0, 0, 0)
        x = 0
print "There are", 2 * n1, "electric field lines."

# equipotential lines
n2 = 400                         # how many lines to find volt
nj = 5                           # how many equipotential lines
v_v0 = 1
delv0 = 25000

v = []                           # potential of particular point
dv = []
v0 = [0, delv0, 2 * delv0, 3 * delv0, 4 * delv0]
v_p = []                         # equipotential dots
v_line = []                      # draw lines
v_line2 = []                     # symmetry
v_line3 = []
v_line4 = []
v_h = []                         # the higher point
v_l = []                         # the lower point

for j in range(nj):
    v.append([])
    dv.append([])
    v_p.append([])
    v_line.append([])
    v_line2.append([])
    v_line3.append([])
    v_line4.append([])
    v_h.append([])
    v_l.append([])
     
    for i in range(n2):
        v[j].append(0)
        dv[j].append(0)
        v_p[j].append(vector(-0.3 * L+i * 0.8 * L/(n2-1), 0.2 * L * 0.5, -dz))
        v_line[j].append(sphere(pos = v_p[j][i], color = color.yellow, radius = L/500))
        v_line2[j].append(sphere(pos = (-v_p[j][i].x+L, v_p[j][i].y, v_p[j][i].z), 
                               color = color.yellow, radius = L/500))
        v_line3[j].append(sphere(pos = (v_p[j][i].x, -v_p[j][i].y+d, v_p[j][i].z), 
                               color = color.yellow, radius = L/500))
        v_line4[j].append(sphere(pos = (-v_p[j][i].x+L, -v_p[j][i].y+d, v_p[j][i].z), 
                               color = color.yellow, radius = L/500))
        v_h[j].append(v_p[j][i]+vector(0, 0.1 * L, 0))
        v_l[j].append(v_p[j][i]-vector(0, 0.1 * L, 0))
 
t = 0
dt = 1
while t < 30:
    rate(100000)
    if x <= L:
        for j in range(nj):
            for i in range(n2):
                dv[j][i] = k * sigma * (dx * dz) * (1/mag(v_p[j][i]-(x, d, 0))-1/mag(v_p[j][i]-(x, 0, 0)))
                v[j][i] += dv[j][i]
        x += dx
    else:
        for j in range(nj):
            for i in range(n2):
                if v[j][i]>v0[j] and abs(v[j][i]-v0[j]) >= v_v0:
                    v_h[j][i] = v_p[j][i]
                    v_p[j][i] = (v_p[j][i]+v_l[j][i])/2
                    v[j][i] = 0
                elif v[j][i]<v0[j] and abs(v[j][i]-v0[j]) >= v_v0:
                    v_l[j][i] = v_p[j][i]
                    v_p[j][i] = (v_p[j][i]+v_h[j][i])/2
                    v[j][i] = 0
                elif abs(v[j][i]-v0[j])<v_v0:
                    v_line2[j][i].pos = (-v_p[j][i].x+L, v_p[j][i].y, v_p[j][i].z)
                    v_line3[j][i].pos = (v_p[j][i].x, -v_p[j][i].y+d, v_p[j][i].z)
                    v_line4[j][i].pos = (-v_p[j][i].x+L, -v_p[j][i].y+d, v_p[j][i].z)
                v_line[j][i].pos = v_p[j][i]
        x = 0
        t += dt
print "The potential of lines are", 0, delv0, 2 * delv0, 3 * delv0, 4 * delv0 

# capitance
print "(L = 1cm, d = 2mm)"
print "capacity in theory =  ", (E0 * dz * L/d)/dz, "        (per unit z)"

q3 = sigma * L * dz
p3 = vector(0.5 * L, d/2, 0)
E3 = vector(0, 0, 0)
v3 = 0
ball3 = sphere(pos = p3, radius = 0.01 * L)
while p3.y > 0:
    rate(100000)
    if x <= L:
        r_p3 = p3 - (x, d, 0)
        r_n3 = p3 - (x, 0, 0)
        dE3 = k * sigma * (dx * dz) * (norm(r_p3)/mag2(r_p3)-norm(r_n3)/mag2(r_n3))
        E3 += dE3
        x += dx
    else:
        p3 += norm(E3) * ds
        v3 += dot(E3, norm(E3) * ds)
        E3 = vector(0, 0, 0)
        x = 0
        ball3.pos = p3
print v3
print "capacity =            ", (q3/(2 * v3))/dz, "(per unit z)"
