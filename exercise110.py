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
print(f"The circumference of the circle having radius {circle1.radius} is {circumference1:.2f}" )
print(f"The area of the circle having radius {circle1.radius} is {area1:.2f}")

print("")

circle2 = Circle(10)
circumference2 = circle2.calculate_circumference()
area2 = circle2.calculate_area()
print(f"The circumference of the circle having radius {circle2.radius} is {circumference2:.2f}" )
print(f"The area of the circle having radius {circle2.radius} is {area2:.2f}")