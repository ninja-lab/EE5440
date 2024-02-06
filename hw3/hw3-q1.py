#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:49:45 2024

@author: erik
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import numpy as np
from scipy.optimize import root


Eg = 1.15
Ego = 1.18
beta = 636
alpha = .473e-3 


# Define the quadratic function: f(x) = ax^2 + bx + c
def quadratic_function(x, a, b, c):
    return a*x**2 + b*x + c

# Coefficients of the quadratic equation
a, b, c = alpha, (Eg-Ego), (Eg-Ego)*beta

# Function to be passed to `root`, expects x[0] due to the solver expecting an array
def func_to_solve(x):
    return quadratic_function(x[0], a, b, c)

# Initial guess for the root
initial_guess = [200]

# Solve for the root
solution = root(func_to_solve, initial_guess)

# Print the solution
if solution.success:
    print(f"Root found: {solution.x[0]}")
else:
    print("Root finding failed.")
    
T = np.linspace(0,600)
bandgap = Ego - alpha*T**2 / (beta+T)   
fig, ax = plt.subplots()
#major_formatter= EngFormatter(unit='', places=0, sep='')
#ax.yaxis.set_major_formatter(major_formatter)  
ax.set_xlabel('Temperature [K]')
ax.set_ylabel('Bandgap [eV]')
ax.set_title('Bandgap vs Temperature of Silicon')
ax.plot(T, bandgap)
