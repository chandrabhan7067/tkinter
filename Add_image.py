from tkinter import *
from PIL import Image,ImageTk

root = Tk()

root.geometry("400x600")
# photo = PhotoImage(file="chandrabhan.png")

# for jpg images
image = Image.open("chandrabhan.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.pack()

root.mainloop()