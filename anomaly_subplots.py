# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:12:18 2018

@author: katel
Exercise 7, problem 2
Multiple plots for season anomolies in Helsinki
"""
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

#Snagging code from temperature_plot in probs 0-1
fpH = r'C:\Users\katel\Documents\GeoPythonClass\helsinki_426.txt'
HTemps = pd.read_csv(fpH, sep=',')
HTemps['MonthDT'] = pd.to_datetime(HTemps['YYYY_MM'], format='%Y%m')
HTemps = HTemps.set_index('MonthDT')

#Yrng = pd.date_range('2010', '2016', freq='AS')

#3list of season columns

#SeasonalData = pd.DataFrame(index=Yrng)

#4 altered due to bad lesson instructions - will just use 4 years of data


Y2012 = HTemps['2012-01-01':'2012-12-01']
Y2013 = HTemps['2013-01-01':'2013-12-01']
Y2014 = HTemps['2014-01-01':'2014-12-01']
Y2015 = HTemps['2015-01-01':'2015-12-01']


#create a panel 2x2 with subplots
fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize=(12,8))

#Parse axes from the axarray
ax11 = axes[0][0]
ax12 = axes[0][1]
ax21 = axes[1][0]
ax22 = axes[1][1]


Y2012.plot(x=Y2012.index, y='TempC', ylim=(-25,25), ax=ax11, c='blue', lw=2.5, label='2012')
Y2013.plot(x=Y2013.index, y='TempC', ylim=(-25,25), ax=ax12, c='blue', lw=2.5, label='2013')
Y2014.plot(x=Y2014.index, y='TempC', ylim=(-25,25), ax=ax21, c='blue', lw=2.5, label='2014')
Y2015.plot(x=Y2015.index, y='TempC', ylim=(-25,25), ax=ax22, c='blue', lw=2.5, label='2015')

plt.savefig(r'C:\Users\katel\Documents\GeoPythonClass\ex7.png', dpi=300)