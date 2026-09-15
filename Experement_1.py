# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:47:17 2026

@author: alexg
"""
import matplotlib.pyplot as plt

timestep = 0.05 #change in t
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
    
plt.plot(time, quanity)
