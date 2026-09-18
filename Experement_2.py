# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 2026

@author: alexg
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x,t):
    return t - x**2

def Euler(x0,tn,qn):
    tc = time0
    qc = x0
    
    while not abs(tc-max_time) < timestep/2:
        qc = qc + (timestep*f(qc,tc))
        tc = tc + timestep
        tn.append(tc)
        qn.append(qc)


plt.rcParams['figure.dpi'] = 300

timestep = 0.05 #h / time change
max_time = 9 #tmax
tau = 3.0 ##lifetime for decay/time constant

time0 = 1 ##t

#%%
quantity0 = 1 ## x0

time = []
quanity = []

time.append(time0)
quanity.append(quantity0)

timec= time0 #time current
quantc = quantity0 #quantity curreent (N)

while not abs(timec-max_time) < timestep/2:
    quantc = quantc + (timestep*f(quantc,timec))
    timec = timec + timestep
    time.append(timec)
    quanity.append(quantc)

#%%

time = []
quanity = []

Euler(3, time, quanity)




plt.plot(time, quanity, "k-", label="Calculated Values")
plt.title("Particle Quantity vs Time")
plt.ylabel("Quanity (N)")
plt.xlabel("Time (s)")
plt.legend()