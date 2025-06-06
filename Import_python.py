import math
# from math import sqrt -->import specific functions or variables from a module using the from keyword
# from math import * -->import all functions and variables from a module using the * wildcard
# import math as m  --> give a shortcut name to the import package

# from Function import welcome
import Example1 

Example1.Welcome()

print(dir(math))  #--> use to view the names of all the functions and variables defined in a module.
print(math.nan, type(math.nan))