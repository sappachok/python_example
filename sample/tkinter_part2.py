from tkinter import *
from tkinter import messagebox

gui=Tk()
gui.geometry("800x600")
gui.title("Python GUI Basic")

l1=Label(text="Firstname").grid(row=0, column=1)
l2=Label(text="Lastname").grid(row=1, column=1)

e1=Entry().grid(row=0, column=2)
e2=Entry().grid(row=1, column=2)

b1=Button(text="Submit").grid(row=2, column=1)
gui.mainloop()