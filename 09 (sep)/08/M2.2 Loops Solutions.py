# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 20:47:19 2025

@author: Kai
"""



# Task 1 

thing = 25
num_time = 2

for num in range(num_time):
    print(thing)
    

# Taask 2

nums_list = [1,2,3,4,5]

for num in nums_list:
    sqrt = num**.5
    sq = num**2
    cb = num**3
    
    print(f"{sqrt}, {num}, {sq}, {cb}")
    
    #print(sqrt, num, sq, cb)
    
# demo of using fstrings to interpolate into a string & why we care
num_cats = 5
print(f"I have {num_cats} cats")


val = 0
while val < 1 or val > 10:
    val = int (input ("Enter a number between 1 and 10: "))
    
print(f"Your number was {val}")


# Task 4

from random import randrange

init_invest = 10
current_invest = init_invest
num_days = 0


while current_invest > init_invest * .5:
    
    invest_change = (randrange(31) + 80)/100    
    
    current_invest = current_invest * invest_change
    
    num_days += 1
    
print(f"It took {num_days} to gamble away half of our money")


# Task 5    

for row in range(8):
    for col in range(8):
        
        even_row_col = row % 2 == 0 and col % 2 == 0
        odd_row_col = row % 2 == 1 and col % 2 == 1
        
        if even_row_col or odd_row_col:
            print("w ", end="")
        
        else:
            print("g ", end="")
        
    print()