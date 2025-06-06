# tup = (1)
# print(type(tup))   -->output will be the (int) it form confusion to the python interperter
#So, for this we use ,
#tup = (1, )   -->now it will show correct output (tuple)
# print(type(tup))

tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)

print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
  
tup2 = tup[1:4]
print(tup2)