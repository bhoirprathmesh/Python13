# Default arguments:
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
print()


# Keyword arguments:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
print()


# Required arguments:
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")  -->throws an error
#print("\n")


# Variable-length arguments:
#return statement
def average(*numbers):   #--> * indicate 'n' numbers 
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)
print()

#two types
# 1.Arbitrary Arguments:
def name(*name):
    print(type(name))
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
print()

# 2.Keyword Arbitrary Arguments:
def name(**name):
  print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")
print()
