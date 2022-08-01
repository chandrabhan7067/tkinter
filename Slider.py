from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("300x400")
root.title("Slider tutorial")

def getrupp():
    tmsg.showinfo("Amount",f"{slider2.get()}ruppes is send to tour account")
    

# slider1 = Scale(root,from_ = 10, to = 100)
# slider1.pack()

Label(root,text='How many ruppes do you want')
slider2 = Scale(root,from_ = 0, to = 100,orient=HORIZONTAL,tickinterval=50)
slider2.set(20)
slider2.pack()
Button(root,text="submit!",command=getrupp).pack(pady=10)


root,mainloop()