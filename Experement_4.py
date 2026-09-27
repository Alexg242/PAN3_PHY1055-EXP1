# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:27:27 2026

@author: alexg
"""

import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams['figure.dpi'] = 300


h = 0.1
tmax = 32

t0 = 0
x0 = 0
v0 = 1



def E4(h, axs):
    t = t0
    x = x0
    v = v0
    tar = [t0]
    xar = [x0]
    var = [v0]
    while not abs(t-tmax) < h/2:
        xinnit = x + h*v
        vinnit = v - h*x
        x= x+h*(v+vinnit)/2
        v= v-h*(x+xinnit)/2
        t = t+h
        tar.append(t)
        xar.append(x)
        var.append(v)
    axs.plot(tar,xar,"-",label="x(t) for h = "+str(h), linewidth =1)
    axs.plot(tar,var,"--",label="v(t) for h = "+str(h), linewidth =1)
    return xar

hvals = [0.5, 0.2, 0.1]

for i in hvals:
    xar = E4(i, plt)
    

timet = [t0]
quanityt = [x0]

tcurrent = t0
xcurrent = x0

while tcurrent < tmax:
    xcurrent = (math.sin(tcurrent))
    timet.append(tcurrent)
    quanityt.append(xcurrent)
    tcurrent = tcurrent + h

plt.plot(timet, quanityt,"k-", label="Exact Values", linewidth =1)
plt.legend()
plt.title("Particle Quantity vs Time")
plt.ylabel("Quanity (x)")
plt.xlabel("Time (s)")
plt.legend(loc=1,fontsize =5 )

#%%

print(len(timet))
print(len(xar))

values = []
"""
for i in timet:
    temp = abs(quanityt(i)-xar(i))
    values.append[temp]"""

Comparison = np.subtract(quanityt,xar)

plt.plot(timet, Comparison,"k-", label="Exact Values", linewidth =1)
plt.title("Diffence Between True value and Calulated value (h=0.1) vs Time")
plt.ylabel("Difference (x)")
plt.xlabel("Time (s)")


