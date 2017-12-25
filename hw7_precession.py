from __future__ import division
from visual import * 
from math import * 

scene = display(forward = (0.5, -0.5, 0), background = (1, 1, 0.5))

earth_m = 5.972 * 10**24
earth_r = 6357000
sun_m = 1.989 * 10**30
sun_x = 1.495 * 10**11 * vector(1, 0, 0)
sun_pos = sun_x
moon_m = 7.36 * 10**22
moon_x = 3.844 * 10**8 * vector(1, 0, 0)
moon_pos = moon_x
G  = 6.673 * 10**(-11)
au = 1.495 * 10**11
size = 0.05 * au
the1 = 66.5 * pi/180
the2 = pi/4

earth = sphere(pos = (0, 0, 0), radius = size, color = color.blue)
sun_velocity = (G * sun_m/mag(sun_x))**(1/2) * vector(0, 1, 0)
moon_velocity = (G * earth_m/mag(moon_x))**(1/2) * vector(0, 1, 0)

earth_I = 4/9 * pi * (earth_r)**5 * 5500
earth_L = earth_I * 2 * pi/86400 * vector(cos(the1), sin(the1), 0)

belt_m = 2.706092648 * 10**22
dm = belt_m/8

print "earth's I = ", earth_I
print "earth's angular momentum = ", earth_L

t = 0
dt = 86400
sun_T = vector(0, 0, 0)
moon_T = vector(0, 0, 0)
sun_L_year = vector(0, 0, 0)
moon_L_year = vector(0, 0, 0)

#sun
while True:
        rate(3000)
        t += dt

        sun_acc = G * sun_m/(mag(sun_pos))**2 * (-1) * norm(sun_pos)
        sun_velocity += sun_acc * dt
        sun_x += sun_velocity * dt

        dm_1 = rotate((0, 0, earth_r), angle = 0 * the2, axis = earth_L)
        f_1 = G * dm * sun_m/(mag(dm_1-sun_pos)**2) * norm(sun_pos-dm_1)
        T_1 = cross(dm_1, f_1)

        dm_2 = rotate((0, 0, earth_r), angle = 1 * the2, axis = earth_L)
        f_2 = G * dm * sun_m/(mag(dm_2-sun_pos)**2) * norm(sun_pos-dm_2)
        T_2 = cross(dm_2, f_2)

        dm_3 = rotate((0, 0, earth_r), angle = 2 * the2, axis = earth_L)
        f_3 = G * dm * sun_m/(mag(dm_3-sun_pos)**2) * norm(sun_pos-dm_3)
        T_3 = cross(dm_3, f_3)

        dm_4 = rotate((0, 0, earth_r), angle = 3 * the2, axis = earth_L)
        f_4 = G * dm * sun_m/(mag(dm_4-sun_pos)**2) * norm(sun_pos-dm_4)
        T_4 = cross(dm_4, f_4)

        dm_5 = rotate((0, 0, earth_r), angle = 4 * the2, axis = earth_L)
        f_5 = G * dm * sun_m/(mag(dm_5-sun_pos)**2) * norm(sun_pos-dm_5)
        T_5 = cross(dm_5, f_5)

        dm_6 = rotate((0, 0, earth_r), angle = 5 * the2, axis = earth_L)
        f_6 = G * dm * sun_m/(mag(dm_6-sun_pos)**2) * norm(sun_pos-dm_6)
        T_6 = cross(dm_6, f_6)

        dm_7 = rotate((0, 0, earth_r), angle = 6 * the2, axis = earth_L)
        f_7 = G * dm * sun_m/(mag(dm_7-sun_pos)**2) * norm(sun_pos-dm_7)
        T_7 = cross(dm_7, f_7)

        dm_8 = rotate((0, 0, earth_r), angle = 7 * the2, axis = earth_L)
        f_8 = G * dm * sun_m/(mag(dm_8-sun_pos)**2) * norm(sun_pos-dm_8)
        T_8 = cross(dm_8, f_8)
        
        T = T_1+T_2+T_3+T_4+T_5+T_6+T_7+T_8
        sun_T += T

        #stop
        if sun_x.y * (sun_pos+sun_velocity * dt).y<0 and sun_x.y<0: break
        sun_L_year = sun_T * 86400 * 365

