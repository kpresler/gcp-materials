# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 11:55:25 2025

@author: Kai
"""

# Task 1: Hawaiian Earrings (circular version)

import turtle
turtle.speed("slow")

def draw_circles(size, depth):
    if depth == 0:
        return
    
    turtle.circle(size)
    draw_circles(1.2*size, depth - 1)
    
draw_circles(50, 10)

turtle.done()



# Task 1.1: Hawaiian Earrings (hexagon version)

import turtle
#turtle.speed("fastest")

def draw_hex(size, depth, scale):
    if depth == 0:
        return 
    
    for _ in range(6):
        turtle.forward(size)
        turtle.right(60)
    
    draw_hex(size * scale, depth - 1, scale)
    

turtle.setheading(150)    
draw_hex(100, 5, .8)

turtle.hideturtle()
turtle.done()



# Task 2 - Variations on a Tree

import turtle
import random


def tree(size, depth, width):
    
    # base case -- maximum depth reached
    if depth == 0:
        return
    
    # maybe if you get low enough in the level, create green branches
    # (leaves) instead?
    
    
    # otherwise, draw the trunk of our tree
    
    
    turtle.width(width)
    
    turtle.forward(size)
    
    # rather than always turning 30 degrees, choose a random angle
    # between 0 and 60 degrees
    angle = random.randint(0, 60)
        
    turtle.left(angle)
    
    # rather than always shrinking the length of the branch
    # by 20%, shrink it by 0 to 50%
    # we also have a thickness of the branch, that is itself shrunken by a random amount
    
    tree((.5 + random.random() * .5) * size, depth - 1, width*(random.random()/4 + .5))
    
    
    # other possibilities -- don't make both branches come out at mirror angles
    turtle.right(angle*2)
      
    tree((.5 + random.random() * .5) * size, depth - 1, width*(random.random()/4 + .5))
    
    
    # return to where we started to finish this tree
    turtle.left(angle)
    turtle.back(size)
    

turtle.setheading(90)    
tree(100, 8, 12)
turtle.done()




# Task 3 - snowflake

import turtle

def drawFlake(length, scale, depth):
    if depth == 0:
        return 
    
    for _ in range(6):
        turtle.forward(length)
        drawFlake(length *scale, scale, depth - 1)
        turtle.backward(length)
        turtle.left(60)

drawFlake(200,.25, 4)

turtle.done()