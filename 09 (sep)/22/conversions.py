# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 11:58:42 2025

@author: Kai Presler-Marshall
"""


def bin_to_dec(bin_str):
    """This should be documented better"""
    
    reverse = bin_str[::-1]
    
    acc = 0
      
    for idx, char in enumerate(reverse):
        assert char in ("0", "1")
        acc += int(char) * 2**idx
    
    
    return acc



def bin_to_hex(bin_str):
    """This should be documented better"""
    
    reverse = bin_str[::-1]
    
    hex_digits = "0123456789ABCDEF"
    
    acc = 0
    hex_str = ""
    
      
    for idx, char in enumerate(reverse):
        assert char in ("0", "1")
        acc += int(char) * 2**(idx - 4*len(hex_str))
        
        if (idx + 1) % 4 == 0:
            hex_str = hex_digits[acc] + hex_str
            acc = 0
            
    
    if (idx + 1) % 4 != 0:
        hex_str = hex_digits[acc] + hex_str
    
    
    return hex_str


if __name__ == "__main__":
    print(bin_to_hex("1111011110"))

    print(bin_to_dec("11011"))
     