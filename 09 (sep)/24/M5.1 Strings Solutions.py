# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:29:17 2025

@author: Kai
"""

def format_address(name, street, city, state, zip_code):
    
    return f"{name}\n{street}\n{city}, {state} {zip_code}"



print(format_address("Dr. Kai", "3400 N Charles Street", "Baltimore", "MD", "21218"))




def mangle_text(some_string):
    
    mid = len(some_string) // 2
    
    first = some_string[:mid]
    last = some_string[mid:]
    
    first = first.lower()
    last = last.upper()
    
    return last + first


print(mangle_text("SomeText"))




def roman(c):
    
    if c == "I": return 1
    if c == "V": return 5
    if c == "X": return 10
    if c == "L": return 50
    if c == "C": return 100
    if c == "D": return 500
    if c == "M": return 1000
    
    return 0


def romanToInt(s):
    
    num = 0
    
    for idx in range(len(s) - 1):
        
        char = s[idx]
        next_char = s[idx+1]
        
        this_val = roman(char)
        next_val = roman(next_char)
        
        if this_val < next_val:
            num -= this_val
        else:
            num += this_val
            
    num += roman(s[-1])
            
    return num

print(romanToInt('MCMXCIV'))
        
    
    