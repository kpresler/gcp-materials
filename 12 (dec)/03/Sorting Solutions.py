# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 13:14:01 2025

@author: Kai
"""

def binsearch(items, target):
    
    lo = 0
    hi = len(items) - 1
    
    comp = 0
    
    while lo <= hi:
        mid = (lo + hi) // 2    
        
        item = items[mid]
        
        comp += 1
        if item == target:
            print(f"Found the target in {comp} comparisons")
            return mid
        
        comp += 1
        if item < target:
            lo = mid + 1
        
        else:
            hi = mid - 1
        
    print(f"Failed to find the target after {comp} comparisons")
    return -1 # not found


def bubbleSort(l):
    """
    Bubble sort: O(n^2)
    """
    steps = 0
    for j in range(len(l)-1):
        for i in range(len(l) - 1 - j):
            if l[i] > l[i+1]:
                steps +=1
                l[i], l[i+1] = l[i+1], l[i]

    return steps

def selectionSort(l):
    """
    Selection sort:  O(n^2)
    """
    steps = 0
    for j in range(len(l)-1):
        minIndex = j
        for i in range(1+j,len(l)):
            if l[i] < l[minIndex]:
                steps += 1
                minIndex = i
        l[j], l[minIndex] = l[minIndex], l[j]
    return steps