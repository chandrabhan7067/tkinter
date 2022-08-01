from tkinter import *
import os
from PIL import Image,ImageTk
from matplotlib import image

root = Tk()

root.geometry("500x600")
label = Label(text="Multipl images")
label.pack()

image1 = Image.open("chandrabhan.jpg")
image2 = Image.open("chandrabhan2.jpg")

photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)


label1 = Label(image=photo1)
label2 = Label(image=photo2)

label1.pack()
label2.pack()
root.mainloop()