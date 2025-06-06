a = input("Enter your name: ")
print("My name is", a)

x = input("Enter first number: ")  # at run time compiler will consider that the input which is provide this is a "String"
y = input("Enter second number: ")
print(x  + y)  #acc. to this we get concatenate the two variable

print(int(x) + int(y))   #for this we need to type-cast it 