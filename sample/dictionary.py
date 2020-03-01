thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["model"])

for x in thisdict:
  print(x)

print("*"*20)

for x, y in thisdict.items():
  print(x, ":", y)  