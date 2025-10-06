# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 11:30:17 2025

@author: Kai
"""

# Task 1.1

def list_intersection(list1, list2):
    intersection = list()
    
    for item in list1:
        if item in list2:
            intersection.append(item)
            
    return intersection

# second version, with list comprehension

def list_intersection(list1, list2):
    return [item for item in list1 if item in list2]


list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

print(list_intersection(list1, list2))


# Task 1.2

def list_sym_diff(list1, list2):
    first_uniq = [item for item in list1 if item not in list2]
    
    second_uniq = [item for item in list2 if item not in list1]
    
    return first_uniq + second_uniq


list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

print(list_sym_diff(list1, list2))

# Task 1.3

def list_interleave(list1, list2):
    
    target = list()
    
    max_idx = max(len(list1), len(list2))
    
    for idx in range(max_idx):
        if idx < len(list1):
            target.append(list1[idx])
            
        if idx < len(list2):
            target.append(list2[idx])
    return target


list1 = [1,2,3,4,5]
list2 = [40,50,60]

print(list_interleave(list1, list2))


# Task 2


def third_index_of(my_items, item):
    if my_items.count(item) < 3:
        return None
    
    first_index = my_items.index(item)
    
    new_list = my_items[first_index + 1 : ]
    
    second_index = new_list.index(item)
    
    new_list = new_list[second_index + 1 : ]
    
    third_index = new_list.index(item)
    
    return (first_index+1) + (second_index+1) + third_index


my_items = [1,2,3,2,3,4,3,2]


# Task 3



def factors(n):
    #fact = list()
    
    return tuple( num for num in range(1, n + 1) if n % num == 0 )

    # another approach, not using tuple comprehension
    """
    for num in range(1, n + 1):
        if n % num == 0:
            fact.append(num)

    return tuple(fact)

"""