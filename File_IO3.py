#seek(), tell(), truncate() and other function.

with open('hello.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(8)
  
  print(f.tell())

  # Read the next 5 bytes
  data = f.read(5)
  print(data)
  
# with open('sample.txt', 'w') as f:
#   f.write('Hello World3!')
#   f.truncate(3)            #read just three words

# with open('sample.txt', 'r') as f:
#   print(f.read())