# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 10:52:42 2025

@author: Kai
"""


# Recursion!

# Recursion gives us a powerful technique for solving problems, and does
# so in a way that we've not seen before.  Recursion involves
# defining a problem _in terms of itself_

# what this means is that to solve big, complicated, problems, we define
# the solution in terms of one or more smaller versions _of the same problem_

# unfortunately, recursion tends to get a pretty bad reputation in Intro CS
# courses.  Recursion involves thinking about problems in a way that many
# students find to be deeply unnatural, and is often used to solve problems
# that are solved easily using loops.  So, it often feels like you're being
# told to tie one hand behind your back and then solve an easy problem,
# but in a more complicated way

# Why, then, do we bother to learn a technique that seems useless?  Well,
# when you get to more advanced classes, there are many data structures
# that are inherently recursive, and thus recursive algorithms are by far
# the tidier solution

# I'm going to show you a couple of these "tie your hand behind your back"
# algorithms first so that we can see the _structure_ of a recursive solution,
# and then we'll see some problems where recursion is genuinely the 
# best approach


# Let's use recursion to calculate factorials
# It's easy enough to recursively define the factorial function -- I don't
# need to "know" the answer to n! -- it's simple enough to express the operation
# in terms of itself, saying that n! == n * (n-1)!
# We also need to figure out a base case -- what is a version of the problem
# that is simple enough to solve _without_ using more complicated techniques?



def factorial(n):
    
    # 0!, and 1!, are both 1
    if n < 2:
        return 1
    
    else:
        # otherwise, we have a recursively-defined answer.  5! = 5 * 4!
        # so, we make the recursive call to figure out the part of the 
        # answer that we don't yet have, and then build our overall solution
        return n * factorial(n-1)
    
print("5!")
print(factorial(5))

print("3!")
print(factorial(3))




# let's calculate Fibonacci numbers
# This is a place where recurion is a decent solution -- while we can readily
# solve the problem _just_ using loops, Fibonacci numbers are at least a 
# recursively-defined sequence, so this is just "not any better" than a loop
# instead of drastically worse

def fib(n):
    
    # all recursive algorithms must include a _base case_
    # this is a version of the problem that is "simple enough" to solve as-is
    # and where we odn't need to make any further recursive calls to solve it
    # If you _don't_ have a base case, the recursion continues "forever"
    # (or, at least, until your program crashes)
    
    # the first two Fibonacci numbers are 1, so we define that as our base case
    if n == 0 or n == 1:
        return 1
    
    
    # next, we have the _recursive case_.  This is a version of the problem 
    # that is complicated, so we make one or more recursive calls on a smaller
    # version of the problem, and then reassemble their answers into a cohesive
    # solution to the original problem
    
    # all other Fibonacci numbers are the sum of the proceeding two
    return fib(n-1) + fib(n-2) 
    

# let's trace out on the board what actually happens, in terms of the recursive
# calls, from something like this

print(fib(4))

# we can call a larger version of the problem, although it rapidly gets
# rather unwieldy to trace out the larger versions

print(fib(10))



# Enough looking at examples where we tie a hand behind our back.  Let's see
# some examples where recursion makes for an _actually good_ solution
# Suppose I want to sort the list [6, 5, 12, 10, 9, 1]
# Python has a built-in function that'll do this, but I want to actually learn 
# how to do it.  We'll talk more next class about sorting, but we'll get a 
# sneak-peak of it now

# One promising algorithm is called merge-sort.  Let's see how to trace through it



def mergesort(nums):
    """recursive mergesort implementation"""
    
    # base case -- a list of 0 or 1 elements is already implicitly sorted
    if len(nums) < 2:
        return nums
    
    
    # otherwise, split the list in half, and merge-sort each half
    med = len(nums)//2
    
    
    # recursive call on the first half
    left = mergesort(nums[:med])
    
    # recursive call on the second half
    right = mergesort(nums[med:])
    
    # reassemble into the overall solution
    return merge(left, right)
    
    
    
def merge(left, right):
    """merges two sorted lists together into a complete, also sorted, list"""
        
    total_to_merge = len(left) + len(right)

    l_idx = 0
    r_idx = 0
    out = list()
      
    
    while len(out) < total_to_merge:
        if r_idx == len(right):
            out.append(left[l_idx])
            l_idx += 1
        elif l_idx == len(left):
            out.append(right[r_idx])
            r_idx += 1
        elif left[l_idx] < right[r_idx]:
            out.append(left[l_idx])
            l_idx += 1
        else:
            out.append(right[r_idx])
            r_idx += 1
    return out
    
    
from random import randrange
nums = [randrange(100) for _ in range(100)]

sorted_nums = mergesort(nums)
sorted_with_python = sorted(nums)

for i in range(len(sorted_nums)):
    if sorted_nums[i] != sorted_with_python[i]:
        raise ValueError(f"error at idx={i}, expected={sorted_with_python[i]}, actual={sorted_nums[i]}")
print("Hey, it worked!")

print(f"original={nums}")
print(f"sorted={sorted_nums}")


# now, let's see a _fun_ application!


import turtle
def tree(size, depth):
    
    # base case -- maximum depth reached
    if depth == 0:
        return 
    
    # otherwise, draw the trunk of our tree
    turtle.forward(size)
    
    # and then two sub-trees
    # note the `depth - 1`
    # this is what controls the recursion and 
    # makes progress towards the base case
    turtle.left(30)
    
    tree(.8 * size, depth - 1)
    
    turtle.right(60)
      
    tree(.8 * size, depth - 1)    
    
    
    # return to where we started to finish this tree
    turtle.left(30)
    turtle.back(size)
    

turtle.setheading(90)    # up
tree(100, 5)
turtle.done()

import turtle
turtle.speed("fastest")

def tri_tree(size, depth):
    if depth == 0:
        return 
    
    
    # as above, but this time, we draw three sub-trees
    turtle.forward(size)
    turtle.left(30)
    
    tri_tree(.8 * size, depth - 1)
    
    # thus, the angle is a bit adjusted
    turtle.right(30)
    tri_tree(.8 * size, depth - 1)
    
    turtle.right(30)
    tri_tree(.8 * size, depth - 1)    
    
    turtle.left(30)
    turtle.back(size)
    
turtle.setheading(90)    
tri_tree(100, 5)
turtle.done()


# a more impressive version than what we've got above; 
# essentially the same approach at a high-level, but it looks better

# disclaimer: I didn't write this one :)

import turtle
import colorsys

def draw_stick(x,y,length,pensize,color,angle):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(angle)
    turtle.pensize(pensize)
    turtle.down()
    turtle.color(color)
    turtle.fd(length)

def draw_tree(x,y,length,pensize,hue,angle,fat_angle,n):
    if n == 0:
        return
    (r,g,b) = colorsys.hsv_to_rgb(hue,1,1)
    draw_stick(x,y,length,pensize,(r,g,b),angle)
    tx = turtle.xcor()
    ty = turtle.ycor()
        
    draw_tree(tx,ty,length*0.7,pensize*0.7,hue-1/13,angle+fat_angle,fat_angle,n-1)
    draw_tree(tx,ty,length*0.7,pensize*0.7,hue-1/13,angle-fat_angle,fat_angle,n-1)
    
turtle.setup(800,800)
turtle.title("Rainbow Coloured Tree")
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.bgcolor('black')

draw_tree(0,-300,200,10,12/13,90,25,12)
turtle.done()


import turtle
turtle.speed("fast")

def draw_sierpinski(length, depth):
    
    # when we reach max depth, stop
    if depth == 0:
        return

    # for the three sides of a triangle
    for i in range(3):
        # draw the sub-triangle
        draw_sierpinski(length / 2, depth -1)
        # draw the side
        turtle.forward(length)
        # rotate
        turtle.left(120)
    
    
draw_sierpinski(500, 5)
turtle.done()


import turtle
from time import sleep

def spiral(start_size, angle, scale_factor, min_size):
    
    # this time, we don't stop after a predefined number of iterations
    # but instead, when the share that we have drawn is "small enough"
    if start_size < min_size:
        return
    
    turtle.forward(start_size)
    turtle.left(angle)
    spiral(start_size * scale_factor, angle, scale_factor, min_size)
    
spiral(200, 90, 0.95, 15)

sleep(5)
turtle.clear()

    
spiral(200, 121, 0.95, 15)
sleep(5)
turtle.clear()
turtle.setheading(0)
spiral(200, 95, .93, 10)
turtle.done()

