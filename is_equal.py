a = "hello"
b = "hello"

print(a == b)  # value
print(a is b)  # exact location of object in memory

c = 5
d = 5

print(c == d) 
print(c is d) 

e = [1, 2, 3]
f = [1, 2, 3]

print(e == f) 
print(e is f) 

g = None
h = None

print(g is h)
print(g is None) 
print(g == h) 

i = 5
j = "5"

print(i == j) 
print(i is j) 
