# Create a class called `Dog` with attribute `name`. Implement a method `bark()` that prints a message indicating that the dog is barking

class Dog:
    def __init__(self, name):
        self.name = name 

    def bark(self):
         print(f"{self.name} is barking.")

my_dog = Dog("Subhu")
my_dog.bark()