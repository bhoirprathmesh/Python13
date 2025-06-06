# MAP FUNCTION
# def cube(x):
#   return x * x * x


# print(cube(2))

l1 = [1, 2, 4, 6, 4, 3]
# newl = []
# for item in l:
#   newl.append(cube(item))

newl = list(map(lambda x: x*x*x, l1))
print(newl)




# FILTER FUNCTION
# def filter_function(a):
#   return a>2
  
newnewl = list(filter(lambda a: a>2, l1))
print(newnewl)




#REDUCE FUNCTION
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
# def mysum(x, y):
#   return x + y
  
sum = reduce(lambda x, y: x+y, numbers)

# Print the sum
print(sum)

