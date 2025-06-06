class Person:
  def __init__(self, name, occ):   #-->(__init__)used to create the constructor. it intializes the values and return the null value.
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
a.info()
print()
b = Person("Divya", "HR") 
b.info()
# print(a.name)
# a.name = "Divya" 
# a.occ = "HR"
# a.info()

