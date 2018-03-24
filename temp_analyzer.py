# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 11:00:54 2018

@author: katel
"""

from functions import fahrToCelsius as fTC
from functions import tempClassifier as tC
from data import tempData as tD

#created an empty list that will eventually contain classified values
tempClasses = []

#iterate over the Fahrenheit temps in the tempData list
for temp in tD:
    #converting and classifing
    tempCelsius = fTC(temp)
    tempClass = tC(tempCelsius)
    #filling the tempClasses list with the tempClass from above
    tempClasses.append(tempClass)
    
print("How many temps are in each class?")

#now to count how many temps are in each class using the count function
print("There are", tempClasses.count(0), "zeros")
print("There are", tempClasses.count(1), "ones")
print("There are", tempClasses.count(2), "twos")
print("There are", tempClasses.count(3), "threes")
print("There are a total of", len(tempClasses), "classes")
