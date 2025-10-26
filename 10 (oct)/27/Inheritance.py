# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 15:55:40 2025

@author: Kai
"""


# The real power of object-oriented programming comes from that just like
# _objects_ don't exist in isolation (that is, it possible to instantiate
# a class as many times as you want -- you can have a bunch of objects
# of the same type, that share the same attributes/behavious, but individually
# store different data), _classes_ also don't exist in isolation


# We've seen some of this already.  The Vector class we worked with has-a 
# Point2D at each end.  Rather than needing to re-implement the idea of what
# a "Point" looks like, we can take advantage of code that already does some
# of what we want.  This is an incredibly powerful paradigm -- we can build
# more complicated objects by _composing_ together multiple, simpler, types
# that do part of what we need.  If I want to model a University, I don't
# want _all_ of the functionality for the University to exist in a single class
# instead, I'll have other clases that represent reasonable things to be 
# used by the university -- a Student class, a Professor class, a Course class,
# a Transcript class, a Classroom class, etc.  And then I can use has-a 
# relationships; a Course has-a professor and has-a (or rather, has-many) 
# Students; a Student has-a Transcript, and so on and so forth.


# there's another powerful relationship that we can use in object-oriented 
# programming -- the is-a relationship.  is-a is used to _inherit_ (or _extend_)
# from an existing class.  this is useful when you want to create a new type
# that is a specialised version of an existing type.  This new class will
# inherit everything present in its superclass -- all of the fields and all 
# of the methods, and then we can add what is _new_ to the subclass, but
# we don't have to duplicate what's already there.

# Let's see an example of using inheritance, which I hope you'll really enjoy :)



import turtle
import random

max_speed = 500

# defines a class, which represents the template from which all objects will be stamped out

class Ball:
    
    def __init__(self, position = None, velocity = None):
        """ this is the initialiser which lets us create new Ball objects.  a ball will have a position & a velocity,
        both of which are optional & will use suitable defaults"""
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
            
    def draw(self, turtle):
        """ draws the turtle to the screen using the provided turtle"""
        turtle.penup()
        turtle.goto(self.position[0], self.position[1])
        turtle.dot(10)



def main():
    # turtle setup
    turtle.clear()
    turtle.hideturtle()

    # create a few objects
    b = Ball(position = (100, 100))
    b2 = Ball(position = (50, -50))
    b3 = Ball(position = (50, 0))

    # make them do stuff
    b.draw(turtle)
    b2.draw(turtle)
    b3.draw(turtle)

    turtle.update()
    turtle.done()

# main()




import random
import time
import turtle

max_speed = 500
shapes = []


class Ball:
    def __init__(self, size = 10, position = None, velocity = None):
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
        
        self.size = size

    # we might normally choose to create a __str__ method here, or maybe a __repr__ method too

    def move(self, time):
        (px, py) = self.position
        if abs(px) >= 250: 
            self.velocity = (-self.velocity[0], self.velocity[1])

        if abs(py) >= 250:
            self.velocity = (self.velocity[0], -self.velocity[1])

        (vx, vy) = self.velocity
        # set position to computed position at time
        self.position = (px + (vx * time), py + (vy * time))

    
    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.position[0], self.position[1])
        turtle.dot(self.size)



# this is bound to a key so we can create new Balls
def add_ball():
    shapes.append(Ball(random.randrange(20) + 1))

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

    turtle.tracer(0, 0) # only render when we say so
    turtle.hideturtle() # hide the icon
    turtle.penup()

    turtle.onkeypress(add_ball, 'space')
    
    turtle.listen()

    time_step = 1/60
    animation_loop(shapes, time_step)

# main()



# that was all well-and-good
# but what if we wnat the ability to draw _multiple_ shapes
# we are unfortunately out of luck here, at least without substantial
# extra work in order to do so, we'd need to completely recreate the 
# Ball class, and make only very minimal changes, for each additional 
# shape that we want to draw

# needless to say, this is Not Good, because any time we see duplication, 
# our spidey senses ought to start tingling



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
    


# this is the rest of the code that makes the physics simulator do stuff


# this is bound to a key so we can create new Balls
def add_ball():
    shapes.append(Ball(random.randrange(20) + 1))

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

    turtle.tracer(0, 0) # only render when we say so
    turtle.hideturtle() # hide the icon
    turtle.penup()

    turtle.onkeypress(add_ball, 'space')
    
    turtle.listen()

    time_step = 1/60
    animation_loop(shapes, time_step)

# main()




class Apple(Shape):
    
    def draw(self, turtle):
        super().draw(turtle)
        turtle.shape('apple.gif')
        turtle.stamp()
        

# this is bound to a key so we can create new Apples        
def add_apple():
    shapes.append(Apple())
        
# main function that starts running the program
def main():
    screen = turtle.Screen()
    screen.addshape('apple.gif')

    turtle.tracer(0, 0) # only render when we say so
    turtle.hideturtle() # hide the icon
    turtle.penup()

    turtle.onkeypress(add_ball, 'space')
    turtle.onkeypress(add_apple, 'a')
    
    turtle.listen()

    time_step = 1/60
    animation_loop(shapes, time_step)

#main()


class Apple(Shape):
    def draw(self, turtle):
        super().draw(turtle)
        turtle.shape('apple.gif')
        turtle.stamp()
        

# this is bound to a key so we can create new Apples        
def add_apple():
    shapes.append(Apple())
        
# main function that starts running the program
def main():
    screen = turtle.Screen()
    screen.addshape('apple.gif')

    turtle.tracer(0, 0) # only render when we say so
    turtle.hideturtle() # hide the icon
    turtle.penup()

    turtle.onkeypress(add_ball, 'space')
    turtle.onkeypress(add_apple, 'a')
    
    turtle.listen()

    time_step = 1/60
    animation_loop(shapes, time_step)

#main()



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
    
def add_goat():
    shapes.append(Goat())
            
# main function that starts running the program
def main():
    screen = turtle.Screen()
    screen.addshape('apple.gif')
    screen.addshape("banana.gif")
    screen.addshape("goat.png")

    turtle.tracer(0, 0) # only render when we say so
    turtle.hideturtle() # hide the icon
    turtle.penup()

    turtle.onkeypress(add_ball, 'space')
    turtle.onkeypress(add_apple, 'a')
    turtle.onkeypress(add_banana, "b")
    turtle.onkeypress(add_goat, "g")
    
    turtle.listen()

    time_step = 1/60
    animation_loop(shapes, time_step)
    
main()