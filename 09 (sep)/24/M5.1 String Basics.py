# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 11:14:22 2025

@author: Kai Presler-Marshall
"""



# Strings are Python's datatype for working with _text_
# We've learned a bit about strings, which we'll
# first remind ourselves of, and then see some new stuff

e = "This is some text in English, using characters we all recognise"

d = "Denne tekst er på dansk med et ekstra tegn"

c = "這篇文章是中文的，有很多新字"

print(e)
print(d)
print(c)

x = "This is a string denoted with double quotes"
y = 'This is a string denoted with single quotes'

# z = 'This is an invalid string, b/c the quotes do not match"

# q = “copy-and-paste doesn't tend to work too well from PowerPoint, or anything else with so-called "smart quotes" ”

a = "This is the first half"
b = " and this is the second half"

# we can _concatenate_ strings using +
full_string = a + b

print(full_string)


# if you multiply a string by an int, the string
# gets repeated that many times
print("Na"*10 + " Batman!")


# illegal!  can't concatenate other things to a string
does_this_work = "This is a string" + 5

temp = 6

temp_message = "The temperature today is " + str(temp)

print(temp_message)


# alright, now some time for new stuff

# if we've got a string, we can _extract_ characters out of it using []
#             0123456
this_class = "EN.500.113 Gateway Computing: Python"

print(this_class[0]) # 0th character (E)
print(this_class[1]) # 1st character (N)
print(this_class[2]) # 2nd character (.)
print(this_class[3]) # 3rd character (5)
# ....and so on and so forth

# notice how strings (and lists, and tuples, and other "things")
# are zero-indexed.  so, the "first" element is at index 0, not 1

# we can also index into a string from the right side

print(this_class[-1]) # last character (n)
print(this_class[-2]) # second-to-last character (o)
print(this_class[-3]) # third-to-last character (h)

# you might be wondering...in addition to using [] to access characters out of a string
# can we also _change_ the string like so?

# nope!
# TypeError: 'str' object does not support item assignment
this_class[3] = "6"

# Strings in Python, like in _most_ other languages are _immutable_
# that is, you can't change a string to be a different string
# you can generate _new_ strings (that's what the concatenation, repetition etc)
# does, but it's a _new_ string, not changing the original object
# when we learn about lists (next module!) we'll see how they
# are our first _mutable_ datatype


# in addition to extracting single characters out of strings
# we can also _slice_ strings to extract multiple characters

class_prefix = this_class[0:2] # grabs characters 0 & 1 (EN)
class_dept = this_class[3:6] # grabs characters 3, 4, 5 (500)
class_num = this_class[7:10] # grabs characters 7, 8, 9 (113)
class_name = this_class[11:] # grabs characters from 11 to the end

# note something pretty important about what we've got above
# when you're slicing a string, the _start index_ is inclusive
# and the end index is _exclusive_

# so this_class[0:2] is from 0, inclusive, up to, but not including, 2
# this is nice because it means you can take consecutive 
# slices of a string and you get no overlap/repetition
# in our case, we are deliberately _not_ taking consecutive
# slices, since we want to drop the `.`s and ` `, but YMMV

# notice something else about slicing
# either (and in fact, both) indices are optional
# we had
class_name = this_class[12:]

# if you don't have an end index, it says to go all the way to
# the end of the string

# if you don't have a start index, it says "start at the beginning"

class_prefix = this_class[:2] # this is a fine way to extract characters 0 & 1

# "start at the beginning & go all the way to the end"
# this creates a _copy_ of the entire original string
entire_str = this_class[:]


# more slicing

import string

all_letters = string.ascii_lowercase

# "start at the beginning, run to the end, and walk our way forward
# by two elements at a time"
every_other_letter = all_letters[0:len(all_letters):2]

# other, more advanced, stuff

# "start at index 10, go to index 5, and do so by decrementing
# the index by 1 each time"
reverse = all_letters[10:5:-1]

# note that :-1 part is really important
# in this case, it's going to increment the index by 1 each time
# but `start` is already past `end`, so we get nothing
reverse_wrong = all_letters[10:5]

# if we want to _reverse_ a string, that's easy too

all_reversed = all_letters[::-1]



# let's learn about some string _methods_ that we can use to 
# generate transformations of strings 

original = "Hello World!"

# WANT TO SOUND REALLY EXCITED?
# HOW ABOUT YELLING ALL THE TIME?
print(original.upper()) # prints HELLO WORLD!

# maybe you're tired of being yelled at now
# can't blame you
print(original.lower()) # prints hello world!

new_str = "this is all lowercase"

# the capitalize method will capitalise
# the first letter of the string
print(new_str.capitalize()) # prints This is all lowercase

# the title method will capitalise the first 
# letter of each word in the string
print(new_str.title()) # prints This Is All Lowercase


# WARNING: COMMON BUG! #
# this capitalises the string and then
# immediately throws it in the trash
new_str.upper()


# You almost always want to do something like this instead
# this puts the capitalised version back into a varible 
# so we can use it later
new_str = new_str.upper()