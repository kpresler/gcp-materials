# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 14:54:05 2025

@author: Kai
"""

# Python gives us tremendous flexibility for controlling the
# formatting of strings
# this is particularly useful for making formatted output that 
# doesn't look like crap

# ignore the dictionary part for now -- we'll cover those later
# but it gives us something interesting to print, formatted
ages_dict = {"Bobby": 25, "Jane": 28, "Ralf": 20, "Nancy": 30, "Michael": 24}

print("Name       Age")
for name, age in ages_dict.items():
    print(f"{name} {age}")
    
# the exact output is
"""
Name       Age
Bobby 25
Jane 28
Ralf 20
Nancy 30
Michael 24

"""
# looks terrible, right?  well, let's un-terrible it

print(f"{'Name':12} {'Age':3}")
for name, age in ages_dict.items():
    print(f"{name:<12} {age:>3}")
    
# there's a couple things we did there
# the :12 part (and corresponding :3)
# says "I want this element to be a total width of 12 (or 3) characters"
# based on the _original width_ of the item, Python will pad it with
# enough spaces to make that desired with.  "Michael" is longer
# than "Jane" so his name gets fewer spaces than hers
# yet they both will get spaces added to end up with a total width of 12


# note we've also got the <12 and >3.  This does not mean 
# "the width must be less than 12".  instead it means that the text
# should be left-aligned within the total width of 12 that is used.
# correspondingly, >3 says "right-align the text within a width of 3".
# You can also do something like ^12 to centre the text and add
# padding on both sides

one_third = .875

print(f"If you divide 1 by 3, you get {one_third}")

# this is maybe more precision than we want, most of the time.  just two decimal
# places is often satisfactory, or even preferred.  We can use 
# format strings to control this, too

# "display this as a floating-point number, to two decimal places"
print(f"If you divide 1 by 3, you get {one_third:.2f}")


# one last thing about strings!

# we saw previously that you can loop through all of the characters in a string

our_loc = "Baltimore Maryland"
for char in our_loc:
    print(char)

# what if we want words, but not chars?

our_loc_words = our_loc.split()

# this _splits_ the string into a list (soon!) of strings
# the default split character is a space, so we get the list
# ["Baltimore", "Maryland"]

# thus

for word in our_loc_words:
    print(word)

# suppose we've got a strangly formatted string
odd = "this.string.is.written.really.oddly.because.maybe.my.spacebar.is.broken"

words = odd.split(".")

# ahhh, much better :)
for word in words:
    print(word)
    
    
# we can also do the reverse -- convert a list of strings
# into a single string by _joining_ them together

# join all of the words from our list together, using a space (" ")
# as the separator character between each element
reassembled = " ".join(words)

# we can use whatever we want as the joining character, however

# let's image our assembly instructions came from IKEA, so we've 
# got bits of Swedish stuck throughout what we're making
oddly_assembled = "åö".join(words)

# oddly_assembled = thisåöstringåöisåöwrittenåöreallyåöoddlyåöbecauseåömaybeåömyåöspacebaråöisåöbroken
# lovely (?)


