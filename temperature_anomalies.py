# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 11:22:34 2018

Exercise 6

@author: katel
"""

import pandas as pd
import functions as f

#Set a file path variable
fp = r'C:\Users\katel\Documents\GeoPythonClass\1091402.txt'

#Read in the text file, set nan values and fixed width and skip row 2
data = pd.read_csv(fp, sep='\s+', skiprows=[1], na_values=['-9999'])


''' Problem 1'''
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

#Problem 2 = aggregating data into monthly values 
#1st convert to str, slice then convert back to int
data['YYYY_MM'] = data['DATE'].astype(str)

data['YYYY_MM'] = data['YYYY_MM'].str.slice(start=0, stop=6)

data['YYYY_MM'] = data['YYYY_MM'].astype(int)

#create empty dataframe for aggregation
monthlyData = pd.DataFrame()
#create varaible to be looped through
grouped = data.groupby('YYYY_MM')

#iterate over the groups of data
for key, group in grouped:
    #aggregate the data
    mean_values = group[['TAVG']].mean()
    mean_values['YYYY_MM'] = key
    #add the data into dataframe
    monthlyData = monthlyData.append(mean_values, ignore_index=True)

monthlyData['YYYY_MM'] = monthlyData['YYYY_MM'].astype(int)

#create C temp column
monthlyData['TempC'] = (monthlyData['TAVG'] - 32)/1.8

#Problem three
#Create a new dataframe, aggregate the data then merge back to monthlyData tofind anomolies

#Create empty dataframe that will be filled later
referenceTemps = pd.DataFrame()

#Create a selection of 52-80 data with a temp dataframe called MounthlyDataS
monthlyDataS = monthlyData.ix[(monthlyData['YYYY_MM']>=195901) & (monthlyData['YYYY_MM']<=198012)]
monthlyDataS = monthlyDataS.reset_index()
#create a new column for last two char of YYYY_MM to be aggregated next
monthlyDataS['Month'] = monthlyDataS['YYYY_MM'].astype(str)
monthlyDataS['Month'] = monthlyDataS['Month'].str.slice(start=4, stop=6)
monthlyDataS['Month'] = monthlyDataS['Month'].astype(int)


#create a groupby varaible for aggregation
MDSgrouped = monthlyDataS.groupby('Month')

#iterate  filling empty refernceTemps
for key, group in MDSgrouped:
    mean_vals = group[['TempC']].mean()
    mean_vals['Month'] = key
    referenceTemps = referenceTemps.append(mean_vals, ignore_index=True)

#Create a list to replace month number with name
#rowMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#Replace the number with the name
#referenceTemps['Month'] = rowMonth

#Rename the TempC column
referenceTemps = referenceTemps.rename(columns={'TempC':'avgTempsCHelsinki'})
#conv back to int
referenceTemps['Month'] = referenceTemps['Month'].astype(int)

#Begin the merge
join = monthlyDataS.merge(referenceTemps, on='Month', how='outer')

join['Diff']=(join['TempC'])-(join['avgTempsCHelsinki'])


#create a file path for Helsinki output
fpH = 'referenceTempsHelsinki.txt'
#output to csv
referenceTemps.to_csv(fpH, sep=',')



























