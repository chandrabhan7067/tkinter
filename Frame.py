from tkinter import *

root = Tk()

root.geometry("600x333")

f1 = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)

f2 = Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(fill=X)

l1 = Label(f1,text="project")
l1.pack(pady=150,padx=30)

l2 = Label(f2,text="welcome to new world")
l2.pack()


root.mainloop()