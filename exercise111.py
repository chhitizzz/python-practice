# Create a class called `Student` with attributes `name` and `grade`. Implement a method `get_grade()` that returns the grade of the student as a letter (A, B, C, etc.) based on a grading scale

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade