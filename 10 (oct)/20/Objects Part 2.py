# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 11:44:26 2025

@author: Kai
"""

# Topics
# - Class Interfaces / information hiding
# - Special methods (seen a bit of this with __str__, show others)
# - Operator Overloading


# A key part of (good) object-oriented development is maintaining a separation
# between the interface/abstraction of a class and the implementation of it
# the abstraction focuses on "What does this thing _do_?" and will 
# reveal as little as possible about "_How_ does this thing do it?"

# This is not _required_ -- you can have a class "leak" implementation details
# to the outside world, but this is (usually) a Bad Idea.  Why is that?
# - Almost everything is easier to use if you can focus on _what_ it does
#  instead of worrying about _how_ it does it.  As an example of this, 
#  both a for-in loop and a while loop ultimately convert to (basically) 
#  the same underlying instructions when it's time for the computer to evaluate
#  them.  In fact, neither are run as written -- they're both turned into 
#  if statements and goto statements.  is it possible to write code that just 
#  uses ifs/gotos instead of loops?  absolutely, and if you program in assembly,
#  you get (have) to do that -- but it's far less pleasant than 
#  using a higher-level abstraction.  Likewise, if I can look at a class and see
#  what operations a class supports, then I know how I can _use_ it and 
#  don't have to worry about the (more complicated, lower-level) details of
#  how it's doing it.

# - Secondly, if you focus on _what_ something will do, then it's possible
#  to change the underlying implementation at any point.  This means that
#  it's possible to _refactor_ code in beneficial ways -- changing the algorithm
#  to a more performant one, or using data structures that are faster.  It's
#  even possible for the code to be _completely rewritten_ in a way that is
#  invisible to the user (because the interface is still the same), but
#  makes it easier on the developer to maintain, etc.  If you are working
#  directly with the implementation rather than the interface, then this can
#  cause more "breaking changes"

# Java, C++, etc support this using something called _access modifiers_.  A 
# method (or field) in a Java class that is declared "public" can be accessed
# from anywhere.  A method that is declared "private" cannot be accessed 
# outside of the class where it is declared.  Part of good development
# is figuring out, "What _exactly_ needs to be exposed to the outside world,
# and what are implementation details I should hide?"

# Python doesn't support making things public or private.  Instead, Python
# uses naming conventions -- a field (or method) that you want to be private
# starts with an underscore.  This does not _actually_ make it private --
# anyone _can_ still access it, from anywhere, but it is used to signify
# "This is not intended to be part of the public interface.  Use of it is
# at your own risk"


# we had a question in class about having a list with a bounded capacity, rather
# than one that grows automatically, forever
# here, we create a BoundedList which represents that.  the capacity can be set
# when created, and the list will never get bigger than that
class BoundedList:
    
    def __init__(self, capacity):
        
        # Here, we choose to make both of the fields in the class _private_
        # We do so to stop someone who's using the list from accidentally 
        # mucking around inside it and doing something stupid
        # If they went messing around inside it, they could readily
        # change the capacity, or, worse, by doing something with the internal
        # list representation, could use the list in a way that totally ignores
        # the capacity we try to enforce.
        self._capacity = capacity
        self._lst = list()
        
    def get(self, idx):
        if idx >= self._capacity or idx >= len(self._lst): 
            raise IndexError("Index out of bounds")
        
        return self._lst[idx]
    
    def set(self, idx, value):
        if idx >= self._capacity or idx >= len(self._lst): 
            raise IndexError("Index out of bounds")
        
        self._lst[idx] = value
        
    def add(self, value):
        if len(self._lst) == self._capacity: raise ValueError("List is full")
        
        self._lst.append(value)
    
    def get_capacity(self):
        return self._capacity
    
    # other methods, if we wanted to implement them, could go here
    

my_list = BoundedList(5)

for i in range(6):
    # last iteration, this will blow up
    my_list.add(i)
    
# can't access it like this -- doesn't exist w. this name
inner_list = my_list.lst

# this _does_ work
# we still have access to the inner details, even though we maybe don't want to
inner_list = my_list._lst

# Python also has "name mangling" which makes it harder to access fields
# but this is used more in the context of inheritance than with
# making things private.  What is done above is convention, and relies on 
# your users demonstrating good sense




# Recall the __init__ and __str__ methods from before
# __init__ is the name of the "initialiser" (also called "constructor") which is
# used to instantiate new object instances.  __str__ is the toString method
# which is used to get a readable string representation from an object
# these leading and trailing underscores are used to create "special methods"
# -- these are methods that are not ever called directly by name, but instead
# are called automatically by Python at the right time.

# for example, when you print anything, Python first converts it to a string

print (3)

# is equivalent to 

print( str( 3 ) )

# If we print one of _our_ objects, Python converts it to a string by passing
# it to `str()`.  `str()`, in turn, calls the __str__ method automatically

# there are other "special" methods that we can define in addition to these two
# __repr__ is used to provide a "debugging representation" of your object, ideally
# with enough information to recreate it as-is.  More relevantly, if you have
# a collection of your objects, __repr__ is called on each object to convert it to 
# a string before printing it out, _instead_ of calling __str__


# there are a bunch of other fun methods to, beyond that
# recall how you can use + not just on numbers, where you'd probably expect
# it, but also on strings, or lists, where maybe you _wouldn't_ expect it
# this comes from _overloading_ the operator for our types, so that it, too
# understands what it means to add, or multiply, or whatnot


class Point2D:
    """Represents a point in 2D space, such as on a Cartesian plane"""
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Point2D({self.x}, {self.y})"
    
    
    
the_origin = Point2D(0, 0)
print(the_origin)

other_point = Point2D(3, 4)
print(other_point)


third_point = Point2D(5, 7)
print(third_point)


# it might make sense to _add_ two points, to get a new point
# that has the sum of each of their coordinates
# that is, (3, 4) + (5, 7) => (8, 11)


# TypeError: unsupported operand type(s) for +: 'Point2D' and 'Point2D'
# well, nice idea, but doesn't get us very far
res_point = other_point + third_point



class Point2D:
    """Represents a point in 2D space, such as on a Cartesian plane"""
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Point2D({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)


    def __mul__(self, value):
        return Point2D(self.x * value, self.y * value)

"""

the_origin + other_point

=> the_origin.__add__(other_point)

the_origin * 10
=> the_origin.__mul__(10)
"""


other_point = Point2D(3, 4)
print(other_point)


third_point = Point2D(5, 7)
print(third_point)



res_point = other_point + third_point

print(res_point)


scaled_point = other_point * 4
print(scaled_point)



# Operator overloading is a really fun feature.  IMO, C++ supports it better
# because it allows you to be more careful with _how_ you overload an operator

# in our code above, the __add__ method will get called any time we 
# have an expression where we add _something_ to a Point2D

# even if it doesn't make sense
what = other_point + "Hello, World!"

# this will blow up in the _add__ method when it tries to access the attribute
# `x` out of an object that doesn't contain it.  But C++ will stop things, 
# and refuse to even let you use the + operator if the right-hand operand
# has the wrong type.  ultimately this mostly boils down to compiled languages
# vs interpreted languages

