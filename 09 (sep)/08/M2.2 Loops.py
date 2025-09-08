# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 20:48:42 2025

@author: Kai
"""


# When cooking, you’re often faced with instructions like “Stir until boiling” 
# or “Bake until a toothpick inserted comes out clean”
# The baking process is clearly something we want to repeat
# But, we don’t know how long it will take until it’s done

# We can, conceptually, use a _while loop_ to solve a problem like this

# The idea of a while loop is that we will:
# Check if some condition is true
# If it's true, go take some action
# Then, check if the condition is still true
# If so, go take the action again
# _repeat over and over_
# Finally, once the condition is false, at that point the loop terminates

# You can see how this is similar to what we saw above with conditionals.
# There, if the condition was true, we would go do a thing
# Same idea, except we keep re-checking the condition (and maybe, re-doing)
# the thing


num = 0
while num <= 10:
    num = int (input ("Enter a number greater than 10: "))

print(f"Your number greater than 10 was: {num}")



num = 0
while num < 10:
    print(f"Haven't reached 10 yet; our value is {num}")
    num += 1

print(f"After the loop, what's my value? {num}")








# we can use while loop for other purposes


from random import randrange

def is_it_done(cooked_time):
    if cooked_time <= 80:
        return False
    return randrange(cooked_time - 80) > 20

bread_is_done = False
cooked_time = 0
while not bread_is_done:
    bread_is_done = is_it_done(cooked_time)
    cooked_time += 5
    
print(f"Total cooking time: {cooked_time}")



# here's a more complicated, but also more fun, example


lower = int(input("Please enter the lower number: "))
upper = int(input("Please enter the upper number: "))
if lower >= upper:
    print("I can't generate a number with no range!")

number = randrange(lower, upper + 1) # to make it inclusive

guessed_correctly = False
number_of_tries = 0

while not guessed_correctly:
    guess = int(input("Enter your guess: "))
    number_of_tries += 1
    if guess == number:
        guessed_correctly = True
        print("Correct!")
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
print(f"It took you {number_of_tries} guesses to get the correct number")



# DANGER Zone
# it's really easy to _misuse_ a while loop and create an _infinite loop_

# the pattern of all of our examples above was:

# <some initialisation; often creating a loop variable>
# while <some condition>:
#    <do something>
#    <update the condition>

# if you forget that "update the condition" step your loop will _never terminate_
# (and then you'll need to call in Arnold Schwarzenegger)





# this is obviously bad -- you have a loop where its condition will _always_
# be True, and thus will never end

while True:
    print("Still in the loop....")



    
# however, you can get the same problem in a more subtle way

i = 0
while i < 10:
    print(f"i is {i}")
    i += 1
    # forgot to update `i` :(

apple_types = ["Granny Smith", "Gala", "Red Delicious", "Crab"]

idx = 0
while idx < range(len(apple_types)):
    if idx % 2 == 0:
        apple_types[idx] = apple_types[idx].upper()
    else:
        apple_types[idx] = apple_types[idx].lower()
    
    # here, we have a more complicated loop body, so it's easier to miss that we forgot to update
    # the loop variable
    




# We've got _another_ type of loop that is a better fit when we want to run through
# a collection of elements, or want to run through things a determinate
# number of times

# let's look at the _for_ loop


# Suppose it’s the end of the semester, and you’re moving out of your dorm
# Among the things you need to pack up is a shelf of books
# Your process for doing so might looks something like
#    Start at the left side of the shelf
#    For each book on the shelf, take it off of the shelf, and put it in a cardboard box
#    Keep going until we reach the right side of the shelf

# that's pretty much exactly what a `for` loop does (at least in its simplest form)
# start at the left end of a collection
# work our way right, and for each element _do a thing_ with it

all_fruits = ["cherries", "grapes", "oranges", "blueberries", "bananas", "mangos", "apples"]


# for each fruit we've got, print it out
for fruit in all_fruits:
    print(fruit)
    
idx = 0
while idx < len(all_fruits):
    print(all_fruits[idx])
    idx += 1


# we can also loop over a list literal
# we'll learn (lots) more about lists next week
for number in [-6, 24.5, 3.1, 16/7, 400]:
    print(number)
    
# this doesn't do what you (probably) think it ought to
# it doesn't loop through things word-by-word
# but instead character-by-character
# still useful, though.  we'll learn about word-by-word when we
# talk more about lists next week
for letter in "Baltimore, Maryland":
    print(letter)
    

# if you want to repeat something a definite number of times
# a for loop is generally an easier solution than a while loop
# (also, safter -- you can't get an infinite loop with a for loop,
# at least in Python.  In Java or C++, you easily can)

for number in range(10):
    print ("I will not throw paper airplanes in class")



# we can also use `range` when we want to _do_ something with each of the numbers

print("The numbers from 0 to 10 are...")
for number in range(10):
    print(number)
    
# was that what you expected?  perhaps not.  range(10) starts at 0, inclusive
# and goes up to 10, exclusive
# so we get 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


# as it turns out, Python has _overloaded_ the range function -- there are multiple
# different versions, and we can control a bit more about what happens


# rather than starting the count at 0, here we start it at 5
# so this will print 5, 6, 7, 8 9
for number in range(5, 10):
    print(number)
    

# in addition to not (always) starting at 0, we don't (have to) count up by 1
# each time

for number in range (0, 10, 2):
    print(number)
    
# the third argument is the increment amount, which here we set to 2.
# so this'll give us 0, 2, 4, 6, 8
# note that we _don't_ get 10.  again, the end value is exclusive, so this
# stops before hitting 10


# sometimes, you need not one, but two, loops to effectively solve a problem
# this will become more obvious when we talk about lists next week, because
# if you have complicated collections of data, you may need to loop over it
# in similarly complex ways

# for now, we'll see a somewhat contrived example

import string


# this outputs all possible combinations of one letter followed by one number
for letter in string.ascii_lowercase:
    for number in range(10):
        print(letter, number)
        
