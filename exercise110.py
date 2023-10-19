# Create a class called `Circle` with the attribute `radius`. Implement methods `calculate_circumference()` and `calculate_area()` that return the circumference and area of the circle, respectively

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * 3.14 * self.radius
    
    def calculate_area(self):
        return 3.14 * (self.radius ** self.radius)