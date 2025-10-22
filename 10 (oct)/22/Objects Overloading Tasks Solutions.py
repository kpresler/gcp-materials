# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 14:19:40 2025

@author: Kai
"""

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
    
    
class Vector:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __str__(self):
        return f"Vector({self.start} -> {self.end})"
    
    
    def __add__(self, other):
        thisXComp = self.end.x - self.start.x
        thisYComp = self.end.y - self.start.y
    
        otherXComp = other.end.x - other.start.x
        
        otherYComp = other.end.y - other.start.y
        
        start = self.start
        
        end = Point2D(self.start.x + thisXComp + otherXComp\
                      , self.start.y + thisYComp + otherYComp)
        
        return Vector(start, end)
    

s = Point2D(0, 0)
e = Point2D(4, 5)

vec = Vector(s, e)

print(vec)

vec2 = Vector (Point2D(5, 5), Point2D(3, -6))
print(vec2)


res = vec + vec2
print(res)

