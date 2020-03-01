class MyClass:
    x = 5

a = MyClass()
print(type(a))
print(a.x)

class MyClass2:
    def __init__(self, num):
        self.x = num
        print("number is", self.x)

b = MyClass2(50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("My name is {}. I 'm {} years old.".format(self.name, self.age))
  
p = Person("Sappachok", 25)
print(p.name)
print(p.age)
p.info()

