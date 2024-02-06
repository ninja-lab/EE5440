#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:10:13 2024

@author: erik
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import numpy as np
import pandas as pd 
from scipy import constants

k = constants.Boltzmann
q = constants.elementary_charge

T = np.array([0.1, 77, 300, 1073])
E = np.linspace(0, k*300*4/q)
#E = np.linspace(0, k*300*4)

def fermi(e, t):
    return 1 / (1 + np.exp((e*q)/(k*t)))
#def fermi(e, t):
#    return 1 / (1 + np.exp(e/(k*t)))

f_values = fermi(E[:, np.newaxis], T)
#fig, ax = plt.subplots()


# Convert to DataFrame
df = pd.DataFrame(f_values, index=E, columns=[f'T={param}K' for param in T])
fig, ax = plt.subplots()
df.plot(ax=ax)
major_formatter= EngFormatter(unit='eV', places=0, sep='')
ax.xaxis.set_major_formatter(major_formatter)  
ax.set_xlabel('Energy above Fermi Level (E - Ef)')
ax.set_ylabel('Probability')
ax.set_title('Fermi Probability')
ax.legend(title='Temperatures')

def fermi_approx(e):
    return np.exp(-(e*q)/(k*300))

fig, ax = plt.subplots()

ax.plot(df.index/ (k*300/q) , df['T=300.0K'], label = 'exact')
ax.plot(df.index/ (k*300/q) , fermi_approx(df.index), label = 'approximation')
#major_formatter= EngFormatter(unit='kT', places=0, sep='')
#ax.xaxis.set_major_formatter(major_formatter)  
ax.set_xlabel('Energy above Fermi Level [kT]')
ax.set_ylabel('Probability')
ax.set_title('Fermi Probability and Boltzmann Approximation')
ax.legend()


