# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Exercise 3, problem 1
"""
basename = "Station"

#create empty list
filenames = []

#for loop that will become station numbers
for stationnumber in range(21):
    station = basename + "_" + str(stationnumber) + ".txt"
    filenames.append(station)
    
print(filenames)    
    
    

    

    