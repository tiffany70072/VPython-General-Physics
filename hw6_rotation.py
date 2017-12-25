from __future__ import division
from visual import*

G = 6.673*10**(-11)
M = 1.989*10**30
au = 1.495*10**11
size = 0.1*au

e_d = 1.495*10**11
m_d = 2.279*10**11
h_d = 8.7655*10**10

e_v = vector(0.0, 2.9783*10**4, 0.0)
m_v = vector(0.0, 2.4077*10**4, 0.0)
h_v = vector(0.0, 5.4578*10**4, 0.0)

s = sphere(pos = (0, 0, 0), radius = size, color = color.yellow)
e = sphere(pos = (e_d, 0, 0), radius = size, color = color.blue, make_trail = True)
m = sphere(pos = (m_d, 0, 0), radius = size, color = color.red, make_trail = True)
h = sphere(pos = (h_d, 0, 0), radius = size, color = color.white, make_trail = True)

a = G*M
t = 0
dt = 3600

while not(e.pos.x >= e_d and t > dt):
    rate(10000)
    t = t + dt
    e.pos = e.pos + e_v*dt
    e_ac = -a/mag(e.pos)/mag(e.pos)*norm(e.pos)
    e_v = e_v + e_ac*dt
    t_1 = t
print"earth:T**2/R**3 = " , t_1**2/(e_d)**3, "(s**2/m**3), ", "one year = ", t_1/24/3600, "days, "
 
while not(m.pos.x >= m_d and t > t_1):
    rate(10000)
    t = t + dt
    m_ac = -a/mag(m.pos)/mag(m.pos)*norm(m.pos)
    m_v = m_v + m_ac*dt
    m.pos = m.pos + m_v*dt
    t_2 = t - t_1
print"mars:T**2/R**3 = " , t_2**2/(m_d)**3, "(s**2/m**3)"  

while not(h.pos.x >= h_d and t > t_1 + t_2 + 36000):
    rate(10000)
    t = t + dt 
    h_ac = -a/mag(h.pos)/mag(h.pos)*norm(h.pos)
    h_v = h_v + h_ac*dt
    h.pos = h.pos + h_v*dt
    t_3 = (t - t_2 - t_1)/24/3600/365.25
    if h.pos.x/mag(h.pos) >= 0.999:
        t_p = (t - t_1 - t_2)/86400/365.25
        hv_p = h_v
        hp_p = h.pos
    if h.pos.x/mag(h.pos) <= -0.99999:
        t_a = (t - t_1 - t_2)/86400/365.25
        hv_a = h_v
        hp_a = h.pos
    if h.pos.y/mag(h.pos) <= 0.999:
        hv_m = h_v
        hp_m = h.pos

print "T = ", t_3, "years, ", t_a, t_p, "perihelion:", mag(cross(hv_p, hp_p)*86400/2), 
print ", aphelion:", mag(cross(hv_a, hp_a)*86400/2), ", haif-way:", mag(cross(hv_m, hp_m)*86400/2)

    
    

    
    
    
    

