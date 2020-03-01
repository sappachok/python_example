# Set or Dictionary
s1 = {1,2,3,4,5}
s2 = {5,6,7}

print(s1.union(s2))
print(s1 | s2)

print(s1.intersection(s2))
print(s1 & s2)

print(s1.difference(s2))
print(s1 - s2)

s2.update(["red","green"])
print(s2)

s2.remove("red")
print(s2)