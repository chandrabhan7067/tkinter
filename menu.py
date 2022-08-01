from tkinter import *

root = Tk()
root.geometry("500x500")

def myfun():
    print("yes working")

# non dropdown menu

# mymenu = Menu(root)
# mymenu.add_command(label="file",command=myfun)
# mymenu.add_command(label="exit",command=quit)
# root.config(menu=mymenu)

filemenu = Menu(root)

m1 = Menu(filemenu,tearoff=0)
m1.add_command(label="projects",command=myfun)
m1.add_command(label="save",command=myfun)
m1.add_separator()
m1.add_command(label="edit",command=myfun)
m1.add_command(label="print",command=myfun)

root.config(menu=filemenu)
filemenu.add_cascade(label="view projects",menu=m1)

m2 = Menu(filemenu,tearoff=0)
m2.add_command(label="cut",command=myfun)
m2.add_command(label="paste",command=myfun)
m2.add_separator()
m2.add_command(label="copy",command=myfun)
m2.add_command(label="find",command=myfun)

root.config(menu=filemenu)
filemenu.add_cascade(label="Edit",menu=m2)


root.mainloop()