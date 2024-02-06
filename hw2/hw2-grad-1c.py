#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:48:44 2024

@author: erik
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import numpy as np
from scipy import constants

# Planck's constant
h = constants.h
print("Planck's constant:", h)
hbar = constants.hbar
# The speed of light
c = constants.c
print("Speed of light:", c)

# Electron charge
electron_charge = constants.e  # Charge in coulombs
print("Electron charge (C):", electron_charge)

# Electron mass
electron_mass = constants.m_e  # Mass in kilograms
print("Electron mass (kg):", electron_mass)
pi = constants.pi 

#Efs = .5*electron_mass*(10e5)**2/electron_charge 
Vo = 3

E = np.linspace(.001, .99*Vo)
#Efs = Vo - E
k1 = np.sqrt(2*electron_mass*E*electron_charge/hbar**2)
k2 = np.sqrt(2*electron_mass*(Vo-E)*electron_charge/hbar**2)

L1 = .2e-9
L2 = .5e-9 
T1 = 1/ (1+ ((k1**2+k2**2)/(2*k1*k2))*np.sinh(k2*L1)**2)
T2 = 1/ (1+ ((k1**2+k2**2)/(2*k1*k2))*np.sinh(k2*L2)**2)
T1_approx = 16*(E/Vo)*(1-E/Vo)*np.exp(-2*k2*L1)
T2_approx = 16*(E/Vo)*(1-E/Vo)*np.exp(-2*k2*L2)


fig, ax = plt.subplots()
ax.plot(E/Vo, T1, label = '.2nm actual')
ax.plot(E/Vo, T1_approx, label = '.2nm approx' )
ax.plot(E/Vo, T2, label = '.5nm actual')
ax.plot(E/Vo, T2_approx, label = '.5nm approx' )
#major_formatter= EngFormatter(unit='m', places=0, sep='')
#ax.xaxis.set_major_formatter(major_formatter)  
ax.legend()
ax.set_xlabel('Normalized Incident Energy')
ax.set_ylabel('Tunnelling probability')
ax.set_title('Tunneling Approximation vs Analytical')