#moon
while True:
        rate(10000)
        t += dt

        moon_acc = G * earth_m/(mag(moon_pos))**2 * (-1) * norm(moon_pos)
        moon_velocity += moon_acc * dt
        moon_x += moon_velocity * dt
        
        sun_acc = G * sun_m/(mag(sun_pos))**2 * (-1) * norm(sun_pos)
        sun_velocity += sun_acc * dt
        sun_x += sun_velocity * dt

        dm_1 = rotate((0, 0, earth_r), angle = 0 * the2, axis = earth_L)
        f_1 = G * dm * moon_m/(mag(dm_1-moon_pos)**2) * norm(moon_pos-dm_1)
        T_1 = cross(dm_1, f_1)

        dm_2 = rotate((0, 0, earth_r), angle = 1 * the2, axis = earth_L)
        f_2 = G * dm * moon_m/(mag(dm_2-moon_pos)**2) * norm(moon_pos-dm_2)
        T_2 = cross(dm_2, f_2)

        dm_3 = rotate((0, 0, earth_r), angle = 2 * the2, axis = earth_L)
        f_3 = G * dm * moon_m/(mag(dm_3-moon_pos)**2) * norm(moon_pos-dm_3)
        T_3 = cross(dm_3, f_3)

        dm_4 = rotate((0, 0, earth_r), angle = 3 * the2, axis = earth_L)
        f_4 = G * dm * moon_m/(mag(dm_4-moon_pos)**2) * norm(moon_pos-dm_4)
        T_4 = cross(dm_4, f_4)

        dm_5 = rotate((0, 0, earth_r), angle = 4 * the2, axis = earth_L)
        f_5 = G * dm * moon_m/(mag(dm_5-moon_pos)**2) * norm(moon_pos-dm_5)
        T_5 = cross(dm_5, f_5)

        dm_6 = rotate((0, 0, earth_r), angle = 5 * the2, axis = earth_L)
        f_6 = G * dm * moon_m/(mag(dm_6-moon_pos)**2) * norm(moon_pos-dm_6)
        T_6 = cross(dm_6, f_6)

        dm_7 = rotate((0, 0, earth_r), angle = 6 * the2, axis = earth_L)
        f_7 = G * dm * moon_m/(mag(dm_7-moon_pos)**2) * norm(moon_pos-dm_7)
        T_7 = cross(dm_7, f_7)

        dm_8 = rotate((0, 0, earth_r), angle = 7 * the2, axis = earth_L)
        f_8 = G * dm * moon_m/(mag(dm_8-moon_pos)**2) * norm(moon_pos-dm_8)
        T_8 = cross(dm_8, f_8)

        T = T_1+T_2+T_3+T_4+T_5+T_6+T_7+T_8
        moon_T += T
        #stop
        if sun_x.y * (sun_pos+sun_velocity * dt).y<0 and sun_x.y<0:
                break
        moon_L_year = moon_T * 86400 * 365

#sun + moon
print "sun L/moon L = ", mag(sun_L_year)/mag(moon_L_year)

L_year = sun_L_year+moon_L_year
print L_year
#print mag(L_year)

#L_com = (earth_L.x, 0, earth_L.z)
#deltaL = norm(cross(L_com, earth_L)) * mag(L_year)
#print L_com
#print "delta L for a year from sun and moon = ", deltaL
#print earth_L+deltaL

tt = 0
dtt = 86400 * 365
while True:
        rate(10000)
        tt += dtt
        L_com = norm(vector(earth_L.x, 0, earth_L.z))
        deltaL = norm(cross(L_com, norm(earth_L))) * mag(L_year)
        earth_L += deltaL
        np = arrow(axis = norm(earth_L) * size * 2, shaftwidth = size * 0.05, color = color.white)
        if earth_L.z * (earth_L+deltaL).z<0 and earth_L.z<0: break

print "precession T=", tt/86400/365, "years"#, earth_L, deltaL

 
        

