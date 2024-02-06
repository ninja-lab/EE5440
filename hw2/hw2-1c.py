#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:48:07 2024

@author: erik
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import numpy as np
from random import random
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
m_eu = .13*electron_mass
m_el = .45*electron_mass
a = np.linspace(1e-9, 10e-9)
E1u = pi**2*hbar**2/(2*m_eu*a**2)
E1l = pi**2*hbar**2/(2*m_el*a**2)
Eg = 1.74*electron_charge

lambdas = h*c/(E1l + E1u + Eg)
fig, ax = plt.subplots()
ax.plot(a*1e9, lambdas)
major_formatter= EngFormatter(unit='m', places=0, sep='')
ax.yaxis.set_major_formatter(major_formatter)  
ax.set_xlabel('Width of Well [nm]')
ax.set_ylabel('Wavlength of Emitted Light')
ax.set_title('Emitted Photon Wavelength vs Well Width')