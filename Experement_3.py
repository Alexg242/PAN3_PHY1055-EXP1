# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:03:15 2026

@author: alexg
"""

import matplotlib.pyplot as plt
import math

plt.rcParams['figure.dpi'] = 300


def dx_func(y):
    dx = y
    return dx

def dy_func(x):
    dy = -x
    return dy


x0 = 0
y0 = 1
t0 = 0


dx = x0
dy = y0
timec = 0

timestep = 0.5
max_time = 32

time = []
time.append(t0)
quantity = []
quantity.append(x0)

yc = y0
xc = x0

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))


def E3(x0, y0, t0, max_time, timestep, axs):
    time = [t0]
    quantity = [x0]
    timec = t0
    xc = x0
    yc = y0
    while not abs(timec-max_time) < timestep/2:
        dx = dx_func(yc)
        xc = xc + dx*timestep
        dy= dy_func(xc)
        yc = yc + dy*timestep
        timec = timec + timestep
        time.append(timec)
        quantity.append(xc)
    axs.plot(time, quantity, "-", label="h="+ str(timestep))


Timesteps = [1, 0.5, 0.2, 0.1, 0.05, 0.01, 0.005]

for i in Timesteps:
    E3(x0,y0,t0,max_time,i,ax1)

timet = []
quanityt = []

timet.append(t0)
quanityt.append(x0)

tcurrent = t0
xcurrent = x0

while tcurrent <= max_time:
    xcurrent = (math.sin(tcurrent))
    timet.append(tcurrent)
    quanityt.append(xcurrent)
    tcurrent = tcurrent + timestep
    
E3(x0,y0,t0,max_time,0.05,ax2)

ax2.plot(timet, quanityt, "k--", label="Exact Values")
fig.suptitle("E3: Coupled Equations (x vs Time)")
ax1.set_xlabel("Time(s)")
ax1.set_ylabel("x")
ax2.set_xlabel("Time(s")
ax2.set_ylabel("x")
ax1.set_title("Comparitive Values of Timestep(h)")
ax2.set_title("Exact Value vs Calulated Value")
ax2.axis()
fig.suptitle("R6: Driven Oscillator")
ax2.legend(loc=3)
ax1.legend(loc=8, fontsize =10)

fig.show()  