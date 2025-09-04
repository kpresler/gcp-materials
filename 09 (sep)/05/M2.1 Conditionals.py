# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 13:00:44 2025

@author: Kai Presler-Marshall
"""



# writing programs that do the same thing every time they're run is _really boring_
# if we want to solve any problem of substance, we need to have our program _react_
# to conditions, data, input, etc.


# enter, conditionals!

x = 87
if x > 10:
    print("X is greater than 10")
    

# in the example above, nothing got printed, because the condition wasn't satisfied
# (is -87 greater than 10?  no, clearly not)


# we can write all sorts of conditionals


animal_name = "cat"

animal_name = "elephant"

if len(animal_name) > 7:
    print("That's a pretty long animal name.  Maybe you should shorten it?")


lst = [1,2,3,4,5]

if 5 in lst:
    print("Look, I found it!")


# sometimes we want to take one action if a condition is true, and another
# action if the condition was false



first_num = 20
second_num = 35

# first_num = 70

if first_num > second_num:
    # all expressions "inside" an if statement are
    # indented
    print("The first number was larger")
    
else:
    print("The second number was larger")
    print("It's possible to have _multiple_", end ="")
    print(" expressions inside a single block")
    print("All of them are part of the block, and evaluated as such")
    

# note that if you have an if-else like above, the body of _only one_
# of the blocks will get executed.  a condition is always either true, or it
# isn't.  there's nothing that is true-or-false (unless we're talking about
# irradiated cats, but let's not)


# sometimes you want to take an action if a condition is true, another action if
# that condition was false, and then, _regardless_, follow it up with a different action

first_num = 100

if first_num > second_num:
    print("This statement will get executed only if first > second")
else:
    print("This statement gets executed when second >= first")
    
    
print("This statement is after the if/else block -- so it always gets run -- just like all other statements we've written before today")


first_num = 35

# some problems call for chaining together _multiple_ conditions to evaluate
# a more complex set of tests

if first_num > second_num:
    print(f"The first number, {first_num}, was the larger one")

if second_num > first_num:
    print(f"The second number, {second_num}, was the larger one")
    
if first_num == second_num:
    print("Both numbers were equal ¯\_(ツ)_/¯")
    
    
# as it turns out, we can take that code from above and _rewrite it_ to be a bit tidier
# this gets back to the discussion above.  except for irradiated cats, if we've got
# three mutually exclusive options, only one of them can be true
# this code "does the same thing" as the code above, but it helps make it
# clearer to other developers (including possibly me, in the future) what
# it's trying to do

# as a bonus, this sort of branching is a _tiny_ bit faster for the computer to run



if first_num > second_num:
    print(f"The first number, {first_num}, was the larger one")

elif second_num > first_num:
    print(f"The second number, {second_num}, was the larger one")
    
else:
    print("Both numbers were equal ¯\_(ツ)_/¯")
    
    



# note -- sometimes you don't just *prefer* to use mutually exclusive behaviour,
# but you actually _need_ it for things to work properly


temp = 103

if temp > 100:
    print("It is extremely hot!")
elif temp > 90:
    print("It is quite hot")
elif temp > 80:
    print("It is a bit hot, but not too hot")
elif temp > 70:
    print("It's a lovely warm day")
elif temp > 60:
    print("It's a lovely cool day")
elif temp > 50:
    print("It's maybe a bit cool today")
elif temp < 50:
    print("Starting to get a bit chilly")
elif temp < 20:
    print("Today is very cold")

print("Here I am at the bottom")

# oops, that almost certainly didn't do what we wanted :(
# let's fix it!


# some problems call for creating _compound_ conditions.  that is, 
# I only want to take an action if two different things are true, at the same time
# for instance, if it's 103 degrees, that's probably a good day for swimming
# however, if there's also a tornado, my desire for swimming disappears 
# even faster than all of the nearby buildings



# expr1 and expr2 evaluates to True only if both expr1 and expr2 are True

expr4 = False and True # False
expr5 = False and False # False
expr6 = True and False # False
expr7 = True and True # True, finally!


# expr1 or expr2 evaluates to True if either (or both) of expr1/2 are true

expr4 = True or True # True
expr5 = False or True # True
expr6 = True or False # True
expr7 = False or False # False




# now, let's get back to our problem for a moment ago
# I want to know when I should go swimming, but make sure I won't be 
# vacuumed up by a tornado

temp = 100
bonus_weather = "tornado"

if temp > 90 and bonus_weather == "sunny":
    print("Good weather for swimming")

else:
    print("Not so good weather for swimming")




# another example, seeing how to use `or`


temp = -60
bonus_weather = "cloudy"


if temp < -20 or bonus_weather == "tornado":
    print("This is dangerous weather, you should stay home")

else:
    print("Not too dangeorus, at least")
    
    
    
# when doing arithmetic, you can keep gluing things together to your heart's content
# for instance, this is fine

res = 3 + 5 + 17 + 6 + 19 + 40 + 76 # 166

# same with boolean expressions, too

temp = 85
bonus_weather = "hurricane"

if temp < -20 or bonus_weather == "tornado" or bonus_weather == "hail" or bonus_weather == "hurricane":
    print("This is dangerous weather, you should stay home")

else:
    print("Not too dangeorus, at least")




