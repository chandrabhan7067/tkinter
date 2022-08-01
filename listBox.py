from tkinter import *


root = Tk()
root.geometry("500x500")
def add():
    global i
    lbx.insert(ACTIVE,f"{i} item")
    i += 1
i = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"First item of the list")
Button(root,text="Add item",command=add).pack()
root.mainloop()