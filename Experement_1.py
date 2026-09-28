# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:47:17 2026

@author: alexg
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.dpi'] = 300

max_time = 10 #t~max
tau = 2.0 ##lifetime for decay/time constant
time0 = 0 ##t
quantity0 = 10 ## N0
timestep = 0.1

def E1(h):
    timestep = h #change in t
    time = [time0]
    quanity = [quantity0]
    timec= time0 #time current
    quantc = quantity0 #quantity curreent (N)
    while not abs(timec-max_time) < timestep/2:
        quantc = (quantc-((quantc*timestep)/tau))
        timec = timec + timestep
        time.append(timec)
        quanity.append(quantc)
    plt.plot(time, quanity, "-", label="Calculated Values h="+str(timestep))

E1(0.01)
E1(1)
E1(0.5)
E1(0.1)

timet = []
quanityt = []

#timet.append(time0)
#quanityt.append(quantity0)

tcurrent = time0
Ncurrent = quantity0

while tcurrent <= max_time:
    Ncurrent = (quantity0*(np.exp((-tcurrent/tau))))
    timet.append(tcurrent)
    quanityt.append(Ncurrent)
    tcurrent = tcurrent + timestep


plt.plot(timet, quanityt, "k--", label="Exact Values")
plt.title("E1: Particle Quantity vs Time")
plt.ylabel("Quanity (N)")
plt.xlabel("Time (s)")
plt.legend()

#%%

Comparison = np.subtract(quanityt,quanity)

plt.plot(timet, Comparison,"k-", label="Exact Values", linewidth =1)
plt.title("E1: Diffence Between True value and Calulated value (h=0.1) vs Time")
plt.ylabel("Difference (x)")
plt.xlabel("Time (s)")