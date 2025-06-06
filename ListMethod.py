l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

l.append(7)
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(1))    #position of the 1 at the first occurence

print(l.count(1))    #no. of count 1 in the given list

m = l.copy()
m[0] = 0
print(m)

l.insert(1, 899)
print(l)

n = [900, 1000, 1100]
k = l + n
print(k)

l.extend(n)
print(l)