# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 10:09:39 2025

@author: Kai
"""



# when writing programs, it's useful to think about both the "happy path"
# and the "unhappy path" through your program.  

# What does this mean?

# The "happy path" represents what your program is _supposed_ to do.  That is,
# assuming we get all good input (from the user, from a file, from a remote 
# computer, etc), this path does what your program is _supposed_ to accomplish
# So far, nearly everything we've been doing is handling "happy path" scenarios

# In addition, however, we've got the "unhappy path".  The unhappy path focuses
# on what _might go wrong_.  This generally does _not_ mean "What bugs might
# I have introduced that I'm unaware of?" but instead thinking about bad 
# scenarios in terms of data or commands your program has to react to.
# What happens if you're supposed to load data from a remote computer, but
# you're somewhere with no internet access?  Or what happens if the user is
# supposed to enter in a number, but gives you a string?  Or what happens if
# your CSV file is supposed to have a certain format, but you get a junk file?

# These are all _unhappy path_ scenarios, and you absolutely need to be 
# thinking about how to handle them in addition to the "happy path" scenarios
# _Do not_ count on everything going right all fo the time, because you can 
# be damn certain that eventually, not everything will go right.  And rather 
# than your program doing something nonsensical, it's better for it to 
# error out (preemptively crash with an error message, rather than doing 
# something that will cause problems down the road).  Additionally, you want
# to give a user-friendly error, rather than just dumping out a database
# exception (such as https://security.stackexchange.com/q/60642)


# We're familiar already how Python will error-check certain scenarios, and 
# _raise an exception_ if an expected condition is violated

# NameError -- trying to use a variable that doesn't exist
capitalised_name = my_name.upper()

# ZeroDivisionError -- can't divide by zero
start_amt = 173
one_tenth_of = start_amt / 0

# IndexError -- index is out of range
my_favourite_fruits = ["Apple", "Banana", "Cherry", "Grape", "Orange"]
my_favourite_fruits[ 10 ] = "Lemon"

# ...and so on, and so forth



# So, what do we do about scenarios like these?
# In some case, nothing.  If you try to use a variable that doesn't exist,
# this is pretty much always an unrecoverable error.  Expecting a program
# to find bugs _in itself_ and do something about them is a tall ask
# However, when you're dealing with user input, network communications, etc
# It is reasonable to _gracefully handle_ those errors

# We do so by using try & except

# Try says, "attempt something that might fail" (sorry, Yoda)

print(my_favourite_fruits)

try:
    idx = int (input ("Which index do you want to change? "))
    new_fruit = input ("What's your new favourite fruit? ")

    my_favourite_fruits[idx] = new_fruit

# then, if something goes wrong (anywhere in the block of code in the try block)
# Python will automagically jump to the except block, and run whatever is there
except:
    print("Bad index (not a number, or out of range?)")

print(my_favourite_fruits)


# it's often reasonable that a block of code might generate _multiple_
# types of errors (there can be different things that go wrong)

# for example, with some slightly abstracted code:

remote_host = getHostname()
username = getUsername()
pw = getPassword()

try:
    conn = connect(remote_host, username_password)

except NoNetworkError:
    print("Your computer appears to not be connected to the network.  Recheck\
          your connection and then try again")    

except ConnectionRefusedError:
    print("The host refused your connection")
    
except TimeOutError:
    print("The network appears to be connected, but the host did not respond\
          in the time allocated")

except CredentialsError:
    print("Username or password was incorrect.  Make sure you typed it correctly")
    
except:
    print("Unknown error occurred; please try again later...")
    
# consider the example above.  While all of these errors have the same end
# result (You couldn't connect to the computer requested), the cause is different
# and what the user might do to resolve the error is different
# Thus, handling different types of exceptions with different code makes a lot of sense

# as for, mechanically, how this works -- Python will attempt to execute the
# code in the `try` block, as before
# if something goes wrong, Python will try to match the _exception type_
# against the various types listed in the `except` blocks.
# the code in the _first matching block_ will get evaluated, and all other blocks
# are skipped.  Consequentially, **make sure you have more general exception
# types later on in the list**.  This is exemplified by putting
# the more general "except" block at the end


# there are a few other promising things we can do with exceptions, too
# just like Python will automatically _raise_ exceptions when you do certain
# illegal thing (divide by zero, etc), you can manually raise exceptions
# This is Very Useful when you want to validate user input, and reject something
# that's nonsensical

# we actually saw a taste of that previously, when we did some OOP

# excerpt from the Student class
def addMajor(self, new_major):
    if len(self.major) >= 3: 
        # return None
        raise ValueError("A student can have at most three majors")
    
    if new_major in self.major: 
        raise ValueError(f"{self.name} {self.surname} is already studying {new_major}")
    
    # finally, add the new major
    self.major.append(new_major)

# there's nothing in Python that says you can't have more than three majors, or that
# you can't major in the same thing twice.  But, for our purposes, for our student
# management system....it doesn't make sesne.  So, we have our own validation 
# here to enforce what rules are reasonable _for the problem we are trying
# to solve_.

# let's see an example of using this in some new code

credentials = {
    "bob": "password123",
    "alice": "dragon",
    "nguyen": "administrator",
    "xliang": "root",
    "juan": "abrahamlincoln"
}

username = "xliang"
password = "NotMyPassword"

if username in credentials and credentials[username] == password:
    print(f"You are now logged in as {username}")
    
else: raise ValueError("Invalid username or password")

# This is useful because we can _very clearly_ reject invalid
# information, helping prevent security problems.  In older languages 
# (C being a prime example) without exception support,
# you instead have to juggle complex conditional logic, special 
# return values, and there's more opportunity for things to go wrong

# one final thing -- defining our _own_ exception classes

# in an example above, I used a bunch of different types of 
# exceptions to signify different types of things that had gone wrong
# as we can see from the syntax highlighting, ConnectionRefusedError
# does actually exist in Python already, but the others aren't there

NoNetworkError, ConnectionRefusedError, TimeOutError, ...

# If I wanted to be able to catch my "Invalid username/password" as a specific
# type of exception (which would help with all of the except blocks we used above)
# I can define my own exception class to represent it

class PasswordError(Exception):
    
    def __init__(self, value):
        self.value = value
        
class NoNetworkError(Exception):
    
    def __init__(self, value):
        self.value = value

import random

username = "bob"
password = "pasword123"

def login():
    # simulating a network connection error with one-in-three odds
    if random.randint(0, 3) == 0:
        raise NoNetworkError("Network connection appears to be down")
    
    if username in credentials and credentials[username] == password:
        print(f"You are now logged in as {username}")
        
    else: 
        raise PasswordError("Invalid username or password")

try:
    
    login()
    
except PasswordError as pe:
    print("Password error detected with the following message: ")
    print(pe)
except NoNetworkError as nne:
    print("Network connection error detected with the following message: ")
    print(nne)


