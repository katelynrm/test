# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:53:57 2018

@author: katel

Exercise 5: Manipulating data with Pandas
"""
import pandas as pd

#Reading in csv and assigning na values as an astrisk
data = pd.read_csv('6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])

print(data.columns)

print (len(data.index))
