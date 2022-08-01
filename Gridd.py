from tkinter import *

def getvals():
    with open("new.txt","a") as f:
        f.write(f"the name of user is:{uservalue.get()}\n")
        f.write(f"The value of password is: {passvalue.get()}\n")

root = Tk()

root.geometry("500x500")

user = Label(root,text="username")
password = Label(root,text="password")

user.grid()
password.grid()

# variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="submit",command=getvals).grid()

root.mainloop()
