# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:14:44 2018

@author: katel
"""

def fahrToCelsius(tempFahrenheit):
    '''Converts temp in Fahr to temp in celcius 
    Parameters
    ---------
    tempFahrenheit <numerical>
    temp in Fahrenheit
    
    Returns
    --------
    <float>
    Converted temp
    '''
    return (tempFahrenheit -32) / 1.8

print("71 degrees Fahrenheit in Celsius is:", fahrToCelsius(71))