tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res1 = tuple1.count(3)
print(res1)

res2 = tuple1.index(3)
print(res2)

#res3 = tuple1.index(311)  -->error

res4 = tuple1.index(3, 4, 8)  #-->index(element, start, end)
print(res4)

res5 = len(tuple1)
print(res5)