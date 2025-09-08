# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 13:48:16 2025

@author: Kai
"""



# Task 1
temp = 85


if temp >= 90:
    print("Too hot")

elif temp <= 20:
    print("Too cold")

else:
    print("Today might be nice ")
    

# Task 2

if temp < 20:
    print("Skiing")
elif temp < 50:
    print("Hiking")
elif temp > 80:
    print("Swimming")
elif temp > 50:
    print("Jogging")
    
# Task 3

what_month = "September"
how_many_nuts = 70


# Two ways of solving this

# First -- use variables, and a sinle print
aug = what_month == "August" and how_many_nuts >= 50

sept = what_month == "September" and how_many_nuts >= 100

oct = what_month == "November" and how_many_nuts >= 200

print (aug or sept or oct or nov)


# Second -- more conditionals
if what_month == "August" and how_many_nuts >= 50:
    print("True")
elif what_month == "September" and how_many_nuts >= 100:
    print("True")
elif what_month == "October" and how_many_nuts >= 150:
    print("True")
elif what_month == "November" and how_many_nuts >= 200:
    print("True")
else:
    print("False")


temp = 65
bonus = "tornado"


very_hot = temp > 85
not_hot_or_cold = temp > 30 and temp < 80

if very_hot and bonus == "sunny":
    print("Good day for swimming")
elif bonus == "windy" and temp > 40:
    print("Go fly a kite")
elif bonus != "raining" and not_hot_or_cold:
    print("Go for a hike")

