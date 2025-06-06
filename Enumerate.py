# enumerate function in python which has sequence (such as a list, tuple, or string) 
# and get the index and value of each element in the sequence at the same time.

marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 1
# for mark in marks:
#   print(index, mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, mark in enumerate(marks, start=1):
  print(index, mark)
  if(index == 3):
    print("Harry, awesome!")
    