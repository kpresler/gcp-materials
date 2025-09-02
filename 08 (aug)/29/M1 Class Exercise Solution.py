# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 15:04:51 2025

@author: Kai
"""


# Task 1

melting_point_c = 660.3

melting_point_f = (9/5) * melting_point_c + 32

print(melting_point_f)

# Task 2

n = 3
T = 300
P = 150
R = 8.31446261815324

# PV = nRT

V = n*R*T/P

print(V)


# Task 3

starting_weight = 80
not_water = .4 * starting_weight
print (not_water)

final_weight = not_water / .75

print(final_weight)


# Task 4

"""

1: 10

"""


# Task 5

hours = int(input("How many hours did you work? "))

rate = int(input ("What is your hourly pay rate? "))

gross_pay = hours * rate

net_pay = gross_pay - 3.5

net_pay = net_pay * .84

print("Gross weekly pay: " + str(gross_pay))

print("Net weekly pay: " + str(net_pay))
