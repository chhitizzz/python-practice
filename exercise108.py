# Create a class called `Person` with attributes `name` and `age`. Implement a method `display_info()` that prints the name and age of a person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")