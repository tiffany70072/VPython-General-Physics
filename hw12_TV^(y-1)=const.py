from __future__ import division
from visual import *
from visual.graph import *
from math import *
from random import random

m = 4E-3/(6E23)     # mass
k = 1.4E-23         # boltzmann constant
#r = 0.03           # radius of atom
r = 0.03
size = 0.025        # radius of atom for visual
T = 300             # temperature
N = 100             # atom number
L = 1.0             # side of the box
dL = 1.0/5          # visiualization of the box
A_final = 6*L**2          # total area of the box
V_box = L**3              # volume of the box
V_atom = (4/3)*pi*r**3*N  # volume of all the atom
V_final = V_box-V_atom          # real volume

#color
side = (0.0, 0.0, 0.0)      # color of the box
col_pink = 0.9            # color of hot atom
col_blue = 1.4            # color of cold atom
col_back = (0.5, 0.5, 0)    # color of background
col_wall = (0, 0, 0.5)
#time
t = 0
dt = 1E-5
times = 0     
dP = 0            #initial momentom


# moving wall
t_move = 0.005      #when the wall starts to move
s = 0             #print when the wall starts to move
wall_x = L        #this wall will move
v_wall2 = 5     #how fast the wall moves
v_wall = 0.0      #to find when the wall will move
Cv = 1.5          #the molar specific heat of a monatomic gas at constant volume
Cp = Cv+1         #the molar specific heat of a monatomic gas at constant pressure
gamma = Cp/Cv

# find the temperature
Ek = 0
Ektot = 0
Tf = (2.0**(gamma-1))*T   #Theoretical value of final temperature
print "Theoretical value of final temperature = ", Tf
# main window
scene = display(title = "Gas", width = 600, height = 600, x = 0, y = 0, center = (L/2, L/2, L/2), background = col_back)
deltav = 80
vdist = gdisplay(width = 600, height = 0.6*600, x = 600, y = 0, ymax = N*deltav/1000, 
               xtitle = 'v', ytitle = 'dN', background = col_back)
theory = gcurve(color = color.green)
theory2 = gcurve(color = color.blue)
dv = 10

for v in range(0, 3601+dv, dv):
    theory.plot(pos = (v, (deltav/dv)*N*4*pi*((m/(2*pi*k*T))**1.5)
                     * exp((-0.5*m*v**2)/(k*T))*v**2*dv))
    theory2.plot(pos = (v, (deltav/dv)*N*4*pi*((m/(2*pi*k*Tf))**1.5)
                     * exp((-0.5*m*v**2)/(k*Tf))*v**2*dv))

# do the histogram
observation = ghistogram(bins = arange(0, 3600, deltav), accumulate = 1, average = 1, color = color.red)

# draw the box
xaxis = curve(pos = [(0, 0, 0), (L, 0, 0)], color = side)
yaxis = curve(pos = [(0, 0, 0), (0, L, 0)], color = side)
zaxis = curve(pos = [(0, 0, 0), (0, 0, L)], color = side)
wall1 = curve(pos = [(L, 0, L), (L, 0, 0), (L, L, 0), (L, L, L)], color = side)
wall2 = curve(pos = [(L, L, L), (L, L, 0), (0, L, 0), (0, L, L), (L, L, L)], color = side)
wall3 = curve(pos = [(L, L, L), (0, L, L), (0, 0, L), (L, 0, L), (L, L, L)], color = side)
box_visual = curve(pos = [(L+dL, L+dL, L), (L+dL, -dL, L), (-dL, -dL, L), (L+dL, -dL, L)], color = col_back)
wall = box(pos = (wall_x+L/200, L/2, L/2), length = L/100, width = L, height = L, color = col_wall) #this wall will move

           
# collision
def collision(v1, v2, x1, x2):
    v1f = v1+(x2-x1)*dot(v2-v1, x2-x1)/dot(x2-x1, x2-x1)
    v2f = v2+(x1-x2)*dot(v1-v2, x1-x2)/dot(x1-x2, x1-x2)
    return (v1f, v2f)

