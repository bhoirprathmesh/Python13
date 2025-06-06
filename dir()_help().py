x = [1, 2, 3]
print(dir(x)) # list of all the attributes and methods available for an object.
print(x.__add__)  # give info about particular methods.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("John", 30)
print(p.__dict__)  # attribute returns a dictionary representation of an object's attributes.

print(help(Person)) # function is used to get help documentation for an object, including a description of its attributes and methods.