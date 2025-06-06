fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:]) # from index 0 to index 5 (automatically decided by pyhton interpreter)
print(fruit[:5]) #directly set the index 0
print(fruit[0:-3])   # 0 : len(fruit) -3  //5-3 
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])    # 4 : 2  it do not slice but not show error and create a blank space.
print(fruit[-3:-1])     # 2 : 4
print(fruit[::-1])      # reverse the string [strat:stop:step]
