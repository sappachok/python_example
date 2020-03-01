import os

print(os.getcwd())

os.mkdir("TESTDIR")
print(os.listdir())

# os.F_OK, os.R_OK, os.W_OK, os.X_OK

print(os.access("TESTDIR", os.F_OK))

os.removedirs("TESTDIR")
print(os.listdir())