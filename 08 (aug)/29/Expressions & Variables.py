# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 13:04:25 2025

@author: Kai
"""

# note -- when we enter expressions directly into the Python shell, it'll evaluate them & display the result
# however, when we run a .py file like this, expressions don't have their result displayed unless we use `print`

# for example, if I select the following expression & evaluate it (or, put your cursor on the next line, & hit F9), we get to see the output
# however, if we run the entire script, it doesn't show up
"hello world".upper()


# some arithmetic operations
print(3**5) # 3 to the 5th

print(3//5) # 3 integer divide 5

print(3*(3**3) - 3) # compound expression -- parentheses would be good!



# let's use variables to break things up into pieces

temperature_f = 96 # not ideal :(

temperature_c = (temperature_f - 32) * (5/9)

print(temperature_c)



# more examples with variables

gcp_instructor = "Dr. Kai"

print(gcp_instructor) # prints `Dr. Kai` (with no ticks)


# this loses Dr. Kai, since each variable can only store one thing
gcp_instructor = "Dr. Kutten"



# prints `Dr. Kutten` (with no ticks)
print(gcp_instructor) 


# let's calculate the volume of a circular prism
import math
h = 10
r = 5

area_end = math.pi*r*r # alternative: pi*r**2
volume = area_end * h
print(volume) # 785


# suppose we're trying to ship a box of rice, and we've been told that the
# maximum weight that we can put in the box is 5 pounds
# let's figure out how much rice we can fit

# apparently a grain of rice weights about .03 grams
rice_weight = .03

# first, handle unit conversion
# 1 gram = .035... ounces
gram_to_ounce_conversion = 0.035274

rice_weight_ounce = rice_weight * gram_to_ounce_conversion

rice_in_pound = 16 / rice_weight_ounce #16 for ounce -> pound

rice_total = rice_in_pound * 5 # for 5 pounds

print(int(rice_total)) # int allows only for whole grains of rice

# apparently about 75,500 grains of rice
# I hope I don't have to count that


# note -- be careful -- we must use =, and not ==
# = is used to _assign_ a variable to store something
# == is used to check, "Are these two things equivalent?"

# so
x = 5 # stores 5 in x
x == 7 # checks "is x equal to 7?" (no, x is equal to 5)
y = 20
x == y # are these variables equal? (that is, do they store the same value?) (no)
x = 20
x == y # and now, they are



# we can store the value of one variable into another variable, too

my_shipping_address = "3400 N Charles Street, Baltimore, MD 21218"

my_billing_address = my_shipping_address

# note, however, that updating one won't update both

my_shipping_address = "3400 N Charles Street, Malone Hall 160, Baltimore, MD 21218"

# shipping address is updated
print(my_shipping_address)

# billing address is unchanged

print(my_billing_address)


# note at this point we've seen a few different types of data

# -4 is an int
# 1.8 is a float
# False is a bool(ean)
# "3400 N Charles Street, ...." is a str(ing)

# some operations are legal on some datatypes, but not others

# we can glue strings together

num_trees = "4"

msg = "I have " + num_trees + " olive trees." 


# the more natural version -- having `num_tees` stored as an `int`, however
# doesn't work
num_trees = 5
msg = "I have " + num_trees + " olive trees."



# some other potentially useful things we can do with numbers

# / does (fractional) division

5/3 # 1.66666666
10 / 5 # 2.0 (you _always_ get a float, even if the result can be expressed as an int)

# // does integer division
# this throws away whatever is left after the decimal place

5 // 3 # 1
10 // 5 # 2

# % is the modulus operator
# if you don't remember it, it's the "what's left over after division?"

5 % 3 # 2
10 % 5 # 0

# perhaps the most useful thing we can do with these is _extracting_ a certain digit from a number

# let's see how this works
# suppose we've got
num = 34567

# I want to get the digit in the 100s place
# to do so, I can throw out everything to the right of it
num = num // 100

# then I can grab the last digit
print (num % 10)

# another example

# suppose I've got 397 cents.  I want to figure out how many quarters that is, and what's left over after making as many quarters as I can

print (397 // 25) # how many quarters can I make?

print (397 % 25) # what's left over after doing so?


# Python is not limited to only the characters that we use in English
name = input ("Please enter your name: ")

greeting_en = "Hello, " + name + "!"
greeting_es = "¡Hola, " + name + "!"
greeting_ru = "Привет " + name + "!"

print (greeting_en)
print (greeting_es)
print (greeting_ru)
