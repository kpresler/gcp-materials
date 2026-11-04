#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:26:52 2019

@author: kkutten1
@author: Kai
"""
import math


class Shape:
    def __init__(self):
        self.name = "Shape"
        
    def display(self):
        print(f"I am a {self.name}")


class Polygon(Shape):

    def __init__(self, side_lengths):
        super().__init__()
        
        self.name = "Polygon"
        self.side_lengths = side_lengths
        
    def getPerimeter(self):
        return sum(self.side_lengths)
        
        
    def display(self):
        super().display()
        print(f"I have {len(self.side_lengths)} sides.")
        print(f"My perimeter is {self.getPerimeter()}")



class RightTriangle(Polygon):
    def __init__(self, width, height):
        
        diagonal = math.sqrt(width**2 + height**2)
        side_lengths = [width, height, diagonal]
        
        super().__init__(side_lengths)
        
        self.width = width
        self.height = height
        self.name = "Right Triangle"
        
    def display(self):
        super().display()
        print(f"My area is {self.getArea()}")

    def getArea(self):
        return self.width*self.height / 2


def main():
    T = RightTriangle(3,4)
    T.display()
    print()

if __name__ == "__main__": main()