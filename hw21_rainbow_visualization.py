from __future__ import division
from visual import *

scene = display(title = "RAY", background = (0.8, 0.9, 1), width = 700, height = 700)

R  = 2
b  = 1.78
dt = 0.005
v0 = vector(1, 0, 0)
drop = sphere(pos = (0, 0, 0), color = (0.6, 0.7, 1), opacity = 0.4, radius = R)

def refraction(n1, n2, v_in, normal):
    vN = dot(v_in, normal)/mag2(normal)*normal
    vT1 = v_in - vN
    sinth1 = mag(vT1)/mag(v_in)
    th2 = asin(n1/n2*sinth1)
    vT2 = norm(vT1)*mag(vN)*tan(th2)
    return norm(vN + vT2)
    
def reflection(v_in, normal):
    vN = dot(v_in, normal)/mag2(normal)*normal
    return norm(v_in-2*vN)

for (ray_color, n_water) in [(color.red, 1.331), (color.blue, 1.339), 
                            (color.orange, 1.333), (color.yellow, 1.335), 
                            (color.green, 1.337), ((0.6, 0, 1), 1.342)]:
    ray = sphere(pos = (-5, b, 0), v = v0, color = ray_color, radius = 0.02, make_trail = True)
 
    while True:
        rate(4000)
        ray.pos += ray.v*dt

        if mag(ray.pos) >= R and mag(ray.pos + ray.v*dt) <= R:
            ray.v = refraction(1, n_water, ray.v, -ray.pos)

        if mag(ray.pos) <= R and mag(ray.pos + ray.v*dt) >= R and ray.pos.y > 0:
            ray.v = reflection(ray.v, ray.pos)
            s = 1

        if mag(ray.pos) <= R and mag(ray.pos + ray.v*dt) >= R and ray.pos.y < 0 and s == 1:
            ray.v = refraction(n_water, 1, ray.v, ray.pos)
            s = 2

        if ray.pos.y < -5:
            if ray_color == color.red: red = ray.v
            if ray_color == color.blue: blue = ray.v
            break
    
print "angle(red)  = ", 180-acos(dot(red , v0))*180/pi, "(degree)"
print "angle(blue) = ", 180-acos(dot(blue, v0))*180/pi, "(degree)"

scene2 = display(title = "RAY2", background = (0.8, 0.9, 1), width = 500, height = 500, x = 500)
drop = sphere(pos = (0, 0, 0), color = (0.6, 0.7, 1), opacity = 0.4, radius = R, display = scene2)
b    = []
s    = []              # opening
ray  = []
rayv = []
n    = 30
n_water = 1.334

for i in range(n):
    s.append(0)
    b.append(0.1 + i/(n-1)*1.88)
    rayv.append(v0)
    ray.append(sphere(pos = (-5, b[i], 0), radius = 0.02, make_trail = True, display = scene2))
    ray[i].trail_object.color = color.yellow

while s[i] != 4:
    for i in range(n):
        rate(1000000)
        if ray[i].pos.y >= -5 and ray[i].pos.x >= -5:
            ray[i].pos += rayv[i]*dt
        else:
            if i > 24 and i < 28: ray[i].trail_object.color = color.orange
            s[i] = 4
    
        if mag(ray[i].pos) > R and mag(ray[i].pos + rayv[i]*dt) < R and s[i] == 0:
            rayv[i] = refraction(1, n_water, rayv[i], -ray[i].pos)
            s[i] = 1

        if mag(ray[i].pos) < R and mag(ray[i].pos + rayv[i]*dt) > R and s[i] == 1:
            rayv[i] = reflection(rayv[i], -ray[i].pos)
            s[i] = 2

        if mag(ray[i].pos) < R and mag(ray[i].pos + rayv[i]*dt) > R and s[i] == 2:
            rayv[i] = refraction(n_water, 1, rayv[i], ray[i].pos)
            s[i] = 3

        if s[0] == 2:        # amplify rainbow
            scene.range = (0.5, 0.5, 0.5)
            scene.center = (0.5, -2, 0)

print "density(orange):b = ", b[25], "(cm)"
print "density(orange):b = ", b[26], "(cm)"
print "density(orange):b = ", b[27], "(cm)"
