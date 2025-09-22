# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 14:09:42 2025

@author: Kai
"""


def C2F(C):
    """
    converts Celcius to Fahrenheit    
    """
    return ((9.0/5.0)*C) + 32

def F2C(F):
    """
    converts Fahrenheit to Celcius
    
    """
    return (F-32.0)*(5.0/9.0)

def C2K(C):
    """
    converts Celcius to Kelvin
    
    """
    return C + 273.15

def K2C(K):
    """
    converts Kelvin to Celcius
    
    """
    return K - 273.15


def F2K(F):
    """
    converts Farenheit to Kelvin
    
    """
    return (F + 459.67)* (5.0/9.0)

def K2F(K):
    """
    converts Kelvin to Farenheit
    
    """
    return ((9.0/5.0)*K) - 459.67


if __name__ == "__main__":
    temp = float(input("Enter a temprature: "))
    scale = input("Enter scale: ")

    if scale.upper() == 'C':
        print("{:0.1f} C is {:0.1f} K or {:0.1f} F".format(temp,  C2K(temp), C2F(temp)))
    elif scale.upper() == 'F':
        print("{:0.1f} F is {:0.1f} K or {:0.1f} C".format(temp,  F2K(temp), F2C(temp)))
    elif scale.upper() == 'K':
        print("{:0.1f} K is {:0.1f} C or {:0.1f} F".format(temp,  K2C(temp), K2F(temp)))
    else:
        print('You did not select correct temrature scale !!!!')        
    
