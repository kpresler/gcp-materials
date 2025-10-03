# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 09:56:41 2025

@author: Kai
"""


# one final topic with lists -- list comprehension!

vegetables = ["squash", "carrots", "pumpkin", "beans", "potatoes"]

# we know how to loop through a collection of elements and print them
for vegetable in vegetables:
    print(vegetable)
    
# or make a new list
upper_veggies = list()

for vegetable in vegetables:
    upper_veggies.append(vegetable.upper())
    
for veggie in upper_veggies:
    print(veggie)
    
    

# loops & conditionals
# we can also loop through a collection of elements, and apply some 
# conditional logic to each one, rather than doing something with _every_
# element
animals = ["elephant", "cat", "ant-eater", "hippopotamus", "dragonfly"]

long_animals = list()
for animal in animals:
    if len(animal) > 3:
        long_animals.append(animal)
    
print(long_animals) # ["elephant", "ant-eater", "hippopotamus", "dragonfly"]



for _ in range(10):
    print("Demo")
    
# We also know how to loop through a range of numbers, and
# for each number, transform it and stick it into a list
# (well, actually, I've not showed you exactly this, but)
# I _have_ showed you all of the pieces
nums = range(1, 11)
final_list = list()
for num in nums:
    my_list.append(num**3)
    


# now, we'll see how we can use syntax known in Python as 
# _list comprehension_ to quickly and efficiently generate
# a new list from an existing list-like structure

# we'll see how to condense this further in a moment
existing_list = list(range(1, 11))

# exhibit 1
# what does this crazy syntax mean??
# the square brackets we've seen, that's used
# to denote a list

# `for element in existing_list` we've also seen, already
# in a slightly different context (standard for loop)

# this says, "Loop over each element in the existing list"
# and then, put in a new list whatever the first expression
# in our case `element**3` evaluates to
new_list = [element**3 for element in existing_list]

print(new_list)


# exhibit 1.1.  same idea, just a list of strings
# and a different expression for generating our new list
star_trek_characters = ["Pavel Chekov", "Mr. Scotty", "Captain Kirk", "Spock"]

capital_characters = [character.upper() for character in star_trek_characters]

print(capital_characters)


# exhibit 2
# looping over a range
squared_numbers = [num**2 for num in range(17)]
print(squared_numbers)


# exhibit 3
# filtering.  so far, we'd do something like this

squared_numbers = []

for num in range(17):
    if num % 2 == 0:
        squared_numbers.append(num ** 2)

print(squared_numbers)

# better :)
squared_numbers = [num**2 for num in range(17) if num % 2 == 0]
print(squared_numbers)


print(star_trek_characters)


# just because you can, does not mean that you should
# please don't write code like this.  if you're trying to do this much, 
# use a standard for loop.  it'll be a lot easier to read.
mangled_characters = [ (character.upper() if idx % 2 == 0 else character.lower()) for idx, character in enumerate(star_trek_characters) if len(character) > 5]



some_characters = [character.upper() for character in star_trek_characters if len(character) > 5]

# this generates a new list, and immediately throws it away.  Not ideal :(
[character.upper() + " is the best" for character in star_trek_characters]




# one other thing, while we're at it
# recall previously I told you how functions can return multiple values
# well, what _actually_ happens when you return multiple
# values from a function is that Python generates a _tuple_

# Tuples are another data structure built into Python.  Like 
# lists, Tuples store elements sequentially.
# however, there are a few key differences:
#  first, their purpose.  Lists are usually used for storing homogenous 
#    collections, like storing all of the students enrolled in a class
#    or storing a list of players on a baseball team
#    tuples, by contrast, are generally used for storing _heterogeneous_
#    collections of elements -- ones where, generally, it doesn't make
#    sense to loop over all of the elements and do the same thing
#    with each one.  You _can_ loop through a tuple, but it usually
#    indicates that you're doing something that is, if not wrong, odd
#  second, tuples are _immutable_, like strings.  Once you've created
#    a tuple, you can't modify it.  You can create a _new_ tuple, but 
#    cannot change an existing one.

# finally, there's a matter of syntax -- tuples are created using 
# (parentheses) instead of [square brackets]
# otherwise, you create them the same way, comma-separating their values

bob = ("Bob Smith", 37, "bob@gmail.com", "3400 N Charles Street")

# we can access elements from a tuple like so
bobs_name = bob[0]
bobs_age = bob[1]
bobs_email = bob[2]
bobs_addr = bob[3]

# You can also _unpack_ a tuple back into its individual elements
bobs_name, bobs_age, bobs_email, bobs_addr = bob

# like with lists, you can slice a tuple
three_fourths_of_bob = bob[1:]
# however, this is generally not very useful given what you do with 'em

# a few other nuances with tuples

# first, if you're creating a tuple with one element, 
# you have to add a trailing comma
# however, since creating a tuple of a single elements is odd
# (both in length and purpose -- it's not like a list of one element,
# since you generally don't loop over a tuple), 
# this is not of supreme concern

dmitry = ("Dmitry Mendeleev",)
print(type(dmitry)) # <class 'tuple'>
print(dmitry) # ('Dmitry Mendeleev',)

# second, you can create a tuple _without_ using parentheses

cave = "Cave Johnson", 70, "cave@aperturescience.com", "Aperture Science Salt Mine, MI"
print(type(cave)) # <class 'tuple'>
print(cave) # ('Cave Johnson', 70, 'cave@aperturescience.com', 'Aperture Science Salt Mine, MI')


# other stuff, not shown, but I promise you works
# - you can create a tuple from variables, not just literals
# - you can pass a tuple to a function
# - you can return a tuple from a function 
#   (actually, we saw that earlier with the card game)
# - you can use _tuple comprehension_ to generate a new tuple 
#   from some iterable, like you can with list comprehension
