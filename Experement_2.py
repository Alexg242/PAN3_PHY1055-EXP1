# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 2026

@author: alexg
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x,t):
    return t - x**2

def Euler(x0,tn,qn):##This defines the function we will be useing later Certian variables are static for consiteanty purpses
    tc = time0
    qc = x0
    
    while not abs(tc-max_time) < timestep/2:
        qc = qc + (timestep*f(qc,tc))
        tc = tc + timestep
        tn.append(tc)
        qn.append(qc)


plt.rcParams['figure.dpi'] = 300

timestep = 0.01 #h / time change
max_time = 9#tmax
time0 = 1 ##t

time = []
quanity = []
Euler(1, time, quanity)

t1 = []
q1 = []
Euler(2, t1, q1)

t2 = []
q2 = []
Euler(1.5, t2, q2)

t3 = []
q3 = []
Euler(0.5, t3, q3)

t4 = []
q4 = []
Euler(0, t4, q4)

t5 = []
q5 = []
Euler(-0.5, t5, q5)

t6 = []
q6 = []
Euler(-1, t6, q6)


plt.plot(time, quanity, "k-", label="x0 = 1")
plt.plot(t1, q1, "-", label="x0 = 2")
plt.plot(t2, q2, "-", label="x0 = 1.5")
plt.plot(t3, q3, "-", label="x0 = 0.5")
plt.plot(t4, q4, "-", label="x0 = 0")
plt.plot(t5, q5, "-", label="x0 = -0.5")
plt.plot(t6, q6, "-", label="x0 = -1")
plt.title("Particle Quantity vs Time")
plt.ylabel("Quanity (x)")
plt.xlabel("Time (s)")
plt.legend()