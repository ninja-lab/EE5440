# %%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
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
major_formatter= EngFormatter(unit='A', places=0, sep='')
ax.yaxis.set_major_formatter(major_formatter)  
ax.set_xlabel('V2 [V]')
ax.set_ylabel('I2 [A]')
ax.set_title('I2 vs V2')

fig2, ax2 = plt.subplots()
ax2.yaxis.set_major_formatter(major_formatter)  
ax2.set_xlabel('V3 [V]')
ax2.set_ylabel('I2 [A]')
ax2.set_title('I2 vs V3')
grouped = df.groupby("V3")

V3s = list(grouped.groups)
for V3 in V3s: 
    color=(random(), random(), random())
    g = grouped.get_group(V3)
    ax.plot( g['V2'].values, g['I2'].values, linestyle='None', marker='.', color=color, label=V3)
    ax2.plot( g['V3'].values, g['I2'].values, linestyle='None', marker='.', color=color)
    
ax.legend()
#plt.show()

