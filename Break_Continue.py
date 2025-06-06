for i in range(1, 12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)
print("\n")
  
i = 0
while True:
  print(i)
  i = i + 1
  if(i % 50 == 0):
    break