# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 17:45:20 2018

@author: Katelyn

Exercise 2
"""
#A list of the 12 months
monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', \
             'August', 'September', 'October', 'November', 'December']

#A list of the average temps in C for each month 
aveTemp = [-3.5, -4.5, -1.0, 4.0, 10.0, 15.0, 18.0, 16.0, 11.5, 6.0, 2.0, -1.5]

#Following variable is the month for which the script will find the ave temp of
inputMonth = 'June'

#Following will find the index of the inputMonth
indexInputMonth = monthList.index(inputMonth)

#Follwing will calc the temp of the inputMonth
calcTemp = aveTemp[indexInputMonth]

print('The average temperature in Helskini in', inputMonth, 'is', calcTemp)
