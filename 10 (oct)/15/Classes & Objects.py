# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 10:49:45 2025

@author: Kai Presler-Marshall
"""


# In Python, every single piece of data that you work with is an object
# Numbers are objects (either of type `int` or `float`)
# Strings are objects (of type `str`)
# Dictionaries are objects (of type `dict`)
# Imports are object (of type `module`)
# All semester, we’ve been calling methods on these objects
# Methods allow us to do things with these objects
#   Add elements to a list
#   Capitalise a string (or, at least get a new, capitalised version)
# Today, we’re going to learn how to define our own object types





# First off, before we get into the syntax, let's take a minute to think
# about the _object-oriented programming_ paradigm

# But, before we get to _that_ -- what are programming paradigms?
# there are many high-level ways of approaching problem-solving
# some languages are single-paradigm (or at least, support some paradigms
# better than others); others are multiple-paradigm and you
# can incorporate multiple strategies as works best for what you're doing

# Procedural programming works by creating procedures (functions)
# to solve problems, and having functions call each other so that
# solutions to large problems are composed out of solutions to 
# parts of the problem

# Functional programming works by applying a series of functional 
# transformations to data -- feed your data through one function, 
# then through another function, etc.  This also involves passing
# functions as arguments to other functions, which may transform
# the function itself

# Object-oriented programming (that's today!) invovles taking a problem
# and breaking it down into a set of _objects_, thinking about
# what each object type should _do_ and the relationships that it has 
# with other objects in your system.  essentially, complex objects
# (either abstractions of physical objects, or abstractions of purely
# conceptual objects) are decomposed into simpler objects that interact
# in meaningful ways


# We’ve seen so far that all objects have methods that you can call on them
#   "abc".upper()
#   [1,2,3].append(4)
# Different objects have different methods (supported behaviour)
# This is why we can call .upper() on strings, but not on lists, or on ints
# This behaviour comes from the object's _type_, represented by its _class_

# All strings support exactly the same behaviour (that is, we can call 
# the same methods on them) because all strings are instances of the `str` class

# A class serves as a blueprint that defines what data an object will 
# store, and what we can do with it (that is, which methods we can call on it)
# The classes are then instantiated into new objects, which store data, 
# and provide methods that let you do something with this data


# Now, let's see some syntax


# The class keyword is used to define a new class (surprising, right?)
# Then, we've got the name of the class.  This should be descriptive 

class Student:
    
    """Class contents go here"""


    # this defines a _method_ in the class
    # note the odd name -- __init__ is the _initialiser_
    # (more commonly called the _constructor_) of the class

    # when you create a new object instance, the constructor gets called 
    # automatically
    
    # a few other things to note, while we're at it
    # `self` must be the first parameter of every _method_ you define
    # (recall -- a method is a function, but one defined inside a class)
    # `self` represents _the current object instance_ that we're working with
    # (for the constructor, that's the instance being constructed)
    # after that, you can have any other parameters you want
    def __init__(self, name, surname, graduation_year, major):
        
        # these expressions set _attributes_ (also called _fields_)
        # within the newly-created object
        # Other methods can access these fields, or update them
        self.name = name
        self.surname = surname
        self.graduation_year = graduation_year
        self.major = [major] if major else list()
        

# Instantiating an object is done by _calling_ the class as if it was a function
# This will automatically call the constructor you've defined
# Note, we pass in arguments here that correspond to all of the parameters
# above, _except_ for `self`.  You _never_ pass an argument for `self` --
# Python will fill that in automagically

joe = Student("Joeseph", "Smith", 2026, "Computer Science")

jane = Student("Jane", "Doe", 2025, "Math")


# joe's first name
print(joe.name)

# joe's surname
print(joe.surname)


# print out the whole object
# hmm, that didn't look good
print(joe)

# for an object to print nicely, you've got to define a `__str__` method
# I call this the `toString` method, which is the name Java gives it, and is
# easier to say, but the name _must_ be __str__

class Student:
    
    """Class contents go here"""

    def __init__(self, name, surname, graduation_year, major):
        self.name = name
        self.surname = surname
        self.graduation_year = graduation_year
        self.major = [major] if major else list()
        

    # toString method always has only one parameter -- the object being string-ified
    def __str__(self):
        maj_str = " and ".join(self.major) if len(self.major) != 0 else "Nothing"
        return f"{self.name} {self.surname} is graduating in {self.graduation_year} and studying {maj_str}"
    
    
    
jane = Student("Jane", "Doe", 2025, "Math")
print(jane) # much better :)

# An object that can only be created, and printed, isn't very interesting
# Our objects become more useful when we have _other_ methods present
# Ones that lets us do interesting things with the data there


class Student:
    
    """Class contents go here"""

    def __init__(self, name, surname, graduation_year, major):
        self.name = name
        self.surname = surname
        self.graduation_year = graduation_year
        self.major = [major] if major else list()
        

    # toString method always has only one parameter -- the object being string-ified
    def __str__(self):
        maj_str = " and ".join(self.major) if len(self.major) != 0 else "Nothing"
        return f"{self.name} {self.surname} is graduating in {self.graduation_year} and studying {maj_str}"
    
    
    
    
    def addMajor(self, new_major):
        if len(self.major) >= 3: raise ValueError("A student can have at most three majors")
        
        if new_major in self.major: raise ValueError(f"{self.name} {self.surname} is already studying {new_major}!")
        
        # finally, add the new major
        self.major.append(new_major)
    
jane = Student("Jane", "Doe", 2025, "Math")

jane.addMajor("Computer Science")

jane.addMajor("International Relations")

print(jane)

# Generally when you define a type it's because you want to have _multiple_ objects
# of that type.  So, we can go stamp out multiple Students representing different students

# Bob doesn't have a major yet, but has other information
bob = Student("Robert", "Smith", 2028, None)

alex = Student("Alexandra", "Richardson", 2026, "Physics")

mike = Student("Mikhail", "Rurikovich", 2027, "Russian Literature")
mike.addMajor("Genetics")

roster = [jane, bob, alex, mike]

for student in roster:
    print(student)
    
