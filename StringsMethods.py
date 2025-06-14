# Strings are immutable
a = " !!!Harry!! !!!!!!!!! Harry "
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))   # rstrip() removes any trailing characters
print(a.strip(" "))    #strip() method removes any white spaces before and after the string.
print(a.replace("Harry", "John"))
print(a.split(" "))    #given string at the specified instance and returns the separated strings as list items.
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())  #capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) #isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9.
                    #If any other characters or punctuations are present, then it returns False.

str1 = "Welcome"
print(str1.isalpha())   #isalpha() method returns True only if the entire string only consists of A-Z, a-z.
                        #If any other characters or punctuations or numbers(0-9) are present, then it returns False.

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace()) # isspace() method returns True only and only if the string contains white spaces, else returns False.

str1 = "World Health Organization" 
print(str1.istitle())  #istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())  #title() method capitalises each letter of the word within the string