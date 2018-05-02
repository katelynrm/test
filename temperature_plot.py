# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:00:35 2018

@author: katel
"""
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
#Problem 0- read in H and S temp data

fpH = r'C:\Users\katel\Documents\GeoPythonClass\helsinki_426.txt'
fpS = r'C:\Users\katel\Documents\GeoPythonClass\sodankyla_426.txt'

HTemps = pd.read_csv(fpH, sep=',')
STemps = pd.read_csv(fpS, sep=',')

#Problem 1 - conv M to datetime. 
HTemps['MonthDT'] = pd.to_datetime(HTemps['YYYY_MM'], format='%Y%m')
HTemps = HTemps.set_index('MonthDT')

#STemps['MonthDT'] = pd.to_datetime(STemps['Month'], format='%m')
#STemps = STemps.set_index('MonthDT')


#Create a dataframe for HTemps from 2010-2017 for the plot
HTemps1017 = HTemps['2010-01-01':'2018-01-01']

#Plot data from HTemps1017 and add xy and title labels
HTemps1017.plot(x=HTemps1017.index, y='TempC', c='black', marker='o', linestyle='dashed')
plt.xlabel('Year')
plt.ylabel('Temp in C')
plt.title('Ave temps in Helsinki from 2010-2017')
