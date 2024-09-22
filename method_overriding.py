class Employee:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def print_employee_info(self):
        employee_info = f"{self.first_name} {self.last_name} {self.date_of_birth}"
        return employee_info

new_employee = Employee('Mickey', 'Mouse', '10/10/1890')
print(new_employee.print_employee_info()) 

class Hourly_Employee(Employee):
    def __init__ (self, first_name, last_name, date_of_birth, hourly_wage, hours_worked):
        super().__init__(first_name, last_name, date_of_birth)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def print_employee_info(self):
        employee_info = f"{super().print_employee_info()} {self.hourly_wage} {self.hours_worked}" 
        return employee_info 

regular_employee = Employee('Donald', 'Duck', '10/10/1999') 
print(regular_employee.print_employee_info())

new_employee = Hourly_Employee('Nibar', 'Poudel', '100k', '6hours')
print(new_employee.print_employee_info)

'''class Animal:
    def make_sound(self):
        print("Generic Animal Sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animal_1 = Animal()
new_dog = Dog()
new_cat = Cat()

animal_1.make_sound()
new_dog.make_sound()
new_cat.make_sound()'''
