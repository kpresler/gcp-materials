# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 11:27:05 2025

@author: Kai
"""


# Task 1

def total_bill(meal_amt, sales_tax = .06, tip_percent = .15):
    
    tax_amount = meal_amt * sales_tax
    
    tip_amount = meal_amt * tip_percent
    
    return meal_amt + tax_amount + tip_amount


bill_total = total_bill(100, tip_percent=.08)

print(bill_total)



# Task 2

def stddev(nums):
    
    avg = mean(nums)
    
    total_variance = 0
    
    for num in nums:
        total_variance += (num - avg)**2
        
    avg_variance = total_variance / len(nums)
    
    dev = avg_variance ** .5
    
    return dev
    
    
def mean(nums):
    
    #return sum(nums) / len(nums)
    
    total = 0
    count = 0
    
    for num in nums:
        total += num
        count += 1
        
    return total / count

nums = [10, 7, 14, 3, 6, 21]
stdev_nums = stddev(nums)



# Task 3


def is_prime(num):
    
    for potential_factor in range(2, num):
        
        # if the number divies evenly by anything less than it, not prime
        if num % potential_factor == 0:
            return False
        
    # if it divided evenly by nothing, then it is prime
    return True


def primes_up_to(num):
    
    # 0 & 1 aren't prime, so we start range at 2
    # also, the +1 to make the end num inclusive
    
    for i in range (2, num + 1):
        if (is_prime(i)):
            print(i)
    