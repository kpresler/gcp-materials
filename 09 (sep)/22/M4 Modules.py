# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 10:21:06 2025

@author: Kai
"""

# We've briefly used a couple of Python's libraries -- the `math` library, and
# the `random` library for random number generation and shuffling elements
# In Python parlance, these are called _modules_

# But, what _is_ a module?

# A module is a Python file that bundles together multiple, usually related, 
# functions, which you can then _import_ and _call_ from another file
# a module can be either a part of a large project (and, in this sense, 
# something where you expect each function to be used only here)
# or a _library_ that provides generally-useful code that you 
# expect to be widely used.  There's no difference in _how_ you define
# the module in either scenario
# Modules may also define constants (things like different colours),
# classes (from which you can create objects -- later), and more -- not
# just functions

# For this, I've got another file I've written, `conversions.py`
# I can _import_ functions from there to use here

bin_str = "11010101"

from conversions import bin_to_hex, bin_to_dec
# alternatively, `from conversions import *`, but that's less elegant
# from conversions import *
# or, `import conversions`, and then call as `conversions.bin_to_dec(...)`

hex_eq = bin_to_hex(bin_str)

import conversions

int_eq = conversions.bin_to_dec(bin_str)


print(f"{bin_str} in base-10 is {int_eq} and in base-16 is {hex_eq}")


# note, when you import a module, Python will run that entire module
# What does this mean?  If all it contains is functions, not really anything
# -- Python will discover that the functions exist, 
# which is what lets you actually call them later on

# if your module contains any expressions _outside_ of functions, 
# they will get run, and their results printed.  This is, usually
# not what you want, so it's best practice to have a "main guard" 
# to protect against it.  Let's see results with and without