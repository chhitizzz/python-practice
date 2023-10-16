# Create an instance of the Person class and assign the values "Alice" and 30 to name and age respectively

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)

print(f"Person 1: Name - {person1.name}, Age - {person1.age}")