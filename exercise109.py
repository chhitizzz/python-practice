# Create a class called `Rectangle` with attributes `length` and `width`. Implement a method `calculate_area()` that returns the area of the rectangle

class Rectangle: 
    def __init__(self, length, width):
        self.length = length 
        self.width = width 
    
    def calculate_area(self):
        return self.length * self.width