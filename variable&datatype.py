a = 1         #int 
b = True      #bool
c = "Harry"   #string  -->both are possible 'Harry'
d = None      #nonetype
e = complex(8, 2)   #complex
print(a)
print(b)
print(e)
print(d)
a1 = 9
print(a + a1)
print("The type of a is ", type(a))    #type()-->use to find the data type
print("The type of b is ", type(b))
print("The type of c is ", type(c))
print("The type of c is ", type(e))
print("The type of c is ", type(d))


list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]     #-->data type (muteable-->value can be change)
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))   #-->data type  (non-muteable-->value can not be change)
print(tuple1)

dict1 = {"name":"Om", "age":20, "canVote":True}    #-->data type  -->also called as Mqpped data type
print(dict1)