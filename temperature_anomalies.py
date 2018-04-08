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

data = pd.read_csv(fp, sep='\s+', )