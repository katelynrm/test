# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 11:22:34 2018

@author: katel
"""

import pandas as pd
import functions as f

#Set a file path variable
fp = r'C:\Users\katel\Documents\GeoPythonClass\1091402.txt'

#Read in the text file, set nan values and fixed width and skip row 2
data = pd.read_csv(fp, sep='\s+', skiprows=[1], na_values=['-9999'])

''' Problem 1
#get count of all non values
data['TAVG'].count()
data['TMIN'].count()
data['TMAX'].count()
data['DATE'].count()

#finding first and last date
print('The first date is:', data['DATE'].ix[0])
print('The last date is:', data['DATE'].ix[23715])

#ave temp of entire file
print('The average temp of all the data is:', data['TAVG'].mean())

#create a summer 69 frame with only summer 69 values
summer69 = data.ix[(data['DATE']>=19690501) & (data['DATE']<=19690831)]

#reset the index
summer69 = summer69.reset_index()

#find the max temp of 69
print('The max temp of the summer of 1969 was:', summer69['TMAX'].max())
'''
#Problem 2 = aggregating data into monthly values and exporting  to a csv






