from __future__ import division
from visual import *

scene = display(title = "flux (Gauss' law) ", width = 500, height = 500, 
              range = (2, 2, 1), background = (0, 0.2, 0.3))

L = 1.0
E0 = 8.854E-12      # epsilon
k = 1/(4*pi*E0)

Q = 0
flux_side = 0
flux_up = 0

x0 = -L/2
x = -L
y = 0
dx0 = 0.0025
dx = dx0
dy = dx0
rat = 1000000

A = 2 * pi * L * dx * vector(0, 1, 0)
E_side = vector(0, 0, 0)
E_up = vector(0, 0, 0)
rod = cylinder(pos = (x0, 0, 0), axis = (L, 0, 0), radius = L/30, color = color.cyan)
bottle = cylinder(pos = (-L, 0, 0), axis = (2*L, 0, 0), radius = L, 
                color = color.white, opacity = 0.3)
t = arange(0, 2 * pi, 0.01)
ring1 = curve(x = x, y = cos(t), z = sin(t), color = color.red)
ring2 = curve(x = x, y = cos(t)*y, z = sin(t)*y, color = color.red)
xaxia = curve(pos = [(-3, 0, 0), (3, 0, 0)], color = color.white)

while y <= L:
    rate(rat)
    if x0 <= L/2:
        lam = (1E-6) * (sin(pi*x0/L))**2
        dE_up = k * lam * dx/(y**2 + (x0-(-L))**2) * norm(vector(-L, y, 0) - vector(x0, 0, 0))
        E_up += dE_up
        x0 += dx
    else:
        A_up = 2 * pi * y * dy * vector(-1, 0, 0)
        flux_up += dot(E_up, A_up)
        E_up = vector(0, 0, 0)
        # A += A_up
        x0 = -L/2
        y += dy
        ring2.y = cos(t) * y
        ring2.z = sin(t) * y
print "flux_up  =  flux_down  = ", flux_up

print "A = ", mag(A)   
while x <= L:
    rate(rat)
    if x0 <= L/2:
        lam = (1E-6) * (sin(pi*x0/L))**2
        dE_side = k * lam * dx/(L**2+(x0-x)**2) * norm(vector(x, L, 0) - vector(x0, 0, 0))
        E_side += dE_side
        x0 += dx
    else:
        # print E
        flux_side += dot(E_side, A)
        E_side = vector(0, 0, 0)
        x0 = -L/2
        x += dx
        ring1.x = x
print "flux_side  = ", flux_side

while x0 <= L/2:
    rate(rat)
    lam = (1E-6)*(sin(pi*x0/L))**2
    q = lam * dx
    Q += q
    x0 += dx


print "total flux  = ", 2 * flux_up + flux_side
print "Q/epsilon = ", Q/E0
      


    
    
