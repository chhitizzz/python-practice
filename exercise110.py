# Create a class called `Circle` with the attribute `radius`. Implement methods `calculate_circumference()` and `calculate_area()` that return the circumference and area of the circle, respectively

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

circle1 = Circle(5)
circumference1 = circle1.calculate_circumference()
area1 = circle1.calculate_area()
print("The circumference of the circle is ", circumference1)
print("The area of the circle is ", area1)