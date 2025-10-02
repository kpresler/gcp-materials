# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 14:13:12 2025

@author: Kai
"""

# Task 1

units = [ 
    ["inch", "foot", "yard", "mile"], 
    ["teaspoon", "tablespoon", "cup", 
     "pint", "quart"] 
]


# 1.1
units[0][0]

# 1.2
units[0][0][-1]


# 1.3
units[0]

# 1.4
units[1][2:4]



# Task 2
# 2.1
numbers = [4353, 2314, 2956, 3382, 9362, 3900]
numbers.remove(3382)

# 2.2
numbers = [4353, 2314, 2956, 3382, 9362, 3900]
idx = numbers.index(9362)

# 2.3
numbers = [4353, 2314, 2956, 3382, 9362, 3900]
numbers.insert(5, 4499)

# 2.4
numbers = [4353, 2314, 2956, 3382, 9362, 3900]
numbers.extend([5566, 1830])
# OR
numbers.append(5566)
numbers.append(1830)

# 2.5
numbers = [4353, 2314, 2956, 3382, 9362, 3900]
numbers.reverse()

# 2.6
numbers = [4353, 2314, 2956, 3382, 9362, 3900]
numbers.sort()


# Task 3
def somewhat_buggy_count(lst, item1, item2):
    if item1 not in lst and item2 not in lst:
        return -3
    elif item1 not in lst:
        return 6
    elif item2 not in lst:
        return 4
    
    return lst.count(item1) + lst.count(item2)
