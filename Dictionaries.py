info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(type(info))
print(info.keys())
print(info.values())

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")   #-->f_String concepts
    
print("\n")
print(info.items())
print(type(info.items()))

for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  