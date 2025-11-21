# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 14:10:16 2025

@author: Kai
"""


# Task 1

def product_of_list(nums):
    
    if len(nums) == 1:
        return nums[0]
    
    else:
        return nums[0] * product_of_list(nums[1:])
    
    
print(product_of_list([5,4,2,10]))
    
    
    
# Task 2

def double_chars(string):
    
    if len(string) == 0:
        return ""
    
    if len(string) == 1:
        return string[0] + string[0]
    
    else:
        return string[0] + string[0] + double_chars(string[1:])
    
print(double_chars("apple"))