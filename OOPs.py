class Person :  # --> Class 
    name = "Prathmesh Bhoir"
    occupation = "Software Engineer"  # ---> 1]
    networth = "10LPA"
    
    def info(self):  # self parameter is the reference to the current instence of the class and to access variable that belongs to the class.
        print(f"{self.name} is a {self.occupation}")

a = Person()      # --> Object  [here 'a' object is called on the info(self)] 
a.name = "PRATHAM"
a.occupation = "Data Engineer"
# print(a.name,"-" ,a.occupation,"-", a.networth)  -->using form 1]
a.info()

#also,  --->create n number of objects.
b = Person() # --> Object      [here 'b' object is called on the info(self)] 
b.name = "Nikita"
b.occupation = "HR"
b.info()

c = Person()  # we not change the value of the c we get the default value from the class.
c.info()
 