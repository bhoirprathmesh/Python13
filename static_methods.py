#static methods not belong to the instance or any class
class Math:
    # instance method associate with the class
    def __init__(self, num):    
        self.num = num
        
    def addtonum(self, n):
        self.num += n
    
    # static method associate with the class we can call methods independently      
    @staticmethod
    def add(a, b):
        return a + b  # output: 3
    
# result = Math.add(1, 2)
# print(result)

result = Math(5)
print(result.num)
result.addtonum(6)
print(result.num) 

print(result.add(7, 2))

# Note : the is no need to use self argumemnt to create a method in the class