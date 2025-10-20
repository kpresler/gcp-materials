# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 14:59:20 2025

@author: Kai
"""

# Task 1

class Car:
    
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        
    def __str__(self):
        return f"{self.colour} {self.year} {self.make} {self.model}"
    


# Task 2

class Car:
    
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.current_speed = 0
        
    def __str__(self):
        return f"{self.colour} {self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return self.__str__()
    
    def go_faster(self, how_much_faster = 5):
        self.current_speed += how_much_faster

    def brake(self):
        if self.current_speed >= 5:
            self.current_speed -= 5
        else:
            self.current_speed = 0
    
    def how_fast(self):
        return self.current_speed


# Task 3 / 3.1
    
def filter_cars_by_colour(list_of_cars, colour="blue"):
    return [car for car in list_of_cars if car.colour == colour]

my_car = Car("Toyota", "Prius", 2011, "Silver")
print(my_car)

other_car = Car("Ford", "E150", 1999, "Red")
print(other_car)

red_car = Car("Mazda", "Miata", 2023, "Red")

red_car.year = 1995

my_car.go_faster(3)
my_car.brake()
print(my_car.current_speed)
my_car.go_faster()

print(my_car.current_speed)


all_cars = [my_car, other_car, red_car]

print(all_cars)

for red in filter_cars_by_colour(all_cars, "Red"):
    print(red)
    
    
# Task 4

class Course:
    
    def __init__(self, subject, number, title, instructor, enrollment_cap = 30):
        self.subject = subject
        self.number = number
        self.title = title
        self.instructor = instructor
        
        # this will either set enrollment to the default, if the user doesn't specify a value, or use what they provide
        self.enrollment_cap = enrollment_cap
        
        # this initialises fields we want to use later on
        # even though no data was provided for them in the
        # initialiser call
        self.enrolled_students = list()
        self.waitlisted_students = list()
        
    def __str__(self):
        return "{} {}: {} ({})".format(self.subject, self.number, self.title, self.instructor)
    
    def enroll(self, student):
        # already enrolled
        if student in self.enrolled_students or student in self.waitlisted_students:
            raise ValueError("You can't enroll in a class twice!")
        # class is full -- add to waitlist    
        if len(self.enrolled_students) >= self.enrollment_cap:
            self.waitlisted_students.append(student)
            return False
        # enroll normally
        self.enrolled_students.append(student)
        return True

    def drop(self, student):
        if student not in self.enrolled_students and student not in self.waitlisted_students:
            raise ValueError("This student is not currently enrolled or waitlisted for this course!")
        
        # if just on the waitlist, fine, you get removed
        if student in self.waitlisted_students:
            self.waitlisted_students.remove(student)
        else:
            # if you're actually enrolled, and there's someone on the waitlist, handle that
            if len(self.waitlisted_students) > 0:
                first_in_waitlist = self.waitlisted_students.pop(0)
                self.enrolled_students.append(first_in_waitlist)
            self.enrolled_students.remove(student)
