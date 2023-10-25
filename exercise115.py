# Create a class called `Triangle` with attributes `base` and `height`. Implement a method `calculate_area()` that returns the area of the triangle

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height 
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
area1 = Triangle(2, 4)
print(f"The area of triangle is {area1.calculate_area()}")