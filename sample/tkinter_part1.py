from tkinter import *
from tkinter import messagebox

def hello_msg():
    print("Hello Everybody")

def submit():    
    status=messagebox.askyesno(title="ข้อความแจ้ง",message="ต้องการบันทึกใช่หรือไม่")
    print("submit status: ", status)   
    print("textbox: ", textvar1.get()) 
    
    if l1.curselection() :
        index = l1.curselection()[0]
        print("listbox item value: ", index)
        print("listbox item select: ", l1.get(index))

    print("spinbox: ", spinvar1.get())

def show_about():
    status=messagebox.showinfo(title="เกี่ยวกับระบบ",message="ทดสอบเขียน GUI ด้วยภาษา python")

def close():
    gui.destroy()

gui=Tk()
gui.geometry("800x600")
gui.title("Python GUI Basic")

mlabel=Label(text="SAPPACHOK",fg="red",bg="#eee") # or use Lable(..).pack()
mlabel.pack()

textvar1 = StringVar()  
# create textbox
objEntry=Entry(gui, textvariable=textvar1).pack()

#hello_msg = partial(hello_msg, textvar1)  

# create spinbox
spinvar1 = StringVar()
spin1=Spinbox(gui, from_=1, to=100, textvariable=spinvar1).pack() # state=['disabled','readonly']

# create button
mButton=Button(text="Submit",fg="red", command=submit).pack()
mButtonMsg=Button(text="Show Message",fg="black", command=hello_msg).pack()

# create radio button
r1=Radiobutton(text="ชาย", value=1).pack()
r2=Radiobutton(text="หญิง", value=2).pack()

OPTIONS = [
"one",
"two",
"three"
]

# create dropdown
var1 = StringVar()
var1.set("one")
o1=OptionMenu(gui, var1, *OPTIONS).pack()

# create listbox
l1=Listbox(gui) #selectmode=['single', 'multiple']
l1.insert(1,"Python");
l1.insert(2,"JAVA");
l1.insert(3,"DATABASE");
l1.pack()

# create scale
v = DoubleVar()  
scale = Scale(gui, variable = v, from_ = 1, to = 50, orient = HORIZONTAL)  
scale.pack(anchor=CENTER)  

# create menu
menubar=Menu(gui)

# create file menu
fileMenu=Menu(menubar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Close", command=close)
menubar.add_cascade(label="File", menu=fileMenu)

# create help menu
helpMenu=Menu(menubar,tearoff=0)
helpMenu.add_command(label="About", command=show_about)
helpMenu.add_command(label="Document")

menubar.add_cascade(label="Help", menu=helpMenu)

gui.config(menu=menubar)
gui.mainloop()