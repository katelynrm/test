# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:54:36 2018

@author: katel
"""
import pandas as pd

#Set a file path variable
fp = r'C:\Users\katel\Documents\GeoPythonClass\sodankyla_noaa_raw.txt'

#Read in the text file, set nan values and fixed width and skip row 2
data = pd.read_csv(fp, sep='\s+', skiprows=[1], na_values=['-9999'])

data['TAVG'] = ((data['TMAX'])+(data['TMIN']))/2
''' Problem 1'''
#get count of all non values
data['TAVG'].count()
data['TMIN'].count()
data['TMAX'].count()
data['DATE'].count()

#finding first and last date
print('The first date is:', data['DATE'].ix[0])
print('The last date is:', data['DATE'].ix[20546])

#ave temp of entire file
print('The average temp of all the data is:', data['TAVG'].mean())


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
referenceTempsS = pd.DataFrame()

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
    referenceTempsS = referenceTempsS.append(mean_vals, ignore_index=True)

#Create a list to replace month number with name
#rowMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#Replace the number with the name
#referenceTemps['Month'] = rowMonth

#Rename the TempC column
referenceTempsS = referenceTempsS.rename(columns={'TempC':'avgTempsCSodankyla'})
#conv back to int
referenceTempsS['Month'] = referenceTempsS['Month'].astype(int)

#Begin the merge
join = monthlyDataS.merge(referenceTempsS, on='Month', how='outer')

join['DiffS']=(join['TempC'])-(join['avgTempsCSodankyla'])

#read in Helsinki data for join
fpH = r'C:\Users\katel\Documents\GeoPythonClass\referenceTempsHelsinki.txt'
referenceTempsH = pd.read_csv(fpH, sep=',')


H_S_join = referenceTempsH.merge(referenceTempsS, on='Month', how='outer')

Cols = ['Month', 'avgTempsCHelsinki', 'avgTempsCSodankyla']
summerDiffs = H_S_join[Cols]
summerDiffs = summerDiffs.ix[(summerDiffs['Month']>=6)&(summerDiffs['Month']<=8)]
summerDiffs = summerDiffs.reset_index()
summerDiffs['TempDiff'] = (summerDiffs['avgTempsCHelsinki']) - (summerDiffs['avgTempsCSodankyla'])

fpsummerdiffs = 'H_S_summer_diffs.txt'
summerDiffs.to_csv(fpsummerdiffs, sep=',')
