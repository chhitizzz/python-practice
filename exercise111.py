# Create a class called `Student` with attributes `name` and `grade`. Implement a method `get_grade()` that returns the grade of the student as a letter (A, B, C, etc.) based on a grading scale

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_grade(self):
        if 90 <= self.grade <= 100:
            return 'A'
        
        elif 80 <= self.grade <= 90:
            return 'B'
        
        elif 70 <= self.grade <= 80:
            return 'C'
        
        elif 60 <= self.grade <= 70:
            return 'D'

        elif 0 <= self.grade < 60:
            return 'F'
        
        else:
            return 'Invalid'

student1 = Student("Ben", 96)
grade1 = student1.get_grade()
print(f"{student1.name}'s grade is: {student1.grade}")

student2 = Student("Troy", 84)
grade2 = student2.get_grade()
print(f"{student2.name}'s grade is: {student2.grade}")