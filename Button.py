from tkinter import *

root = Tk()
root.geometry("600x500")

def hello():
    print('Hello broh..')

def name():
    print('My name is chandrabhan')

f1 = Frame(root,borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1 = Button(f1,bg="red",borderwidth=4,text="print Now")
b1.pack(side=LEFT,padx=30)

b2 = Button(f1,bg="red",borderwidth=4,text="Enter name",command=name)
b2.pack(side=LEFT,padx=30)

b3 = Button(f1,bg="red",borderwidth=4,text="print Now",command=hello)
b3.pack(side=LEFT,padx=30)

root.mainloop()