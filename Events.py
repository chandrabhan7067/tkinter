from tkinter import *

root = Tk()

def chandu(event):
    print(f"you clicked button at {event.x}, {event.y} ")

root.geometry("600x600")
b1 = Button(root,text="please click here")
b1.pack()

b2 = Button(root,text="For quit double click on button")
b2.pack()

b1.bind('<Button-1>',chandu)
b2.bind('<Double-1>',quit)

root.mainloop()
