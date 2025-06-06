f1 = open("hello.txt", "w")
text = f1.write("Hello, world!")   #-->This mode opens the file for writing only and creates a new file if the file does not exist.(if we use it directly then it clear the previous data or present data in the txt file)
print(text)
f1.close()

f2 = open("hello.txt", "r")
text1 = f2.read()   #--> This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
print(text1)
f2.close()

f3 = open("hello.txt", "rt")  #--> the file get open as the text file 
f4 = open("hello.txt", "rb")     #--> the file get open as the binary file

f5 = open("hello.txt", "a")
f5.write(" See you soon!")   #-->append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
f5.close()

f6 = open("hello.txt", "r")
print(f6.read())

# with open('hello.txt', 'a') as f:
#     f.write("Hey I am inside with")   #-->no need to close the file if we are using (with...)


