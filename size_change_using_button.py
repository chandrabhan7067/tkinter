from tkinter import *

root = Tk()

root.geometry("400x400")

def change_size():
    width1 = width.get()
    height1= height.get()
    root.geometry(f"{width1}x{height1}")

width = StringVar()
height = StringVar()

Label(root,text="Enter the height and width",font="comicsansms 13 bold").grid(row=1,column=2)

Label(root,text="Enter width",font="comicsansms 9 bold",pady=4).grid(column=1,row=2)
Label(root,text="Enter width",font="comicsansms 9 bold",pady=4).grid(column=1,row=3)

Entry(root,text="Enter width",textvariable=width).grid(column=2,row=2)
Entry(root,text="Enter height",textvariable=height).grid(column=2,row=3)

b1 = Button(root,text="Resize",command=change_size,font="comiscansms 11 bold")
b1.grid(column=2,pady=10)

root.mainloop()