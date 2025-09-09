# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 10:02:45 2025

@author: Kai Presler-Marshall
"""


# A crucial component of problem solving is _problem decomposition_
# When tasked with a big, complicated problem, we can solve it by breaking
# it apart into pieces
# these pieces, when composed together, form the solution to the original 
# problem, but are generally easier to solve than trying to do the original
# thing in one go

# to do so, a crucial tool in our toolbox is _functions_

# a function is a group of one or more expressions (usually more, but 
# not always), given a (hopefully descriptive) name
# you can then _call_ a function by name, passing in any arguments required
# and the function will do its thing

# we've used a bunch of Python's built-in functions so far. 

# here we're calling the `len` function built in to Python
# we pass the string "elephant" as an argument to the function
# the function _returns_ a piece of data -- the length of that string
# which we store, so that we can use it later
elephant_length = len("elephant")


# Now, we'll learn how to write our own



# this defines a function, is_positive
# the function has a single parameter, the number we're checking the positivity of
# when the user calls the function, they must pass
# an _argument_ to the function, which is the _specific value_ they
# it then returns a boolean value, True, or False

def is_positive(num):
    if num >= 0:
        return True
    else:
        return False


print(f"Is 37 positive? {is_positive(37)}")
print(f"Is -20 positive? {is_positive(-20)}")


# functins can have multiple parameters, representing the different pieces of 
# information that they need to work

# we've seen some of that before
import math
base = 5
exp = 17
# we must pass math.pow _both_ arguments, or it doesn't know what to do
# otherwise, we'd be asking it to calculate base^??? or ???^exp, and that
# wouldn't make sense
res = math.pow(base, exp)


def convert_to_mins(days, hours, mins):
    hours_in_day = 24
    mins_in_hour = 60
    
    total_hours = hours + (days * hours_in_day)
    total_mins = mins + (total_hours * mins_in_hour)
    
    return total_mins


# this is the total number of minutes in 7 days, 3 hours, and 55 minutes
mins1 = convert_to_mins (7, 3, 55)

print(f"Result is {mins1}")

# There is no reason that I was _required_ to define the 
# convert_to_mins function
# I could have _inlined_ its body (the five indented expressions)
# here instead, and the code would have worked just as well
# however, it is _much easier_ to _read_ code that uses functions -- I can
# focus on the higher-level "What does this thing _do_?" instead of the
# lower-level "How is this thing doing it?"



# another benefit -- once I've got a function called, I can 
# _call it again_ with different arguments, and no copy-paste of the code req'd

mins2 = convert_to_mins(25, 6, 43)
print(f"Result is {mins2}")

# sometimes, you create functions that have no parameters
# these functions can either source their data themselves
# for instance, using `input()`, or reading over the network, etc
# note, the () are still req'd, when defining, and calling, the function

def sum_of_two():
    first = int (input ("Please enter a number: "))
    second = int (input ("Please enter another number: "))
    
    result = first + second
    
    return result

num_sum = sum_of_two()
print(f"Sum is {num_sum}")

# for things like the above, however, parameters are generally better than `input`
# Using parameters makes it so that your function can be used more broadly 
# because its data can come from anywhere, and not just prompting the user



# it's a good practice to _document_ our functions
# we do so by providing a _docstring_, which goes directly below the function's
# def line, and before the rest of its body


def convert_to_mins(days, hours, mins):
    """
    Calculates the total number of minutes elapsed,
    given a number of minutes, hours, and days
    Parameters
    -------
    days : int
         Number of complete days elapsed
    hours : int
        Number of hours elapsed, past the last day
    mins : int
        Number of mins elapsed, past the last hour

    Returns
    -------
        int: Total number of minutes
    """
    hours_in_day = 24
    mins_in_hour = 60
    
    total_hours = hours + (days * hours_in_day)
    total_mins = mins + (total_hours * mins_in_hour)
    
    return total_mins

# It may seem excessive here that we've got a docstring that's longer than
# the body of the function itself.  I do get that argument, and the _format_
# of the docstring is not something I will be extremely pedantic about
# however, as your functions get more complicated, the necessity of 
# good docstrings continues to increase


# there's no required format for docstrings -- they are ignored by the Python
# interpreter, and their presence, or absence, has no impact on whether
# the function runs, correctly or otherwise.  
# so, it's OK if what you've got doesn't line up precisely with what we've
# got there, but you _should_ be including basically the same information