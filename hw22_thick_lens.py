from __future__ import division
from visual import *

scene = display(title = "RAY", background = (0.1, 0.3, 0.5), width = 1200, height = 300, 
              center = (3, 0, 10), fov = 0.004, range = (10, 1, 1))

R = 4
r = 1E-3
thick = 0.3                                  #thickness of lens
c1 = vector(-R + thick/2, 0, 0)                   #center of right side
c2 = vector(+R - thick/2, 0, 0)
curve_range = [0.005*t for t in range(259, 314)]
len1 = [(+R*cos(th), +R * sin(th)) for th in curve_range]
len2 = [(-R*cos(th), -R * sin(th)) for th in curve_range]
circle1 = paths.arc(pos = c1, radius = r, angle2 = 2*pi, up = (1, 0, 0))
circle2 = paths.arc(pos = c2, radius = r, angle2 = 2*pi, up = (1, 0, 0))
extrusion(pos = circle1, shape = len1, color = color.cyan)
extrusion(pos = circle2, shape = len2, color = color.cyan)
curve (pos = [(-7, 0, 0), (13, 0, 0)], color = color.red, redius = 0.02)
arrow (pos = (-6, 0, 0), axis = (0, 0.25, 0), shaftwidth = 0.1, color = color.yellow)

def refraction(n1, n2, v_in, normal):
    vN = dot(v_in, normal)/mag2(normal)*normal
    vT1 = v_in - vN
    sinth1 = mag(vT1)/mag(v_in)
    th2 = asin(n1/n2*sinth1)
    vT2 = norm(vT1)*mag(vN)*tan(th2)
    return norm(vN + vT2)

p = []
v = []
f = []
n = 1.5                 #n of glass
N = 7                   #number of rays
s = 1                   #opening
ss = []
ray  = []
ray2 = []
dt = 0.0005

# find focus
for i in range(N):
    p.append(vector(-6, 0.5-1/(N-1)*i, 0))
    v.append(vector(1, 0, 0))
    f.append(0)
    ray.append(sphere(pos = p[i], radius = 0.01, make_trail = 1, color = color.white))    
    ray[i].trail_object.display = scene

while 1:
    rate(1000000)
    for i in range(N):
        p[i] = p[i]+v[i]*dt
        ray[i].pos = p[i]
        
        if mag(p[i]+v[i]*dt-c2) <= R and mag(p[i]-c2) >= R:
            v[i] = refraction(1, n, v[i], c2-p[i])
        if mag(p[i]+v[i]*dt-c1) >= R and mag(p[i]-c1) <= R:
            v[i] = refraction(n, 1, v[i], p[i]-c1)
        if p[i].y * (p[i]+v[i]*dt).y < 0:
            f[i] = p[i].x
    if p[3].x>13: break
    
f = sum(f)/(N-1)               #for p3.y always = 0
print "focus = ", f, "(cm)"

# find image
for i in range(N):
    p[i] = vector(-6, 0.25, 0)
    v[i] = vector(cos(-0.125+0.175/(N-1)*i), sin(-0.125+0.175/(N-1)*i), 0)    
    ray2.append(sphere(pos = p[i], radius = 0.007, make_trail = 1, color = color.orange))
    ss.append(0)

while True:
    rate(1000000)
    for i in range (N):
        p[i] = p[i]+v[i]*dt
        ray2[i].pos = p[i]
       
        if mag(p[i]+v[i]*dt-c2) <= R and mag(p[i]-c2) >= R:
            v[i] = refraction(1, n, v[i], c2-p[i])
        if mag(p[i]+v[i]*dt-c1) >= R and mag(p[i]-c1) <= R:
            v[i] = refraction(n, 1, v[i], p[i]-c1)
        if p[0].y > p[N-1].y and s == 1:
            i1 = p[0]
            iN = p[N-1]
            I = (i1+iN)/2
            s = 2
        #if p[i].x> = I and ss[i] = = 0:
            #print p[i]
            #ss[i] = 1
    if p[3].x>13: break

print "image = ", I, ", m = ", I.y/0.25
print "p = 6"
print "i = ", I.x
print "1/f = ", 1/f
print "1/p+1/i = ", 1/6+1/I.x
print "f(theoretical) = 4, error = ", (f-4)/4*100, "%"
print "i(theoretical) = 12, error = ", (I.x-12)/12*100, "%"

while True:                 #print the image
    rate(1)
    ii = arrow(pos = (I.x, 0, 0), axis = (0, I.y, 0), shaftwidth = 0.1, color = color.yellow) 
        
