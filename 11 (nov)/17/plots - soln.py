# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:43:09 2025

@author: Kai
"""

import matplotlib.pyplot as plt # for plots
import csv # CSV library; easier than what we've done before



with open("baltimore_weather.csv") as weather_file:

    max_temp_header = "tempmax"
    min_temp_header = "tempmin"
    avg_temp_header = "temp"
    

    max_temp_col = 0
    min_temp_col = 0
    avg_temp_col = 0
    

    weather_data = csv.reader(weather_file)

    max_temp_list = list()
    min_temp_list = list()
    avg_temp_list = list()

    for rownum, row in enumerate(weather_data):

        if 0 == rownum:
            max_temp_col = row.index(max_temp_header)
            min_temp_col = row.index(min_temp_header)
            avg_temp_col = row.index(avg_temp_header)


        else:
            max_temp_list.append(float(row[max_temp_col]))
            min_temp_list.append(float(row[min_temp_col]))
            avg_temp_list.append(float(row[avg_temp_col]))
            
    
    days = list(range(len(max_temp_list)))


    # same sort of plot we've done before, give it a list of X and Y values to plot
    # you also know how to do the xlabel and ylabel by now
    plt.plot(days, max_temp_list, "g", label="Daily Max")
    
    plt.plot(days, avg_temp_list, "b", label="Daily Average")
    
    plt.plot(days, min_temp_list, "r", label="Daily Low")
    
    plt.xlabel("Day of Year")
    plt.ylabel("Temperture (F)")
    plt.title("Baltimore Yearly Temperatures")

    plt.legend(loc="upper left")
    
    plt.show()
