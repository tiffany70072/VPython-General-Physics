import numpy as np
import pylab as plt

h_bar, me, nm, eV = 1.055E-34, 9.109E-31, 1E-9, 1.6E-19

E = 5.1*eV
U, L = 4.8*eV, 0.8*nm
x0, sigma = -10*nm, 4*nm
length, N = 120*nm, 6000
dx = length/N
k = np.sqrt(2*me*E/(h_bar**2))
step = 600                           # number_of_time_steps_in_2pi
dt = 2*np.pi*h_bar/E/step
total_time = -2*x0/np.sqrt(2*E/me)
x = np.linspace(-length/2, length/2, N)
V = 0.0*x
V[N/2:N/2+L/dx+1] = U
psi = np.exp(-(x-x0)**2/(2*sigma**2))*np.exp(1j*k*x)
delta_psi = 0*psi

plt.rcParams['figure.figsize'] = 25, 10
plt.ion()
xmin, xmax, ymax = x0, L-x0, 3
plt.axis([xmin, xmax, -ymax, ymax])
lineV, = plt.plot(x, 3*V/U)
lineR, = plt.plot(x, psi.real)
lineP, = plt.plot(x, abs(psi)**2)
plt.draw()
D1 = range(1, N-1)
D2 = range(2, N)
D3 = range(0, N-2)
psi_past = psi
t = 0

while t < total_time :
    delta_psi[D1] = (-h_bar**2*(psi[D2]-2*psi[D1]+psi[D3])/2/me/dx**2+V[D1]*psi[D1])/(1j*h_bar)
    psi_future = psi_past + delta_psi*2*dt
    if int(t/dt)%100 = = 0:
        lineR.set_ydata(psi.real)
        lineP.set_ydata(abs(psi)**2)
        plt.draw()
    psi_past = psi
    psi = psi_future
    t = t + dt
    
print 'T = ', sum(abs(psi[N/2+L/dx+1:]**2))/sum(abs(psi**2))
plt.ioff()
plt.show()
