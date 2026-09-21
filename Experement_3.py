# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:03:15 2026

@author: alexg
"""

import matplotlib.pyplot as plt
import math

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

timestep = 0.005
max_time = 32

time = []
time.append(t0)
quantity = []
quantity.append(x0)

yc = y0
xc = x0

while not abs(timec-max_time) < timestep/2:
    dx = dx_func(yc)
    xc = xc + dx*timestep
    dy= dy_func(xc)
    yc = yc + dy*timestep
    timec = timec + timestep
    time.append(timec)
    quantity.append(xc)
    



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
    
plt.plot(time, quantity, "k-", label="Calculated Values")
plt.plot(timet, quanityt, "k--", label="Exact Values")
plt.title("x vs Time")
plt.ylabel("x")
plt.xlabel("Time (s)")
plt.legend()