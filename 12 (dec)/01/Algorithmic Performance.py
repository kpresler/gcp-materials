# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 11:09:18 2025

@author: Kai
"""


# Algorithms, and algorithm analysis!

# A key part of the study of Computer Science is the study of Algorithms.
# There are many "classic problems" in CS -- ones that show up, over, and over
# again, and for which it's useful to know how to solve them, so that when you
# are faced with these problems, or a variant on them, you know what to do 
# about it.  For many of these problems, there are actually multiple
# solutions, and some of them are still undergoing active research to continue
# the search for better and better solutions


# We'll get a taste of two such problems today -- searching, and sorting,
# and learn a few algorithms that can be used to solve these problems.
# We'll also (briefly) discuss how we can analyse algorithms and figure out
# an approximation for their performance


# suppose I've got a list of numbers, and I want to search through it
# for a certain element.  Well, here in Python, we could use the `in` operator
# to see if that element is present, or, if I care about where, `.index()`

lst = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536]

print(8192 in lst) # True
print(640 in lst)  # False

print(lst.index(32768)) # 13

# OK, great, but what is _actually happening_?  How does this work?


def linsearch(items, target):
    
    # look at all items
    for idx, item in enumerate(items):
        
        # did I find it?
        if item == target:
            
            # return the index
            return idx
    
    # not found
    return -1

print(linsearch(lst, 32768))

# this was an implementation of _linear search_ (called as such because of its
# runtime); also called _sequential search_ because we look at each item 
# sequentially, one at a time


# How do we know that the performance of that code was linear?  Well, let's 
# see a couple smaller examples to work our way up to it


def when_to_wake_up(day):
    
    if day == "Saturday":
        # gotta get up, and do some work around the house
        return "8:30 AM"
    
    elif day == "Sunday":
        # this is my day off!  sleep late!
        return "9 AM"
    
    
    # work/school today
    return "7:30 AM"
    

# what is the peformance of our when_to_wake_up() function?
# Well, the simplest approach is that we can count the number
# of operations that the function performs.  Under 
# simple models (f.ex https://en.wikipedia.org/wiki/Random-access_machine)
# we assume that all "simple steps" (basically, anything other than a loop
# or a function call) has a constant cost of 1.

# In the _best case scenario_ (when day == Saturday) our 
# when_to_wake_up() function completes in _two_ operations -- one 
# for the first if, and one for the corresponding return statement

# in the worst case, it's three operations -- one for the if (which evalutes)
# to false, one for the elif (also false), and one for the return at the end


# let's see another example


# a for loop would be tidier, but this makes the steps easier
count = 0
while count < 500:
    print("I will not throw paper airplanes in class")
    count += 1
    
# what's the performance of this code?  Well, we can follow the "count the steps"
# approach, but account for that some steps will get run multiple times

count = 0                      # run once, at a cost of 1.  total cost == 1
while count < 500:             # run 501 times (500 times condition is
                               # true, final time, condition is false.)  cost of
                               # 1 per check => total cost == 501



    print("I will not throw paper airplanes in class")    # run 500 times, cost 1
                                                          # each.  total == 500
    count += 1                                            # as above -- 500 iterations
                                                          # cost of 1 per iteration
                                                          # => 500
                                                          
# so, the total cost = 1 + 501 + 500 + 500 => 1502 steps

# usually, we are interested in functions (or other blocks of code) where 
# the number of steps is not constant, but _varies_ with some input
# to the function.  Let's get back to linsearch from above, and see what to do

def linsearch(items, target):
    
    # look at all items
    for idx, item in enumerate(items):
        
        # did I find it?
        if item == target:
            
            # return the index
            return idx
    
    # not found
    return -1

# let's say `items` contains 10 elements in it

# in that case, the loop line (for idx, item ...) will run 11 times
# (same logic as the while loop -- once per element, once when it realises
# it's reached the end)

# the _body_ of the loop will run 10 times.  Or, will it?

# In the worst case scenario, yes.  The worst case scenario consists
# of when the element _is not present_ in the list -- you search the whole
# thing, only to not find it.  

# then, the final return runs once. 

# so, something like:
    
def linsearch(items, target):
    
    # look at all items
    for idx, item in enumerate(items):    # runs 11x @ cost of 1/each: 11
        
        # did I find it?
        if item == target:                # runs 10x @ cost of 1/each: 10
            
            # return the index            # _does not get run_
            return idx
    
    # not found
    return -1                             # runs once @ cost of 1: 1

# total cost => 11 + 10 + 1 => 22

# but, that was for a _fixed input_.  in general, we are more interested
# in figuring out the cost _as a function of the (size of the) input_.  
# but, we can do that too

# loop expression runs (size of input) + 1 => n + 1
# loop body runs       (size of input)     => n
# final return runs    (once)              => 1

# total cost = 2n + 2

# note, if n == 10, this gives 22, exactly like what we got before

# in general, we don't bother ourselves with figuring out the _exact_ number
# of steps an algorithm performs.  We are usually content with doing asymptotic
# analysis, or big-O analysis (there are other types of asymptotic analysis
# you'll see if you take DS, but are beyond the scope of this course)

# big-O analysis says "replace all constant factors with 1, and keep only
# the highest-order term".  This lets us focus on the _complexity class_
# of an algorithm -- what is its growth rate as the input size gets arbitrarily
# large.  The advantage of asymptotic analysis is that, after you get some 
# practice, it becomes quick-and-easy to do, and readily lets you see
# the high-level performance of an algorithm.  _then_ you can focus on the 
# details if you really care

# so, for our example above, if the "exact performance" is 2n + 2, 
# the asymptotic performance is O(n) (read as "Big-Oh of N", or just "Oh of N")



def print_every_third(items):
    for item in items[::3]:
        print(item)
        
# this function does approximately a third as much work as one that prints
# every single element (after all, it skips two-thirds of them).  However,
# it does not matter!  If we were to calculate the "exact" number of steps,
# it would be something like:
    
# (.33n + 1) for the loop expression
# (.33n)     for the loop body
# => .66n + 1
# just like we dropped the 2 from our example above, we drop the .66 here.
# it's still linear


# now, some other examples

def print_square(size, what_character):
    
    for i in range(size):
        for j in range(size):
            print(what_character, end = "")
        
        print()
        



# let's reason our way through this.  
# the outer loop expression will run (size + 1) times; its body will run (size) times


def print_square(size, what_character):
    
    for i in range(size):                    # runs `n + 1` times @ cost 1 of per
    
    # ` everything in these ticks runs n times, from the loop its inside
        
        for j in range(size):                # runs `n + 1` times _per iteration of outer loop_
                                             # @ cost of 1 per.  or, 1 * (n + 1) * n => n^2 + n
                                             
            print(what_character, end = "")  # cost of 1, *per iteration* of loop it's in. 
                                             # 1 * (n) * (n) => n^2
    
        
        print()                              # cost of 1 per iteration of loop (n) => 1 * n => n
        
    # `
        
# total cost: (n + 1) + (n^2 + n) + n^2 + n
# => 2*n^2 + 3*n + 1
# we keep only the highest-order term, and drop constants
# so, O(n^2) (or, quadratic)



# Now, let's run through the first set of tasks, do a bit of big-O practice, and
# come back for binary search & some sorting


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