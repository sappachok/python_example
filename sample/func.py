def hello(name):
    print("my name is", name)

def hello2(fname, lname, age):
    print("My name is", fname, lname)
    print("I 'am", age, "years old")

hello("Sappachok")
hello2("Sappachok", "Singhasuwan", 25)

def count_vowel(str):
    vowel = 0
    for c in str:
        if c in ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'):
            vowel = vowel + 1
    return vowel

a = count_vowel("Merry, Christmas!!")
print(a)