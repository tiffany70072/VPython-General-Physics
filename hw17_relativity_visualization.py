from __future__ import division
from visual import*


c = 3E8
g = 9.8                         # acceleration of the spaceship
dts = 1000                      # delta t for spaceship
year = 3600*24*365
# S = 4.24*(c)*year 
ly = 9.4605284E15
S = 4.24*ly                     # distance between earth and star
# print S
dv = g*dts                      # delta velocity through delta t

# counting
vs = 0                          # speed(spaceship)
ve = 0                          # speed(the earth)
ts = 0
te = 0
Ss = 0                          # distance(spaceship)
Se = 0                          # distance(the earth)

# visual
scene = display(center = (S/2, 0, 0), width = 700)
r = S/70                        # size of the earth and star
d = S/30

ship_s  = sphere(pos = (Ss, d, 0), color = color.orange, radius = r, make_trail = True)
ship_e  = sphere(pos = (Se, -d, 0), color = color.cyan, radius = r, make_trail = True)
earth_s = sphere(pos = (0, d, 0), color = color.blue, radius = r)
earth_e = sphere(pos = (0, -d, 0), color = color.blue, radius = r)
star_s  = sphere(pos = (S, d, 0), color = color.yellow, radius = r)
star_e  = sphere(pos = (S, -d, 0), color = color.yellow, radius = r)

def gamma(v):
    gam = (1-(v/c)**2)**(-1/2)
    return gam

def v_acc(v):
    v_new = (v + dv)/(1 + dv*v/(c**2))
    return v_new

def v_dec(v):
    v_new = (v-dv)/(1-dv*v/(c**2))
    return v_new

f1 = 0                          # arrive(spaceship)
f2 = 0                          # arrive(the earth)
f3 = 0                          # deceleration(spaceship)
f4 = 0                          # deceleration(the earth)
n = 0
print "acceleration"

# main
while f1 == 0 or f2 == 0:
    rate(10000000)
    
# for spaceship:
    if Ss <= S:
        vs0 = vs
        if Ss <= S/2:
            v = vs
            vs = v_acc(v)             # v_new
        else:
            if f3 == 0:
                print "deceleration for spaceship, vs_max = ", vs/c, "c"
                f3 = 1
            v = vs
            vs = v_dec(v)             # v_new
        ts += dts
        Ss += (vs0 + vs)/2*dts*gamma(vs)
    else:
        f1 = 1
       
    # for earth
    if Se <= S:
        ve0 = ve
        if Se <= S/2:
            v = ve
            ve = v_acc(v)             # v_new
        else:
            if f4 == 0:
                print "deceleration for the earth, ve_max = ", ve/c, "c"
                v = ve
                print "gamma_earth_max = ", gamma(ve)
                f4 = 1
            v = ve
            ve = v_dec(v)             # v_new
        dte = dts*gamma(ve)
        te += dte
        Se += (ve0 + ve)/2*dte
    else:
        f2 = 1

    ship_s.pos = vector(Ss, d, 0)
    ship_e.pos = vector(Se, -d, 0)
    
print
print "come and back(for years)"
print "ts = ", ts*2/year, "(years)"
print "te = ", te*2/year, "(years)"
print "ts in theory = 7.081(years)"
print "te in theory = 11.71(years)"
