from math import *
from random import random
from visual import *
from visual.graph import *


# Define physics coefficients.
m = 4E-3 / (6E23)                 # Mass of particles.
k = 1.4E-23                       # Boltzmann constant.   
r = 0.02                          # Real radius of atom.
size = 0.025                      # Radius of atom for visualization.
T = 300                           # Temperature.
N = 100                           # Number of atoms.
L = 1.0                           # Size of the box.
dL = 1.0 / 5                      # Visiualization of the box.
A = L ** 2 * 6                    # Total area of the box.
V_box = L ** 3                    # Volume of the box.
V_atom = (4 / 3) * pi * r ** 3    # Calculate the volume of all atoms.
V = V_box - V_atom                # Real empty volume.


# Define colors.
side = (0.0, 0.0, 0.0)      # Color of the box.
col_pink = 0.9              # Color of hot atom.
col_blue = 1.4              # Color of cold atom.
col_back = (0.5, 0.5, 0)    # Color of background.


# Define time related variable.
t = 0
dt = 1E-5
times = 0     
dP = 0                      # Initial momentom.
dPx = 0      
dPy = 0
dPz = 0


# Main window.
scene = display(title="Gas", width=600, height=600, x=0, y=0, center=(L/2, L/2, L/2), background=col_back)
deltav = 80
vdist = gdisplay(width=600, height=0.6 * 600, x=600, y=0, ymax=N * deltav / 1000, 
               xtitle='v', ytitle='dN', background=col_back)
theory = gcurve(color=color.green)
dv = 10

for v in range(0, 3601 + dv, dv):
    theory.plot(pos = (v, (deltav / dv) * N * 4 * pi * ((m / (2 * pi * k * T)) ** 1.5)
                     * exp((-0.5 * m * v ** 2) / (k * T)) * v ** 2 * dv))

    
# Construct the histogram.
observation = ghistogram(bins=arange(0, 3600, deltav), accumulate=1, average=1, color=color.red)


# Draw the box.
xaxis = curve(pos=[(0, 0, 0), (L, 0, 0)], color=side)
yaxis = curve(pos=[(0, 0, 0), (0, L, 0)], color=side)
zaxis = curve(pos=[(0, 0, 0), (0, 0, L)], color=side)
box1 = curve(pos=[(L, L, L), (L, L, 0), (0, L, 0), (0, L, L)], color=side)
box2 = curve(pos=[(L, L, L), (L, 0, L), (L, 0, 0), (L, L, 0)], color=side)
box2 = curve(pos=[(L, L, L), (0, L, L), (0, 0, L), (L, 0, L)], color=side)
box_visual = curve(pos=[(L+dL, L+dL, L), (L+dL, -dL, L), (-dL, -dL, L), (L+dL, -dL, L)], color=col_back)
      
  
# Simulate the collision between two atoms.
def collision(v1, v2, x1, x2):
    v1f = v1 + (x2 - x1) * dot(v2 - v1, x2 - x1) / dot(x2 - x1, x2 - x1)
    v2f = v2 + (x1 - x2) * dot(v1 - v2, x1 - x2) / dot(x1 - x2, x1 - x2)
    return (v1f, v2f)

  
# Initialize the containers for atoms.
atom = []
color = []
pos = []
v = []
dv = []
vmag = list(range(N))


# Initialize setting of atoms.
for i in range(N):
    x = r + (L - 2 * r) * random()
    y = r + (L - 2 * r) * random()
    z = r + (L - 2 * r) * random()
    
    vrms = sqrt(3.0 * k * T / m)
    theta1 = 2 * pi * random()
    theta2 = 2 * pi * random()
    vx = vrms * cos(theta1) * cos(theta2)
    vy = vrms * cos(theta1) * sin(theta2)
    vz = vrms * sin(theta1)

    pos.append(vector([x, y, z]))
    v.append(vector([vx, vy, vz]))
    dv.append(0)
    # atom.append(sphere(pos=(x, y, z), radius=size, color=(0.7 + abs(vx / vrms) / 2, 0.7 + abs(vy / vrms) / 2, 0.5 + abs(vz / vrms) / 2)))
    atom.append(sphere(pos=(x, y, z), radius=size, color=(1, 1 - mag(v[i]) / vrms, 1 - mag(v[i]) / vrms)))
print vrms


# Main simulation.
while true:
    rate(100)
    t += dt
    times += 1
    
    for i in range(N):
        pos[i] = pos[i] + v[i] * dt
        atom[i].pos = pos[i]
        atom[i].color = (1, col_blue - mag(v[i]) / vrms / (col_pink), col_blue - mag(v[i]) / vrms / (col_pink))
        vmag[i] = mag(v[i])
    observation.plot(data=vmag)

    for i in range(N):
        # Collision between two atoms.
        for j in range(i + 1, N):
            if mag(pos[i] - pos[j]) <= 2 * r and dot(pos[i] - pos[j], v[i] - v[j]) < 0:
                v1 = v[i]
                v2 = v[j]
                x1 = pos[i]
                x2 = pos[j]
                (v[i], v[j]) = collision(v1, v2, x1, x2)

        # Collision between one atom and the wall.          
        if (pos[i].x <= 0 and v[i].x < 0) or (pos[i].x >= L and v[i].x > 0):
            v[i] += vector(-2 * v[i].x, 0, 0)
            dPx += 2 * m* abs(v[i].x)
        if (pos[i].y <= 0 and v[i].y < 0) or (pos[i].y >= L and v[i].y > 0):
            v[i] += vector(0, -2 * v[i].y, 0)
            dPy += 2 * m * abs(v[i].y)
        if (pos[i].z <= 0 and v[i].z < 0) or (pos[i].z >= L and v[i].z > 0):
            v[i] += vector(0, 0, -2 * v[i].z)
            dPz += 2 * m * abs(v[i].z)
            
    # Calculate the pressure on the wall due to atoms collision.
    if times == 100:
        dP = dPx + dPy + dPz  # Calculate total momentum.
        p = dP / t / A  # Calculate pressure.
        print "pV = ", p * V, "NkT = ", N * k * T  # Verify if pV = NkT.
        times = 0
        
