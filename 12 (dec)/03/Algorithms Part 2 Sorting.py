# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 08:52:42 2025

@author: Kai
"""

# we've got a faster algorithm, _binary search_, if we know that our collection
# of elements is in order.  In fact, I showed you a sneak-peak of this algorithm
# when we did our work with `while` loops earlier, and played a guessing game
# if I'm asked to guess a number between 1 and 1000, I _could_ try each 
# one, sequentially.  but it's not a very smart approach.  suppose our number 
# is 880.  If I try guessing 500, I can, with one guess, 
# immediately eliminate half of the search space.  Now, I know the number must
# be between 500 and 1000.  so I try 750.  bam, half the search space gone, 
# again.  Now, I try 875.  half, gone again.  now 937.  half again, gone.

# binary search in a list works basically the same way.  Let's see an example
# on the board, and then see how the code works

def binsearch(items, target):
    
    lo = 0
    hi = len(items) - 1
    
    
    while lo <= hi:
        mid = (lo + hi) // 2    
        
        item = items[mid]
        
        if item == target:
            return mid
        
        if item < target:
            lo = mid + 1
        
        else:
            hi = mid - 1
            
    return -1 # not found
    
    
lst = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536]

# make sure we can find every element that _is_ there, at the right spot
for item in lst:
    assert binsearch(lst, item) == lst.index(item)
    
# make sure an element past the end of the list isn't found
assert binsearch(lst, 131072) == -1

# make sure an element past the other end of the list isn't found
assert binsearch(lst, 1) == -1

# make sure an element not present in the middle of the list isn't found
assert binsearch(lst, 3072) == -1



# and now, on to sorting algorithms!

# another classic problem in computer science is _sorting_ collections of elements
# this might seem like a "solved" problem -- and indeed, it _is_ solved
# there are _many_ algorithms that will do this, and a good one is built-in
# to Python already.  However, knowing what the computer is doing is important
# and depending constraitns you face, you might choose between different 
# algorithms.

def insertionSort(lst):
    """
    This function sorts elements in lst using insertion sort
    """
    
    for i in range(1, len(lst)):
        while lst[i-1] > lst[i] and i > 0:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            i -= 1


def mergesort(nums):
    """recursive mergesort implementation"""
    
    # base case -- a list of 0 or 1 elements is already implicitly sorted
    if len(nums) < 2:
        return nums
    
    
    # otherwise, split the list in half, and merge-sort each half
    med = len(nums)//2
    
    
    # recursive call on the first half
    left = mergesort(nums[:med])
    
    # recursive call on the second half
    right = mergesort(nums[med:])
    
    # reassemble into the overall solution
    return merge(left, right)
    
    
    
def merge(left, right):
    """merges two sorted lists together into a complete, also sorted, list"""
        
    total_to_merge = len(left) + len(right)

    l_idx = 0
    r_idx = 0
    out = list()
      
    
    while len(out) < total_to_merge:
        if r_idx == len(right):
            out.append(left[l_idx])
            l_idx += 1
        elif l_idx == len(left):
            out.append(right[r_idx])
            r_idx += 1
        elif left[l_idx] < right[r_idx]:
            out.append(left[l_idx])
            l_idx += 1
        else:
            out.append(right[r_idx])
            r_idx += 1
    return out
    
    
from random import randrange
nums = [randrange(100) for _ in range(100)]

sorted_nums = mergesort(nums)
sorted_with_python = sorted(nums)

for i in range(len(sorted_nums)):
    if sorted_nums[i] != sorted_with_python[i]:
        raise ValueError(f"error at idx={i}, expected={sorted_with_python[i]}, actual={sorted_nums[i]}")
print("Hey, it worked!")

print(f"original={nums}")
print(f"sorted={sorted_nums}")
