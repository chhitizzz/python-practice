# Create a class called `Car` with attributes `make`, `model`, and `year`. Implement a method `start_engine()` that prints a message indicating that the car engine has started

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 

    def start_engine(self):
        print(f"{self.year} {self.make} {self.model}'s engine has started.")