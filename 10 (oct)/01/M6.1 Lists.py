# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 09:01:23 2025

@author: Kai
"""

# Last class we talked about _strings_.  
# Today, we're going to discuss something closely related to strings -- lists!
# Strap in, we've got a lot to talk about


# Gateway Python Class Roster
student1 = "Joe Smith"
student2 = "Alice Zhang"
student3 = "Rachel Johnson"
student4 = "Anisha Chatterjee"


# Let's print out all of the students in class
print(student1)
print(student2)
print(student3)
print(student4)


# Oops, someone else wants in class now
student5 = "Ion Cristea"


# Now, to print all of the students in class again
print(student1)
print(student2)
print(student3)
print(student4)
print(student5)


# Yuck!
# While we clearly _can_ keep track of multiple pieces of data like this,
# it's obviously not a pleasant experience
# this results in a _tremendous_ amount of code duplication.  any code we write for 
# one item has to be repeated for _every single item_

# worse, this is not a one-time ordeal.  Like we saw with the example above
# any time that our number of elements changes, we have to go update our 
# code _in every single place_ that we were using them.

# Python, and other reasonable programming languages, have a solution 
# to this problem.  _Data Structures_ are objects that store pieces of data
# and allow us to keep track of a _collection_ of (usually related) things
# The simplest data structure provided by most languages is a list-like
# structure.  Lists store sequential collections of elements

# We've seen a bit of the syntax before, but let's remind ourselves
# In Python, we use square brackets [] to initialise a list
# The values that we stick in the list are comma-separated
# Like with strings, the values in a list are indexed, starting at 0

#            idx   0     1     2     3     4     5
funny_numbers = [9973, 2179, 1103, 2503, 3851, 4007]

# Once you've got a list of values, there are many things you can do with it

# loop through all the values:
for num in funny_numbers:
    print(num)

# figure out how many you've got:
how_many_funny_numbers = len(funny_numbers)

# figure out the max/min
smallest_funny_number = min(funny_numbers)
largest_funny_number = max(funny_numbers)

# access a specific element, by index
last_number = funny_numbers[5]

# negative indexing works too, just like strings
# -1 would give the last, as before
second_to_last_number = funny_numbers[-2] 

# Like with strings, we can also take a _slice_ of a list

# grab up to, but not including, idx 2 (so, 0 & 1)
smaller_funny_numbers = funny_numbers[:2]

# note -- there is a bit of nuance here that wasn't seen when working with strings
# with strings, whenever you extract elements, you _always_ get another string
# it doesn't matter if I extract a single character (like my_str[0]) or
# extract multiple characters (like my_str[2:])

# when we extract elements from a list, this is no longer the case
# if you specify a _single index_, as in funny_numbers[2], you get 
# a single element back (whatever was at that index)
# if you specify a slice, as in funny_numbers[:2], you get back a list
# this is the case _even if the slice has a range of 1 (or even 0!)
# for instance

one_funny_number = funny_numbers[:1]

no_funny_numbers = funny_numbers[:0]


# this might seem bonkers.  why do I get a list of one element, instead
# of just getting that element itself?
# it makes more sense, however, when you realise that list indices aren't
# required to be constants -- they can be expressions, including variables
# If you always get a list, then it makes things consistent -- you can write 
# code that works with a list, regardless of how many things are in the list
# here's an example


# here I ask the user to tell me what start and end indices they want
# and then loop through all numbers

start = int (input ("Enter a start index: "))
end = int (input ("Enter an end index: "))

sublist = funny_numbers[start:end]

# if slicing returned a list sometimes, or a single value sometimes
# this would fail -- you can't loop over a scalar element
for num in sublist:
    print(num)
    
lst = list()
for num in range(2000):
    lst.append(num)

# Other things you can do -- just like with strings, the _stride_ when 
# slicing a list defaults to 1, but can be set to something else


# start at the beginning, go to the end, and walk forward two at a time
# note -- a tidier solution to the same thing is shown below, but I
# wanted to be really explicit about what we were doing first
every_other_funny_number = funny_numbers[0:len(funny_numbers):2] 

every_other_funny_number = funny_numbers[::2]


# note -- it's possible to have _lists of lists_
lists_of_cities = [
    ["Baltimore", "Towson", "Rockville", "Ellicott City",
     "Annapolis", "College Park"],

    ["Raleigh", "Chapel Hill", "Wilmington", "Asheville",
     "Elizabeth City", "Durham"],

    ["New York", "Rochester", "Albany", "Syracuse", 
     "Utica", "East Fishkill"]    
    
]

for a_list_of_cities in lists_of_cities:
    for a_city in a_list_of_cities:
        print(a_city)
        # if I felt so inclined, I could loop through the individual
        # characters in each string here, too
    print("***")

# I can access one of these lists out of the larger list
md_cities = lists_of_cities[0]

# or a single element
our_city = lists_of_cities[0][0]

# alright, so, that's a lot of stuff that maybe you mostly expected, 
# based on how strings work
# now, we'll see some new stuff -- lists, unlike strings, are _mutable_
# this means that I can take a list of elements, and I can _modify_ that 
# collection

# first, a quick clarification of what we _can't_ do with strings
# say I've got the following string
hw = "Hello, world"

# then, I realise I missed a ! at the end :(
# If I do this, then it doesn't modify the existing string
# instead, it generates a _new_ string, that is the result
# of concatenating the two together, then assigns it back
# to the same variable that we started with

hw + "!"

x = 20

x + 15

hw += "!"

# recall, that's the same as doing 
hw = hw + "!"


# let's see again how this works
# I'll create two variables that initially point to the same object
hw = "Hello, world"
also_hello = hw

# When I update `hw`, it makes that variable point to a _new_ object
# The other variable still points to the object from before
# So, a change made in one place is not visible elsewhere
hw += "!"

# with lists, by contrast, I can _modify_ a list that I've already got

funny_numbers = [9973, 2179, 1103, 2503, 3851, 4007]
also_funny_numbers = funny_numbers

# here we go -- we have _updated_ our existing list of values, _replacing_
# one of its elements
# because we have _changed_ the existing list, _any reference_ to that list
# sees the changes
funny_numbers[5] = 223
print(also_funny_numbers[5]) # 223

# Lists are our first _mutable_ type in Python
# We'll see others -- sets, dictionaries, our own objects, later on
# But, this takes some wrapping your head around to make sense of


# Now that we've seen some basics -- let's see some other things that 
# we can do with lists

my_list = [1, 2, 3, 4, 5]

# add an element
my_list.append(6)

# prints [1,2,3,4,5,6]
print(my_list)

# don't do this!
# append returns None
# so this stores None in the variable
# very unlikely to be what you want
# my_list = my_list.append(7)
# instead, just do what we did above
# my_list.append(7)


last_element = my_list.pop()
print(last_element) # prints 6
print(my_list) # prints [1,2,3,4,5]


print(my_list.index(5)) # prints 4
print(my_list.index(-3)) # error -- not there


new_numbers = [10, 20, 30]

# just like it's possible to _extract_ a slice of a list
# (that's what we did earlier), it's also possible to 
# replace a slice of a list with a different set of elements
# I am not especially sold on this syntax -- I tend to 
# prefer a loop -- but it does work
my_list[:3] = new_numbers


# You can even replace a slice of a list with
# a slice of a different length than what you started with

# this replaces the slice at elements 0 & 1 (or, [10, 20]) 
# with the new list, [10, 20, 30]
# so, the end result is [10, 20, 30, 30, 4, 5]
# where [10, 20, 30] is new
# the second [30] is from our replace above
# and the 4, 5 are the original numbers
my_list[:2] = new_numbers
print(my_list)


# if we want to add one element to the end, we use append
my_list.append(1000)
print(my_list) # [10, 20, 30, 30, 4, 5, 1000]


# we can add multiple elements at once too, however
my_list.extend([2000, 3000, 4000])
print(my_list) # [10, 20, 30, 30, 4, 5, 1000, 2000, 3000, 4000]

# note the difference between `append` and `extend`
# append takes a single element -- regardless of type -- and adds it to 
# the end of the list, as-is

# extend takes a collection of elements (a list, or a string, or other types
# we haven't learned about yet) and _unpacks_ it into its individual elements
# each individual element is then added to the list, one at a time
# a _very, very_ easy mistake to make while you're learning about
# lists is to use append or extend where you meant to use the other one


# We saw above how to remove the last element from a list
# good news is, we can remove other values, too

# this removes the value at _index 0_
first_element = my_list.pop(0)
print(my_list) # [20, 30, 30, 4, 5, 1000, 2000, 3000, 4000]

# we can also remove a value, by value, rather than 
# by index.  Note that this removes only the _first_
# matching value, and not _all_ matching values
my_list.remove(30)
print(my_list) # [20, 30, 4, 5, 1000, 2000, 3000, 4000]


# a few last things

fruits = ["cherries", "grapes", "oranges", "blueberries"]

print("crabapples" in fruits)  # false

print("crabapples" not in fruits)  # true

tropical_fruits = ["bananas", "mangos"]

# concatenate two lists together
# this generates a new list, like how
# string concatenation generates a new string
# the two original lists are left unmodified
all_fruits = fruits + tropical_fruits

print(all_fruits)


# add a new fruit: crabapples
# who even comes up with a name like crabapples?
# imagine if someone made lobsterbananas. absolutely nutty.

# note -- if we used `extend` here, the code would run
# and do completely the wrong thing.  it would explode crabapples
# into individual characters, and add each one of them, as individual elements
all_fruits.append("crabapples") # all_fruits = ['cherries', 'grapes', 'oranges', 'blueberries', 'bananas', 'mangos', 'crabapples']


# suppose we decide we like normal apples better than crabapples
crab_index = all_fruits.index("crabapples")
all_fruits[crab_index] = "apples" # all_fruits = ['cherries', 'grapes', 'oranges', 'blueberries', 'bananas', 'mangos', 'apples']

# maybe we don't like cherries, and _really_ don't like them
all_fruits.remove("cherries") # all_fruits = ['grapes', 'oranges', 'blueberries', 'bananas', 'mangos', 'apples']


# let's add something in the middle now
all_fruits.insert(3, "grapefruit") # all_fruits = ['grapes', 'oranges', 'blueberries', 'grapefruit', 'bananas', 'mangos', 'apples']

# if we want to look at our fruits alphabetically, we can sort them
all_fruits.sort() # all_fruits = ['apples', 'bananas', 'blueberries', 'grapefruit', 'grapes', 'mangos', 'oranges']
print(all_fruits) 



