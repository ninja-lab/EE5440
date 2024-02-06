# %%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, EngFormatter
from cycler import cycler 
import numpy as np
from random import random

df = pd.read_csv('TEST.TXT', header=2 )#na_values='NO.')#,index_col=0)  # you will need to adjust this to read your file properly

### data cleaning/prep if necessary ###
df = df.drop(0)
df.set_index(['NO.', 'V3'], inplace=True)
df = df.astype(np.float64)
df.index = df.index.set_levels([level.astype(np.float64) for level in df.index.levels])
print(df.head())  # check results of import
print(df.xs(0, level='V3'))
#### your plot code here ###

fig, ax = plt.subplots()
major_formatter= EngFormatter(unit='A', places=0, sep='')
ax.yaxis.set_major_formatter(major_formatter)  
ax.set_xlabel('V2 [V]')
ax.set_ylabel('I2 [A]')
ax.set_title('I2 vs V2')
fig, ax2 = plt.subplots()
ax2.yaxis.set_major_formatter(major_formatter)  
ax2.set_xlabel('V3 [V]')
ax2.set_ylabel('I2 [A]')
ax2.set_title('I2 vs V3')

V3s = set(df.index.get_level_values(1))
for V3 in V3s: 
    df1 = df.xs(V3, level='V3')
    color=(random(), random(), random())
    ax.plot( df1['V2'].values, df1['I2'].values, linestyle='None', marker='.', color=color, label=V3)
    n = df1['I2'].size
    ax2.plot( np.ones(n)*V3, df1['I2'].values, linestyle='None', marker='.')
ax.legend()   
    

#plt.show()

