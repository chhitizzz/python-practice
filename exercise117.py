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
        
employee1 = Employee("Kenny", "Manager", 80000)
bonus1 = employee1.calculate_bonus()
print(f"{employee1.name}'s bonus: Rs.{bonus1}")

employee2 = Employee("Watt", "Supervisor", 60000)
bonus2 = employee2.calculate_bonus()
print(f"{employee2.name}'s bonus: Rs.{bonus2}")

employee3 = Employee("Jackson", "Employee", 40000)
bonus3 = employee3.calculate_bonus()
print(f"{employee3.name}'s bonus: Rs.{bonus3}")