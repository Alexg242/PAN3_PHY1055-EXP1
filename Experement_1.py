# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:47:17 2026

@author: alexg
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.dpi'] = 300

timestep = 0.5 #change in t
max_time = 10 #tmax
tau = 2.0 ##lifetime for decay/time constant

time0 = 0 ##t
quantity0 = 10 ## N0

time = []
quanity = []

time.append(time0)
quanity.append(quantity0)

timec= time0 #time current
quantc = quantity0 #quantity curreent (N)

while not abs(timec-max_time) < timestep/2:
    quantc = (quantc-((quantc*timestep)/tau))
    timec = timec + timestep
    
    time.append(timec)
    quanity.append(quantc)


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


plt.plot(time, quanity, "k-", label="Calculated Values")
plt.plot(timet, quanityt, "k--", label="Exact Values")
plt.title("Particle Quantity vs Time")
plt.ylabel("Quanity (N)")
plt.xlabel("Time (s)")
plt.legend()