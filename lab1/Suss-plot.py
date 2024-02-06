#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 06:35:56 2024

@author: erik
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import numpy as np
from random import random

df = pd.read_csv('10-11.TXT', header=1, sep=' ')#,index_col=0)  # you will need to adjust this to read your file properly

### data cleaning/prep if necessary ###
df = df.drop(0)
df.set_index('NO.', inplace=True)
df = df.astype(np.float64)
print(df.head(15))  # check results of import

slope, intercept = np.polyfit(df['V3'], df['I3'], 1)

fig, ax = plt.subplots()
major_formatter= EngFormatter(unit='A', places=0, sep='')
ax.yaxis.set_major_formatter(major_formatter)  
ax.set_xlabel('V3 [V]')
ax.set_ylabel('I3 [A]')
ax.set_title('')
ax.plot(df['V3'], df['I3'])

annotation_text = f'best fit resistance: {1/slope:.1f} Ω'
plt.annotate(annotation_text, xy=(0.05, 0.85), xycoords='axes fraction', fontsize=12,
             bbox=dict(boxstyle="round", fc="w"))

df = pd.read_csv('14-15.TXT', header=1, sep=' ')#,index_col=0)  # you will need to adjust this to read your file properly

### data cleaning/prep if necessary ###
df = df.drop(0)
df.set_index('NO.', inplace=True)
df = df.astype(np.float64)
print(df.head(15))  # check results of import

slope, intercept = np.polyfit(df['V3'], df['I3'], 1)

fig, ax = plt.subplots()
major_formatter= EngFormatter(unit='A', places=0, sep='')
ax.yaxis.set_major_formatter(major_formatter)  
ax.set_xlabel('V3 [V]')
ax.set_ylabel('I3 [A]')
ax.set_title('')
ax.plot(df['V3'], df['I3'])
ax.set_title('The device between pads 14 and 15')
annotation_text = f'best fit resistance: {1/slope:.1f} Ω'
plt.annotate(annotation_text, xy=(0.05, 0.85), xycoords='axes fraction', fontsize=12,
             bbox=dict(boxstyle="round", fc="w"))