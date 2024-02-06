#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from random import random


df = pd.read_csv('TEST.TXT', header=2)#,index_col=0)  # you will need to adjust this to read your file properly

### data cleaning/prep if necessary ###
df = df.drop(0)
df.set_index('NO.', inplace=True)
df = df.astype(np.float64)
print(df.head(15))  # check results of import

#### your plot code here ###
fig, ax = plt.subplots()

 
grouped = df.groupby("V3")
V3s = list(grouped.groups)
for V3 in V3s: 
    color=(random(), random(), random())
    g = grouped.get_group(V3)
    ax.plot( g['V2'].values, g['I2'].values, linestyle='None', marker='.', color=color, label=V3)
ax.legend()




#plt.show()

