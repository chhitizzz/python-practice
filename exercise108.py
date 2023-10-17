# Create a class called `Person` with attributes `name` and `age`. Implement a method `display_info()` that prints the name and age of a person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Paul", 23)
person1.display_info()

person2 = Person("John", 32)
person2.display_info()