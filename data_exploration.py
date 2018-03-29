# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:53:57 2018

@author: katel

Exercise 5: Manipulating data with Pandas
"""
import pandas as pd

#Reading in csv and assigning na values as an astrisk
data = pd.read_csv('6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])
'''
#print the names of the columns in the table
print(data.columns)

#print the number of rows
print ("There are ", len(data.index), "rows")

#print the data types of the columns
print(data.dtypes)

#print the mean temp
print("The mean temperature is:", data['TEMP'].mean())

#print the standard deviation of max temps
print("The standard deviation of the max temp is:", data['MAX'].std())

#print the number of unique values of USAF
print("The number of unique values in USAF is:", data['USAF'].nunique())


Part 2 of Exercise 5
'''

#creating a new varaible that contains only a few column of the source data
selected = data[['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']]

#removing rows with 
selected.dropna(subset =['TEMP'])






