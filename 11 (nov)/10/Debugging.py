# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 10:42:49 2025

@author: Kai
"""


# The readings for today talked a lot about how to fix the "easy" bugs --
# ones where you've used a variable that doesn't exist, tried to call a function
# that doesn't exist, and stuff like that.  These are pretty easy bugs to fix,
# all things considered, because the consequences are very easy to see --
# your program errors out partway through

# Much harder bugs to find (and fix!)
# are _logic errors_ -- ones where your program runs, and doesn't crash along
# the way, but then the answer, or output, is wrong.

# One straightforward approach for this sort of debugging is called 
# "printf debugging", and involves adding a bunch of `print()` calls to your
# program so that, as it runs, you can watch what it's doing.
# If you're not sure which branch of an if/elif/else is being taken, or 
# how many iterations your loop is running, or exactly the type of a variable,
# adding print statements is a solid starting point to start understanding
# what's happening.

# That being said, for all but the _very smallest_ programs, printf debugging
# is not the ideal solution.  One thing that we take for granted is that our
# programs pretty much run instantly (unless they're waiting for user input)
# -- programs of the size that you'd write in (most) undergrad CS courses
# are _so fast_ that all of the output comes out at once.  This makes it somewhat
# difficult to match the output that you see in the console to what your
# program was actually doing.  So you only really get a posthumous view of 
# what your program is doing.  You can't really see what it's doing, 
# as it actually does it



# In order to get a better picture, and thus be able to better 
# understand what our program is doing, we need better tools.  The tool
# that helps here is called a _debugger_, and it's a feature built into
# all IDEs (that, after all, is the point of an IDE -- they Integrate tools
# you need for Developing code into a single Environment).  

# While the specific buttons we'll see next are unique to Spyder,
# all of the concepts we'll see next translate to other debuggers, f.ex in
# Eclipse, IntelliJ, or even more primitive tools like GDB.


# The starting point when using a debugger is to _set a breakpoint_
# This is what tells the debugger, "When you're running the code, don't run 
# all the way to completion.  Stop here, and wait for me to tell you what
# to do next"

# To do that, click _just to the right_ of the line number where you want the 
# debugger to wait

name = "John Smith"

print(f"Hello, {name}")

# then, after that, click the blue Play/Pause button in the top menu bar
# (instead of the normal green Play button)

# this launches the code in Debug Mode, which activates the debugger
# then, rather than running to completion, Python will _stop_ at the 
# first breakpoint it hits, and wait for you to tell it what to do
# you can then inspect variables (including temporary ones), like
# local variables inside a function, loop variables, etc
# and see what's happening.  

# this is where you apply your Keen Intellect to try and figure out what's 
# happening.  Do the values in the variables _look right_?  Have we taken
# the right branch if we've got conditional logic?

# Note, when the debugger hits a breakpoint, it stops _before_ it runs the 
# code on that line.  If you want to see what happens _after_ that line, you 
# have got a couple of options:
#  enter the `!next!` command in the debugger terminal
#  Click the "Step Over" button (Called "Debug current line" if you hover)
#  Click the "Step Into" button (called "Step Into Function or Method")
#  Click the "Step Return" button (called "Execute until function or method returns")
# these options, together, let you 

# let's go see how to use these options to investigate a more interesting problem



# algorithm from: https://en.wikipedia.org/wiki/Trial_division#Method

def factors(num):
    factors = list()
    
    small_primes = primes_up_to( int (num**.5) + 1)
    
    # loop through small prime numbers that might be factors of our desired one
    for p in small_primes:
        
        # Is it a factor of our number?
        if num % p == 0:
            factors.append(p)
            num //= p
    
    
    # if we're left over with a prime number after all this,
    # then it's the last factor
    if is_prime(num):
        factors.append(num)
        
    return factors

def is_prime(num):
    
    if num == 1:
        return False
    if num == 2:
        return True
    
    for possible_factor in range(2, num):
        if (num % possible_factor) == 0:
            return False
    
    return True


def primes_up_to(n):
    res = list()
    for num in range(1, n + 1):
        if (is_prime(num)):
            res.append(num)
    
    return res


fac = factors(36)
print(fac)
