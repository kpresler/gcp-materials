# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 15:13:53 2025

@author: Kai
"""


import random
import time
import turtle

max_speed = 500
shapes = []


class Shape:
    """
    defines a Shape class which we'll use for our physics simulator.  this is used to keep track of the information that will be shared across not 
    just all shape instances, but all different _types_ of shapes, such as balls, hexagons, bananas, and so on
    """
    
    def __init__(self, position = None, velocity = None):
        if velocity:
            self.velocity = velocity
        else:
            vx = random.randint(-max_speed , max_speed)
            vy = random.randint(-max_speed , max_speed)
            self.velocity = (vx, vy)

        if position:
            self.position = position
        else:
            self.position = (0, 0)
        
        # notice, no size any more.  we'll see why soon enough :)

    # we might normally choose to create a __str__ method here, or maybe a __repr__ method too

    def move(self, time):
        """ moves this object to the appropriate location, based on its stored location & velocity, and the amount of time that has elapsed since the previous movement """
        (px, py) = self.position


        if abs(px) >= 250: 
            self.velocity = (-self.velocity[0], self.velocity[1])

        if abs(py) >= 250:
            self.velocity = (self.velocity[0], -self.velocity[1])

        (vx, vy) = self.velocity
        # set position to computed position at time
        self.position = (px + (vx * time), py + (vy * time))

    
    def draw(self, turtle):
        """ All objects that we want to draw will need to start by having the turtle go to the location that we want to draw the object at.  Overridden implementations in subclasses will need to define how to handle the actual drawing at the specified location """
        turtle.penup()
        turtle.goto(self.position[0], self.position[1])


class Ball(Shape):
    """
    A ball represents a type of shape that we can draw.  In addition to all of the information tracked by the Shape itself (loc, velocity) a ball also tracks its size.  A ball knows how to draw itself as well.
    """
    
    
    def __init__(self, size = 10, position = None, velocity = None):
        """ 
        the initialiser for a Ball object 
        It starts by calling the initialiser from the superclass (Shape).  This sets all of the information that _any_ shape knows (position & velocity); we then set the information thta a ball tracks separately from a generic shape.
        
        """
        super().__init__(position, velocity)
        self.size = size

    def draw(self, turtle):
        """ draws a ball with the turtle; as a dot of the specified size
        first, we use the behaviour that comes from our superclass.  then, 
        we add our own on top of it"""
        super().draw(turtle)
        turtle.dot(self.size)
        
    # Because a Ball is-a shape, it inherits the `move` method from the Shape class.  Thus, all Ball objects are capable of moving themselves, even though we have not overridden / redeclared the `move` method.
    


class Apple(Shape):
    def draw(self, turtle):
        super().draw(turtle)
        turtle.shape('apple.gif')
        turtle.stamp()
        

# this is bound to a key so we can create new Apples        
def add_apple():
    shapes.append(Apple())

class Bananna(Shape):
    def __init__(self, position=None, velocity=None):
        super().__init__(position, velocity)

        # 1 in 10 chance
        self.escaping_banana = random.randint(0, 10) == 0

    def draw(self, turtle):
        super().draw(turtle)
        turtle.shape('banana.gif')
        turtle.stamp()

    def move(self, time):
        
        # normal bananas get to move like any other object does
        if not self.escaping_banana:
            super().move(time)
        
        # escaping bananas avoid bouncing off the edge of the box, and instead continue moving
        else:
            (px, py) = self.position
            (vx, vy) = self.velocity
            # set position to computed position at time
            self.position = (px + (vx * time), py + (vy * time))
            
def add_banana():
    shapes.append(Bananna())         
       
def add_ball():
    shapes.append(Ball(random.randrange(20) + 1))

# Task 1
class BouncyBall(Ball):
    
    def __init__(self, bounciness = 1, size = 10, position = None, velocity = None):
        super().__init__(size, position, velocity)
        self.bounciness = bounciness
    
    def move(self, time):
        (px, py) = self.position


        if abs(px) >= 250: 
            self.velocity = (-self.velocity[0] * self.bounciness, self.velocity[1])

        if abs(py) >= 250:
            self.velocity = (self.velocity[0], -self.velocity[1] * self.bounciness)

        (vx, vy) = self.velocity
        # set position to computed position at time
        self.position = (px + (vx * time), py + (vy * time))
        

def add_bouncy():
    shapes.append(BouncyBall(random.random()))


# Task 2

class Goat(Shape):
    
    
    def draw(self, turtle):
        super().draw(turtle)
        turtle.shape('goat.gif')
        turtle.stamp()
    
    def move(self, time):
        super().move(time)
        
        goat_x, goat_y = self.position
        
        for other_object in shapes[:]:
            other_x, other_y = other_object.position
            
            if abs(goat_x - other_x) < 10 or abs(goat_y - other_y) < 10:
                # we found something close enough to eat
                
                if not isinstance(other_object, Goat):
                    shapes.remove(other_object)
            
def add_goat():
    shapes.append(Goat())


# keep looping through updating each object as time progresses
def animation_loop(shapes, time_step):
    while True:
        # drawing loop
        turtle.clear()
        for shape in shapes:
            shape.draw(turtle)

        turtle.update()

        # physics loop
        for shape in shapes:
            shape.move(time_step)

        # wait for next frame
        time.sleep(time_step)
            
# main function that starts running the program
def main():
    screen = turtle.Screen()
    screen.addshape('apple.gif')
    screen.addshape("banana.gif")
    screen.addshape("goat.gif")

    turtle.tracer(0, 0) # only render when we say so
    turtle.hideturtle() # hide the icon
    turtle.penup()

    turtle.onkeypress(add_ball, 'space')
    turtle.onkeypress(add_apple, 'a')
    turtle.onkeypress(add_banana, "b")
    turtle.onkeypress(add_goat, "g")
    turtle.onkeypress(add_bouncy, "c")
    
    turtle.listen()

    time_step = 1/60
    animation_loop(shapes, time_step)
    
main()