# initial list for atom
atom = []
color = []
pos = []
v = []
dv = []
vmag = list(range(N))

# initial setting for atom
for i in range(N):
    
    x = r+(L-2*r)*random()
    y = r+(L-2*r)*random()
    z = r+(L-2*r)*random()
    
    vrms = sqrt(3.0*k*T/m)
    theta1 = 2*pi*random()
    theta2 = 2*pi*random()
    vx = vrms*cos(theta1)*cos(theta2)
    vy = vrms*cos(theta1)*sin(theta2)
    vz = vrms*sin(theta1)

    pos.append(vector([x, y, z]))
    v.append(vector([vx, vy, vz]))
    dv.append(0)
    atom.append(sphere(pos = (x, y, z), radius = size, 
                       color = (1, col_blue-mag(v[i])/vrms/(col_pink), col_blue-mag(v[i])/vrms/(col_pink))))
print "vrms = ", vrms, "(m/s)"
print "NkT = ", N*k*T

# main program
while 1:
    rate(1000)
    t += dt
    times += 1
    
    for i in range(N):
        pos[i] = pos[i]+v[i]*dt
        atom[i].pos = pos[i]
        atom[i].color = (1, col_blue-mag(v[i])/vrms/(col_pink), col_blue-mag(v[i])/vrms/(col_pink))
        vmag[i] = mag(v[i])
    observation.plot(data = vmag)
    
# the wall is moving
    if t >= t_move and wall_x >= L/2:#t<(L/2/v_wall2)+t_move:
        if s == 1:
                print "the wall starts moving."
                s = 2
        v_wall = v_wall2
    else:
        v_wall = 0.0
        
    wall_x += -v_wall*dt
    wall.pos.x = wall_x+L/200
    A_final = 2*(L**2)+4*(wall_x*L)
    V_final = wall_x*(L**2)

    for i in range(N):
# collision for atom and atom
        for j in range(i+1, N):
            if mag(pos[i]-pos[j]) <= 2*r and dot(pos[i]-pos[j], v[i]-v[j])<0:
                v1 = v[i]
                v2 = v[j]
                x1 = pos[i]
                x2 = pos[j]
                (v[i], v[j]) = collision(v1, v2, x1, x2)
                
# TV*(y-1)
# collision for atom and wall          
        if (pos[i].x <= 0 and v[i].x <= 0):
            v[i] += vector(-2*v[i].x, 0, 0)
        if (pos[i].x >= wall_x and v[i].x >= 0):
            v[i] += vector(-2*(v[i].x+v_wall), 0, 0)
        if (pos[i].y <= 0 and v[i].y <= 0) or (pos[i].y >= L and v[i].y >= 0):
            v[i] += vector(0, -2*v[i].y, 0)
        if (pos[i].z <= 0 and v[i].z <= 0) or (pos[i].z >= L and v[i].z >= 0):
            v[i] += vector(0, 0, -2*v[i].z)

        Ektot += (m*(mag(v[i]))**2)/2
# find the temperature 
    if times == 1000:
        Tf = 2/(3*N*k)*Ektot/times
        if t<t_move:
            print "T*V^(gamma-1) = ", Tf*(V_final**(gamma-1))
        if s == 0:
            print "initial T*V^(gamma-1) = ", Tf*(V_final**(gamma-1))
            print "initial V = ", V_final
            s = 1
        if t>t_move:
            
            if wall_x >= L/2:
                print "T = ", Tf
                print "T*V^(gamma-1) = ", Tf*(V_final**(gamma-1)), "V = ", V_final, "(m**3)"
            if wall_x<L/2 and s == 2:
                print "the wall stops moving."
                print "V_final = ", V_final, "(m**3)"
                s = 3
            if wall_x<L/2:
                print "T*V^(gamma-1) = ", Tf*(V_final**(gamma-1))
        times = 0                                        # restart
        Ektot = 0

