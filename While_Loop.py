i = 12

while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")
print("\n")

count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")
print("\n")
 

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break

print("We found the Negative Number\nExit")