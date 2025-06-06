# Class variable shared among all instance of the class
class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj2 = MyClass()

"""
obj1 = MyClass():
When obj1 is created, the __init__ method is called.
MyClass.class_variable is incremented from 0 to 1.

obj2 = MyClass():
When obj2 is created, the __init__ method is called again.
MyClass.class_variable is incremented from 1 to 2.
"""

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2

# Instance variable is unique to the each instnace of the class
class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane

# e.g.
class Employee:
  companyName = "Apple"   # this is the class variable
  noOfEmployees = 0         # class variable
  
  def __init__(self, name):
    self.name = name           # this is the instance variable
    self.raise_amount = 0.02    # instance variable
    Employee.noOfEmployees +=1
    
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3      
emp1.companyName = "Apple India" 
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()