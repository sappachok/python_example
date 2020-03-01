a = [1,2,3,4,5] # List
print(a)
print(type(a))

b = ["a","b","c","d"] # List
print(b)
print(type(b))

c = {1, "one","two","three","four"} # Set
print(c)
print(type(c))

d = ("red","green","blue","yellow") # Tuple
print(d)
print(type(d))

# slicing

print(a[1:])
print(b[1:4])
#print(c(1))
print(d[0:2])

b[0] = "x"
#d[0] = "black"
print(b)

n = a+b
print(n)

a.append(6)
a.append(10)
a.insert(0, 99)
print(a)