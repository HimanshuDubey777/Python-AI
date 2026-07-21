

name1 = "Himanshu"
salary1 = 30000

name2 = "pooja"
salary2 = 25000

def calculate_bonus(salary):
    return salary * 0.10


print(f"{name1} 'bonus: {calculate_bonus(salary1)}")
print(f"{name2} 'bonus: {calculate_bonus(salary2)}")



class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10


emp1 = Employee("Himanshu", 90000)
print(emp1.salary)
print(emp1.calculate_bonus())






