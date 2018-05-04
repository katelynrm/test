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

Yrng = pd.date_range('1953', '2016', freq='AS')
