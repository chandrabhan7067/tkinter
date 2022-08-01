from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("400x400")

# var = IntVar()
var = StringVar()
var.set("radio")
def order():
    tmsg.showinfo("Order done",f"you ordered {var.get()} Its confirm")
    

Label(root,text="Hello sir ?",font="lucida 19 bold").pack()
radio = Radiobutton(root,variable=var,value="Smosa",text="Smosa").pack(anchor='w')
radio = Radiobutton(root,variable=var,value="chaumin",text="chaumin").pack(anchor='w')
radio = Radiobutton(root,variable=var,value="itli",text="itli").pack(anchor='w')
radio = Radiobutton(root,variable=var,value="dosa",text="dosa").pack(anchor='w')
Button(text="submit",command=order).pack(anchor="w")
root.mainloop()