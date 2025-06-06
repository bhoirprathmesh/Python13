def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass              # pass keyword is used for a placeholder for future code.

def welcome():
  print("Good Morning, Have a nice DAY !")
  
if __name__ == "__main__":
  welcome()

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)

c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)

