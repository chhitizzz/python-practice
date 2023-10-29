# Create a Student class with attributes like name, age, and grade. Write a program that allows you to create student objects and display their information

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade 

def main():
    student1 = Student("Troy", 18, "A")
    student2 = Student("James", 17, "B")        
    student3 = Student("Ben", 16, "C")

    print("Student Information")
    print(f"Name: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")
    print(f"Name: {student2.name}, Age: {student2.age}, Grade: {student2.grade}")
    print(f"Name: {student3.name}, Age: {student3.age}, Grade: {student3.grade}")

if __name__ == "__main__":
    main()