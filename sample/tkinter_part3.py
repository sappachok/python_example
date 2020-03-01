from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

        self.submitButton = ttk.Button(self, text = "Save", command = self.saveForm)
        self.submitButton.grid(column = 0, row = 2)

        self.imageFrame = ttk.LabelFrame(self, text = "Image Preview")
        self.imageFrame.grid(column = 0, row = 3, padx = 20, pady = 20)


    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 3)
        self.label.configure(text = self.filename)

        self.img = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.img)
        
        self.label2 = Label(self.imageFrame, image=self.photo)
        self.label2.image = self.photo 
        self.label2.grid(column=0, row=4)

    def saveForm(self):
        print("save!!")
        filename = "images/temp.jpg"
        self.img.save(filename)
        #os.system(filename)
        #self.photo.save()
        messagebox.showinfo(title="ข้อความจากระบบ",message="บันทึกเสร็จสิ้น")
        self.destroy()

root = Root()
root.mainloop()