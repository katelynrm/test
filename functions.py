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

def tempClassifier(tempCelsius):
    '''Classifies temps into 0 1 2 or 3
    Parameters 
    ------
    tempCelsius <numerical>
    temp in Celsius
    
    Returns
    ------
    <int>
    classified temp
    '''
    if tempCelsius < -2:
        return(0)
    elif tempCelsius >= -2 and tempCelsius <=2:
        return(1)
    elif tempCelsius >2 and tempCelsius <=15:
        return(2)
    else:
        return(3)
