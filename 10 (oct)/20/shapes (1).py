#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

class Point:
    """
    Class to represent a 2D point
    """       
    def __init__(self,x,y):        
        self.x = x
        self.y = y
        
    def getX(self):        
        return self.x
    
    def getY(self):        
        return self.y
    
    def setX(self,x):        
        self.x = x
    
    def setY(self,y):        
        self.y = y
        
    
class Circle:    
    """
    Class to represent a circle
    """
    def __init__(self,center,radius):       
        self.center = center
        self.radius = radius
        
    def getCenter(self):         
         return self.center
    
    def getRadius(self):        
        return self.radius
        
    def setCenter(self,center):         
         self.center = center
    
    def setRadius(self, radius):        
        self.radius = radius
    
    def getArea(self):        
        return math.pi* self.radius ** 2
        
    def getPerimeter(self):        
        return 2* math.pi * self.radius
    
    def contains(self,otherCircle):  
        # Check if circle contains otherCircle
        d = (otherCircle.getCenter().getX() - self.getCenter().getX())**2 \
        +  (otherCircle.getCenter().getY() - self.getCenter().getY()) **2        

        if math.sqrt(d) + otherCircle.getRadius() < self.radius:            
            return True
        else:            
            return False

if __name__ == "__main__":
    p1 = Point(-2,2)
    c1 = Circle(p1,4)
    
    p2 = Point(4, 2)
    c2 = Circle(p1, 8)
    
    d = (c2.getCenter().getX() - c1.getCenter().getX())**2 +  (c2.getCenter().getY() - c1.getCenter().getY()) **2
    
    print(d,c1.getRadius() + c2.getRadius())
    
    
    if math.sqrt(d) >= c1.getRadius() + c2.getRadius():
        # print a sensible message here 
    
    elif math.sqrt(d) < (c1.getRadius() + c2.getRadius()):
        # print a sensible message here 

    print(c2.contains(c1))
    print(c2.radius)
    c2.setRadius(10)
    print(c2.radius)
