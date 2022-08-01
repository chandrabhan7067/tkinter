from tkinter import *

root = Tk()

root.geometry("400x500")
root.title("My first GUI")
label_text = Label(text="Ready",bg="red",borderwidth=5,fg="white",padx=300,font="camicscansms 10 bold")
label_text.pack(side=BOTTOM,fill=X)

root.mainloop()