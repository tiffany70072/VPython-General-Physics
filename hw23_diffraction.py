from __future__ import division
import pylab as plt
import numpy as np
from math import *

R   = 1
d   = 50E-6                        # diameter of circle aperture
lam = 500E-9                       # wavelength of light
k   = 2*np.pi/lam
phi = 1                            # wt-kR
N   = 100                          # (x, y) for screen(100~200)
M   = int(N/2)                     # y = 0
N0  = 100                          # (x0, y0) for point light(50~200)
s   = 0                            # opening

side = np.linspace(-0.01 * np.pi, 0.01 * np.pi, N)
x, y = np.meshgrid(side, side)
E = (0*x)

#circular apeture
apet = np.linspace(-d/2, d/2, N0)
x0, y0 = np.meshgrid(apet, apet)
for m0 in range(N0):
    for n0 in range(N0):
        if x0[m0, n0]**2+y0[m0, n0]**2>(d/2)**2:
            x0[m0, n0] = 0
            y0[m0, n0] = 0
"""
# single slit
apetx = np.linspace(-d/2, d/2, N0)
apety = np.linspace(-d/20, d/20, N0)
x0, y0 = np.meshgrid(apetx, apety)

#double slit
apetx = np.linspace(-d/2, d/2, N0)
apety = np.linspace(-d/10, d/10, N0)
x0, y0 = np.meshgrid(apetx, apety)
for m0 in range(N0):
    for n0 in range(N0):
        if abs(y0[m0, n0])<d/20:
            x0[m0, n0] = 0
            y0[m0, n0] = 0
"""
# calculate E field 
for m in range(N):
    for n in range(N):
        E[m, n] = np.sin(phi)*np.sum(np.cos(k*x[m, n]*x0/R+k*y[m, n]*y0/R))
            + np.cos(phi)*np.sum(np.sin(k*x[m, n]*x0/R+k*y[m, n]*y0/R))
        
# calculte Rayleigh criterion
# (if you choose circular apeture,  please open it)       

for m in range(int(0.45*N), int(0.6*N)):
    if E[m, M] <= E[m-1, M] and s == 0 :
        s = 1
        bright = m
for m in range(bright+1, N):
    if E[m, M] >= E[m-1, M] and s == 1:   
        s = 2
        dark = m
        
theta = atan(x[M, dark]-x[M, bright])/R
print "Rayleigh theta  = ", theta
print "thereom         = ", 1.22 * lam/d
print "error           = ", (theta-1.22*lam/d)/(1.22*lam/d)*100, "%"

# calculate intensity and plot 
I = abs(E)**2 
f1 = plt.figure(1)
plt.pcolormesh(x, y, I)
f1.show()
f2 = plt.figure(2)
plt.gray()
plt.pcolormesh(x, y, I)
f2.show()
f3 = plt.figure(3)
plt.pcolormesh(x, y, np.sqrt(I))
f3.show()
plt.show()
