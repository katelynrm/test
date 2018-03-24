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
    