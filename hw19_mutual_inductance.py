from __future__ import division
from visual import*

R  = 0.10                                #radius of big ring
r  = 0.05                                #radius of small ring
z  = 0.2     
I  = 1                                   #(A)
u0 = 4*pi*10**(-7)
k  = u0/4/pi

m  = 100                                  #cut circle into m rings
n  = 60                                   #cut rings into n pieces
dth = 2*pi/n                               #delta theta
p  = []                                   #the position of delta_area
r1 = []                                   #vector from ds to delta_area
ds = []                                   #vector of ds
dB = []            
dB_t = []                                 #total magnetic field of delta_area
dB_t2 =[]    
dflux = []                                #flux of delta_area
flux_total_big = 0
flux_total_small = 0


for j in range(m):
    p.append(vector(R*j/m, 0, 0))
    r1.append([])
    ds.append([])
    dB.append([])
    dB_t.append(vector(0, 0, 0))
    dflux.append(0)
    for i in range(n):
        r1[j].append(p[j] - vector(r*cos(i*dth), r*sin(i*dth), z))
        ds[j].append(r * dth * vector(-sin(i*dth), cos(i*dth), 0))
        dB[j].append(k * I * cross(ds[j][i], r1[j][i]) * mag(r1[j][i])**(-3))
        dB_t[j] += dB[j][i]
    dflux[j] = dot(dB_t[j], (0, 0, 2*pi*p[j].x*R/m))                #B2*dA1
    flux_total_small += dflux[j]
print "M12   = ",  flux_total_small, "(total flux of small ring/I)"


for j in range(m):
    p[j] = vector(r*j/m, 0, z)
    dB_t2.append(vector(0, 0, 0))
    for i in range(n):
        r1[j][i] = p[j] - R*vector(cos(i*dth), sin(i*dth), 0)
        ds[j][i] = R * dth * vector(-sin(i*dth), cos(i*dth), 0)
        dB[j][i] = k * I * cross(ds[j][i], r1[j][i]) * mag(r1[j][i])**(-3)
        dB_t2[j] += dB[j][i]
    dflux[j] = dot(dB_t2[j], (0, 0, 2*pi*p[j].x*r/m))
    flux_total_big += dflux[j]
print "M21   = ", flux_total_big, "(total flux of big ring/I)" 
print "error = ", (flux_total_big - flux_total_small)/flux_total_small * 100, "%"


