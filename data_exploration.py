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
selected.is_copy = None
#removing rows with na values
selected.dropna(subset =['TEMP'])

#convert Temp
selected['Celsius'] = (selected['TEMP']-32)/1.8

#round values
selected['Celsius'] = selected['Celsius'].round(0)


#Part 3 of exercise 5
#Create variable where usaf value is 29980
kumpula = selected.ix[selected['USAF'] == 29980]

#Create variable where usaf value is 28450
rovaniemi = selected.ix[selected['USAF'] == 28450]


