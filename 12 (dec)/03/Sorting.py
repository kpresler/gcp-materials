# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:16:00 2019

@author: kwame
""" 

import random

def insertionSort(l):
    """
    This function sorts elements in l using insertion sort
    """
    steps = 0
    for i in range(1, len(l)):
        while l[i-1] > l[i] and i > 0:
            steps +=1
            l[i-1], l[i] = l[i], l[i-1]
            i -= 1
    return steps
    
def bubbleSort(l):
    """
    Write a bubble sort algorithm here.
    """

def selectionSort(l):
    """
    Write a selection sort algorithm here
    DO NOT use min or max function!
    """

if __name__ == "__main__":
    l = list(range(10)) # List of integers from 0 to 9

    random.shuffle(l)   # Shuffle list
    print("Unsorted:",l)    
    print("Insertion Steps:", insertionSort(l))
    print("Insertion Sorted:", l)
    
   
    random.shuffle(l)   
    print("\nUnsorted:",l)
    print("Bubble Steps:", bubbleSort(l))
    print("Bubble Sorted:", l)
    
    random.shuffle(l)
    print("\nUnsorted:",l)
    print("Selection Steps", selectionSort(l))
    print("Selection Sorted:", l)
    




