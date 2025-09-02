# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 14:34:56 2025

@author: Kai
"""

# this text, starting with a pound sign, is a comment
# the computer ignores it, but I'll use them to explain
# what my code is doing.  You should get in the habit
# of documenting your code too :)


# the text in green above is _also_ a comment.  Actually, it's a multi-line string
# but Python ignores strings like this, so it serves the purpose of a comment
# when you have comments interspersed with your code, it's fine to use either type
# when you are documenting functions/classes (later!), styling rules will
# have you use multi-line comments to create a _docstring_ (documentation string)
# instead of these.



# Today, we're going to get a "crash course" in some of the fundamentals 
# of programming in Python.  We're not going to get into a lot of depth on 
# any of these topics, but rather just introduce you to concepts that we'll
# spend more time working with in the future


# We generally write programs because we want to do something with _data_
# What does that mean, exactly?  Well, there are multiple different types of 
# data we can work with

# and, crucially, different types of data have different things that you can do with them

# let's see the simplest type of data (at least to us people) -- a string
my_name = "Dr. Kai"

# strings are denoted using either double quotes (") or single quotes (')
# I tend to always use double quotes, but you can use either, as long as you're
# consistent

# What we did above _declared a variable_, and stored a value into it
# Why did we do this?  It's useful for our programs to be able to _keep track_
# of things.  Either constants that we want to specify (like that, above)
# or of data that the program computes while it's running, that we'll need later


# although _we_ like to think in text (which is what strings represent)
# computers like to "think" in numbers.  so, we've got those, too

how_many_apples = 450 # that's a lot of apples!

# we can store whole numbers (integers) like we did above,
# or we can store fractional (floating-point/"real") numbers

liters_to_quarts = 1.05669 # 1 liter is 1.05669 quarts

# once we've got data stored in variables, we can _do stuff_ with it
four_liters_in_quarts = liters_to_quarts * 4

# different types of data let you perform different operations on them
capital_name = my_name.upper() 

# upper() is a _method_ we can call on a string
# which returns a new, uppercase version of that string, while leaving the
# original version un-modified.  Note that this is something you can *only*
# do with strings -- it doesn't make sense to ask "Whats the uppercase
# version of a number?"

# to wit
# comment the next line out out once you've seen it doesn't work
capital_quarts = liters_to_quarts.upper() 

# other stuff -- it's possible to have more interesting arithmetic expressions 
# (we'll learn a bit more about this next class)
# and store the result in a variable

power = 2**10 # the funny looking ** operator is ^, or exponentiation.  so, 2^10


# let's talk a little bit more about how to _run_ our code.  The simplest approach
# (well, maybe not at first glance) is to invoke Python dirrectly and point
# it at a Python script file you've written.  On my Windows computer, from
# the terminal, I can run `python my_script.py` (on a Cursed Mac, or on Linux, 
# instead it would be `python3 my_script.py`)
# this will run the entire script (or, at least until something goes wrong -- 
# if your code tries to do anything illegal, it'll fall over and die at that point)

# however, for a class like this, that's not _really_ how we make a habit of 
# running stuff, at least most of the time

# instead, we tend to run a single expression at a time in Python's REPL
# loop (that's the thing that says "Console" over to the right),

# or run the entire file (that's the green Play button up top).  

# we can also run individual expressions by selecting them and hitting F9

# if you evaluate _individual expressions_  in the REPL loop, Python will 
# display the result of each one.  for example:
"""
In [9]: 2 ** 10
Out[9]: 1024
"""

# This comes, in fact, from what REPL means -- "Read, Evaluate, Print, Loop"

# if you've got a larger script file (like this one, that we're working through)
# Python will _not_ print out the result of every expression (think of the mess!)
# instead, you've got to tell it _when_ to print something.  We can do that, using
# print()

print("Hello, world!") # hey, we saw this last class

# print is a function.  You can pass it zero or more arguments, and it'll print 'em out
print() # yes, this is OK too

print("3 + 4 is", 3 + 4) # this passes _two_ arguments to print -- it evaluates
# 3 + 4, and then prints out the string, and then the sum (7)

# you can also print out variables

print("Hello, my name is " + my_name + "!")

# you can also _interpolate_ variables into strings -- this is particularly
# helpful during printing.  for example:
    
print(f"Hello, my name is {my_name}!")

# this is not required, but makes it easier to get formatting right

# Print can also be configured to _format_ your input in other ways, to make it look better
# We'll learn more about this later, but for now, some examples

num = 20/7 # horrible, irrational floating-point number

print(num) # yuck

print(f"{num:.2f}") # print the number, formatted as a floating-point number, and rounded to two decimal places

print("Student Names:")
print(f"{'Bob':^10}")
print(f"{'Rachel':^10}")
print(f"{'Aleksander':^10}")

# _very_ fancy!


# note that in all of our examples so far, we've been using data
# without regard for what type it is.  We've worked with some strings,
# worked with some numbers, and stuff "just works".  neat.  But, what
# actually is happening here?

# all data in Python _does_ have a type.  We can see as such:
    
print(type(3)) # <class "int">

print(type(3.75)) # <class "float">

print(type("Cave Johnson")) # <class "str"> (strings -- Python just gives 'em a goofy name)

print(type(False)) # <class "bool"> (Booleans -- also named funny)

# sometimes, you want to convert data from one type to another

num_cats = 57

print("I have " + num_cats + " cats.  That's a lot, isn't it?") # fortunately, I don't

# ^ the above is illegal, but not actually because of the number of cats
# as opposed to garbage languages (cough cough, PHP, Javascript), Python is 
# _picky_ about types.  it won't let you do something stupid like using +
# on data of different types where the result is potentially unclear.

print("I have " + str(num_cats) + " cats")

# in addition to str (which converts anything => string)
# we've also got int, float, bool

todays_temperature = "76"

todays_temp_in_c = (int(todays_temperature) - 32) * (5/9)

# you can experiment with float/bool as you see fit


# we've seen how to work with print() for printing things to the console
# (lets the user of our program see stuff -- this is good!)

# there's an inverse function -- input() -- which lets us _prompt_ the user to
# enter in stuff, which we can then read in and do stuff with

# this is Very Useful because it means that the program doesn't use
# the same data every time

temp = input("Please enter today's temperature, in F: ")

# input always returns a string, so we've got to convert to other types before doing
# math with it

temp = int(temp)

temp_in_c = (temp - 32) * (5/9)

print(f"The equivalent in Celsius is {temp_in_c}")


# Notice, we've used a few different arithmetic operator so far.  +, -, *, etc.
# Python supports all if the usual "do stuff with numbers" operators you'd expect
# Also, fortunately, it follows the _order of operations_ you (hopefully)
# remember, going back to primary school: PEMDAS

# Python has a _lot_ more operators than this, more of which we'll see over
# the course of the semester.  I don't try to memorise the order
# of operations for everything (there are rules -- you can see them f.ex
# here: https://runestone.academy/ns/books/published/fopp/Conditionals/PrecedenceofOperators.html )
# but instead use parentheses to make it obvious (to the computer, but more importantly, also to me)
# what I'm trying to do

# we can see some impact of how that works, here

print( 3 + 5 * 8 - 76 )

print( (3 + 5) * 8 - 76 )

print( 3 + 5 * (8 - 76) )


# some other useful operators we've got available

age = 20

is_allowed_to_vote = age >= 18

is_allowed_to_drink = age >= 21

print("Can you vote? " + str(is_allowed_to_vote))
print("Can you drink? " + str(is_allowed_to_drink))

state = "MD"

can_buy_a_flamethrower = state != "MD" and state != "CA" # In California and Maryland, fun is strictly prohibited

print("Can you legally purchase a flamethrower? " + str(can_buy_a_flamethrower))

# note in the example above, we used "And" to glue together two smaller boolean
# expressions.  we'll talk a lot more about this next week when we get into 
# conditional evaluation of code


# We had a good question last class about naming variables
# Different languages follow different conventions.  In Java, the convention is
# called
camelCaseWhereYouCapitaliseTheFirstLetterOfEachWord = True

# in Python, we instead use
snake_case_where_you_separate_words_with_underscores = True

# I find it more annoying to types with all of the _s than capital letters
# but that's the convention, and I'll try to follow it

# in addition to following conventions, try to make sure that
# you've got variable names that are descriptive, but not verbose

# Python won't stop you from using single-letter variable names, but this
# is a Bad Idea, because you'll have no idea what what it means
# on the other hand, the 50-character variables above are nuts

# generally, our examples above, like my_name, can_buy_a_flamethrower,
# etc are reasonable

# another key part of good programming style is _documenting_ your code
# the point of documentation is so that someone (maybe it's you, maybe 
# it's someone else) can come back and figure out what's happening
# good documentation focuses less on the _what_ is happening
# and more on the _why_ things are being done


actual_filename = line[2:] # removes the first two characters from the filename

# ^ that is a bad comment.  It's clear (well, it will be once we talk about strings)
# that this is what's happening, so this comment does nothing useful

actual_filename = line[2:] # trims off the ./ at the beginning of each filename to keep just the name

# ^ This lets us see _why_ we're doing this transformation -- much better!


# note, this is one of the (hopefully very few...) cases where I'll tell you
# Do as I say, Not as I do.

# A lot of the code I provide will be showing you things for the first time
# (or, at least, something close to it) so I will have relatively many
# comments saying _what's_ happening, so if you come back
# to read the code, you can see _what_ was going on.  Your comments
# should be written focusing on the _why_.  I'll try to demonstrate better
# habits when we learn function docstrings later.


# we've got one last thing here -- a brief look at Python's libraries

# One of the things I told you I like about Python is you can write a little
# bit of code that accomplishes a lot.  Part of this comes from Python's
# (very good) set of built-in _libraries_ -- code that's already there, which you
# can use, as part of doing stuff

import math

math.sqrt(400) # 20.0

math.pow(2, 5) # not sure this is better than 2**5, but there you are

circle_radius = 5
circle_area = circle_radius**2 * math.pi

# there are many more things here, if you're curious: https://docs.python.org/3/library/math.html

# another brief thing about numbers
# In normal life, we tend to use base-10
# So, you read 317 as "three hundred and seventeen", or, breaking things up a bit more,
# "three hundreds, 1 ten, 7 ones"

# but, base 10 isn't the only thing we've got available.  We could use base-8 instead
# in which case you'd read
# 317 as "three 64s, one 8, and 7 1s", or, converted back to base 10, 207.

# computers store everything in binary, or base-2.
# 101010111
# what the heck does that mean?

"""
1 0 1 0 1 0 1 1 1
| | | | | | | | ^ 1s place
| | | | | | | ^ 2s place
| | | | | | ^ 4s place
| | | | | ^ 8s place
| | | | ^ 16s place
| | | ^ 32s place
| | ^ 64s place    
| ^ 128s place
^ 256s place

"""

# in other words, we've got 1 256, 1 64, 1 16, 1 4, 1 2, and 1 1.  Sum them all up and that's our answer.

# so, who cares?  The reason that this is relevant is that computers have a "hard time"
# storing floating-point numbers.  In particular, there is almost always a 
# tiny "round-off error" between what we _tell_ the computer to store, and what
# it _actually_ stores.  

# the error is generally so small as to be irrelevant _for the most part_ in terms
# of the end result, but _not_ in terms of boolean expressions

# consider for example:
.1 + .2
# this should obviously be .3
# but, if we ask Python, it'll tell us
0.30000000000000004
# lovely.

# and
print(.1 + .2 == .3)

# we can use the "isclose" function to see if two numbers are _very close_
# essentially, a way to do equality checks that ignore this roundoff error
print(math.isclose(.3, .1 + .2))


# much better!
