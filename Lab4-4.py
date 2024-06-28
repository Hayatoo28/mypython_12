a = {1,2,3,4,5,6,8}
b = {3,5,6,7,8}
c = {5,4,3,2,1}
print(a.union(b).union(c))
print(a |b| c)
print(a.intersection(b).intersection(c))
print(a & b & c)
print(b.difference(a))
print(b-a)
