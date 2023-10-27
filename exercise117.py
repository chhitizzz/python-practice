# Create a class called `Employee` with attributes `name`, `position`, and `salary`. Implement a method `calculate_bonus()` that returns a bonus amount based on the employee's position

class Employee:
    def __init__(self, name, position, salary):
        self.name = name 
        self.position = position 
        self.salary = salary 

    def calculate_bonus(self):
        if self.position == "Manager":
            return self.salary * 0.2 
         
        elif self.position == "Supervisor":
            return self.salary * 0.1
        
        else:
            return self.salary * 0.05