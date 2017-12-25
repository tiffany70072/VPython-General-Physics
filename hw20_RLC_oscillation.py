from __future__ import division
from visual import *
from visual.graph import *
from math import *

print "RLC"
scene1 = gdisplay(x = 0, y = 0, width = 1000, height = 400, background = (0.3, 0.5, 0.5), xtitle = "t/T", ytitle = 'i blue, v red')
scene2 = gdisplay(x = 0, y = 400, width = 1000, height = 250, background = (0.3, 0.5, 0.5), xtitle = "t/T", ytitle = 'Energy', )
i_t = gcurve(color = color.blue, gdisplay = scene1)
v_t = gcurve(color = color.red, gdisplay = scene1)
E_t = gcurve(color = color.yellow, gdisplay = scene2)

R = 30
L = 230*10**(-3)
C = 15*10**(-6)

f = 60
T = 1/f
w = 2*pi*f

t = 0
dt = 1/(f*5000)

v = 36*sin(w*t)
q = 0
dq = 0
ddq = 0
n = 0
i_total = 0
s = 0        #opening

while t/T < 13:
    rate(10000)

    if t/T < 7:
        ddq0 = ddq
        i0 = i
        v0 = v
        v = 36*sin(w*t)
    else:
        v = 0
        
    ddq = (v-q/C-dq*R)/L
    dq += ddq*dt
    q += dq*dt

    i = dq
    E = (q**2)/(2*C) + (L*dq**2)/2
    i_t.plot(pos = (t/T, i))
    v_t.plot(pos = (t/T, v/100))
    E_t.plot(pos = (t/T, E))
    
   # Q1
    if ddq0*ddq < 0 and 5 <= t/T < 7 :
        n += 1
        i_total += abs(i)
   # Q2
    if i0*i <= 0 and t/T > 6 and s == 0:
        s = 1
        t1 = t       
    if v0*v <= 0 and t/T > 6 and s == 1:
        s = 2
        t2 = t       
   # Q3       
    if s == 2 and t/T >  = 7:
        s = 3
        E_7T = E       
    if s == 3 and E < E_7T/10:
        s = 4
        t3 = t 
            
    t += dt
    
print "I = ", i_total/n, "(A)"
print "phase angle = ", (t1-t2)/T*2, "(pi), (I relative to V)"      #, t1, t2, T
print "time of 10% energy = ", t3, "(sec), t/T = ", t3/T

# LC
print "LC"
scene1 = gdisplay(x = 0, y = 0, width = 1000, height = 350, background = (0.3, 0.5, 0.5), xtitle = "t", 
                ytitle = 'I:blue, vC:red(/100), q on C:yellow(*400)')
scene2 = gdisplay(x = 0, y = 350, width = 1000, height = 300, background = (0.3, 0.5, 0.5), xtitle = "t", 
                ytitle = 'E_total:yellow, E_L:orange, E_C:cyan, E_L(ave):red, E_C(ave):blue')
i_t     = gcurve(gdisplay = scene1, color = color.blue)
vc_t    = gcurve(gdisplay = scene1, color = color.red)
q_t     = gcurve(gdisplay = scene1, color = color.yellow)
E_t     = gcurve(gdisplay = scene2, color = color.yellow, )
EL_t    = gcurve(gdisplay = scene2, color = color.orange)
EC_t    = gcurve(gdisplay = scene2, color = color.cyan)
ELave_t = gcurve(gdisplay = scene2, color = color.red)
ECave_t = gcurve(gdisplay = scene2, color = color.blue)

L = 230*10**(-3)
C = 15*10**(-6)

t = 0
dt = 1/10000

q = 1          # initial q on C
dq = 0
ddq = 0
EL_total = 0
EC_total = 0
sv = 0
si = 0      # opening

while t < 0.1:
    rate(100)
    t += dt
    if t > dt and t < 0.01:
        vc0 = vc
        i0 = i
    if t > dt and sv == 0 and si == 0:
        sv = 1
        si = 1
        
    ddq =  -q/C/L
    dq  += ddq*dt
    q   += dq*dt
    vc  =  q/C

    i  = dq
    EL = (L*dq**2)/2
    EC = (q**2)/(2*C)
    E  = EL + EC
    EL_total += EL*dt
    EC_total += EC*dt
    
    i_t.    plot(pos = (t, i))
    vc_t.   plot(pos = (t, vc/100))
    q_t.    plot(pos = (t, q*400))
    EL_t.   plot(pos = (t, EL))
    EC_t.   plot(pos = (t, EC))
    E_t.    plot(pos = (t, E))
    ELave_t.plot(pos = (t, EL_total/t))
    ECave_t.plot(pos = (t, EC_total/t))
    
    # calculate T
    if sv == 1 and vc0*vc < 0:
        tv1 = t
        sv = 2
    if sv == 2 and vc0*vc < 0 and vc0 < 0:
        tv2 = t
        sv = 3
    if si == 1 and i0*i < 0:
        ti1 = t
        si = 2

print "T = ", 2*(tv2-tv1), "(sec)"
print "phase angle(I to VC) = ", (ti1-tv1)/(2*(tv2-tv1))*2, "(pi)"

 
