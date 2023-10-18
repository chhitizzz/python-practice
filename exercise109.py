# Create a class called `Rectangle` with attributes `length` and `width`. Implement a method `calculate_area()` that returns the area of the rectangle

class Rectangle: 
    def __init__(self, length, width):
        self.length = length 
        self.width = width 
    
    def calculate_area(self):
        return self.length * self.width
    
rectangle1 = Rectangle(6, 5)
area1 = rectangle1.calculate_area()
print("Area of Rectangle 1:", area1)

rectangle2 = Rectangle(9, 4)
area2 = rectangle2.calculate_area()
print("Area of Rectangle 2:", area2)