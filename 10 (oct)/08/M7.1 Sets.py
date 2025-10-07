# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 10:54:14 2025

@author: Kai
"""

# Previously, we learned all about Lists
# Lists are possibly Python's most widely-used data structure, 
# and are great when you wish to store a linear sequence of 
# (usually) homogenous elements
# We also learned about tuples


# Now, we'll learn about a few other common data structures:
# - sets: these behave like the mathematical notion of a set (don't worry, 
#  we'll recap that if you don't remember what it is)
# - dictionaries: these associate _keys_ with _values_


# first, let's briefly remind ourselves about lists

my_favourite_fruits = ["bananas", "apples", "cherries", "oranges", "apples", "tomatoes"]

most_favourite_fruit = my_favourite_fruits[0]
least_favourite_fruit = my_favourite_fruits[5]
top_two_fruits = my_favourite_fruits[:2]

# tomatoes are not very good in a fruit salad, so let's get rid of them
my_favourite_fruits.pop(5)

# now, onto sets

# first order of business -- sets are constructed using {curly braces}
# just like there's the `list()` function, there's also a `set()` function
# however, and this is important -- if you want to create an empty set
# you _must_ use the set() function
# an empty pair of curly braces creates an empty _dictionary_ instead.  
# Blame Guido for this one

letter_grades = {"A", "B", "C", "D", "F"}
empty_set = set()

# next -- while you can put _anything you want_ into a list, 
# sets have some restrictions.  You can only put _hashable_ elements
# into a set (which for now basically means _immutable_)
# if/when you take Data Structures you'll learn more about
# the implementation & see why this is the case

illegal_set = {list(), list(), list()}

legal_set = {"cat", "dog", "møøsë"}


# sets, as a mathematical construct store _unique_ elements.  Trying
# to add a duplicate element to a set does nothing (no error, it just)
# doesn't modify the set

# sets are an _unordered_ collection of elements.  In a list, the question
# "What is at index 0?" or "What are the last two elements?" makes sense.
# In a set, these questions don't make sense.  You think of elements
# either being in a set, or not being there, but you don't think about
# _where_ they are

# you can add and remove elements from a set

magnificent_musicians = {"Beethoven", "Tchaikovsky", "Dvorak", "Schubert", "Rimsky-Korsakov"}

# note we use _add_ rather than _append_.  Since sets don't have an idea
# of an index, "add" makes more sense than "add at end"
magnificent_musicians.add("Bach")

print(magnificent_musicians) # {"Beethoven", "Bach", "Tchaikovsky", "Rimsky-Korsakov", "Schubert", "Dvorak" }


magnificent_musicians.remove("Schubert")
print(magnificent_musicians) # {"Beethoven", "Bach", "Tchaikovsky", "Rimsky-Korsakov",  "Dvorak" }

# you might be wondering at this point, "What is the point?"  Sets seem to do
# less than lists, so why would we want them?

# The beauty in sets is that they support a lot more from the mathematical 
# notion of sets

famous_russians = {"Tchaikovsky", "Mendeleev", "Peter the Great", "Rimsky-Korsakov"}
german_musicians = {"Bach", "Beethoven"}

# (1) "What are all of the elements present in _either_ (or both) sets?"  That's a _union_
musicians_or_russians = magnificent_musicians | famous_russians

# (2) "What are all of the elements present in _both_ sets?"  That's an _intersection_
russian_musicians = magnificent_musicians & famous_russians

# (3) "What are all of the elements present in one set, but not another?" That's a difference
non_russian_musicians = magnificent_musicians - famous_russians
russian_non_musicians = famous_russians - magnificent_musicians

# (4) "Are all of the elements from this set present in another set?"
are_all_musicians_russian = magnificent_musicians <= famous_russians # False
are_all_russians_musicians = famous_russians <= magnificent_musicians # False
are_all_german_musicians_magnificent = german_musicians <= magnificent_musicians # True

# (5) "Does this set contain at least the elements present in another set?"
do_all_musicians_include_germans = magnificent_musicians >= german_musicians # True

# note, there are also strict-subset and strict-superset versions of the latter operations (<= becomes <, and >= becomes >).  I don't find these quite as useful

