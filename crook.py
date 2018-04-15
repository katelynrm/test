# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:42:26 2018

@author: katel

Testing out Crook join with pandas
"""

import pandas as pd



'''This land table contains only real property owner account numbers.
It also contains acres, however they are seperated out by land use
For example, a parcel with a farm might have two records like
acct: 1   landuse: agg   acre:100
acct: 1   landuse: res   acre:1
So i will aggregate the data for a result like the following
acct:1 acre: 101
'''

#set file path to land table
fp = r'C:\Users\katel\Documents\GeoPythonClass\crook\Land.csv'

#read it in
land = pd.read_csv(fp, sep=',')

#only keep relevant columns
SCol = ['MAPTAXLOT', 'ACCOUNT', 'ACRES']

land = land[SCol]

#Creat an empty dataframe to be filled in with a for loop
landAcreAgg = pd.DataFrame()

#Group the acres by account number
grouped = land.groupby('ACCOUNT')

#iterate through account number and sum the Acres field
for key, group in grouped:
    sum_val = group[['ACRES']].sum()
    sum_val['ACCOUNT'] = key
    landAcreAgg = landAcreAgg.append(sum_val, ignore_index = True)
    
    
'''
Now for the owner table. This table contains owners for all real and non-real
property.  
'''
#set fp2 and read in the owner table

fp2 = r'C:\Users\katel\Documents\GeoPythonClass\crook\Taxlot_owners.csv'

owner = pd.read_csv(fp2, sep=',')

#keep only relevant columns
Ocol = ['ACCOUNT', 'MAPTAXLOT', 'OWNER', 'ADD1']
owner = owner[Ocol]

'''
Now for the join! I will join both tables by acct number 
so that the resulting table will contain owner name info only for real 
property owners.
'''
join = pd.merge(landAcreAgg, owner, on='ACCOUNT', how='left')

join_output = 'crook_join.csv'

join.to_csv(join_output, sep=',')





