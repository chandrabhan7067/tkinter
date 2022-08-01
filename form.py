from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("hello newWord")
root.configure(bg="pink")

a = Label(root,text="first name").grid(row=0,column=0)
b = Label(root,text="Last name").grid(row=1,column=0)
c = Label(root,text="college name").grid(row=2,column=0)

a1 = Entry(root)
a1.grid(row=0,column=1,padx=10)
b1 = Entry(root)
b1.grid(row=1,column=1,pady=10)
c1 = Entry(root).grid(row=2,column=1)

def complete():
    print("Your form is submit successfully")
    print(f"username is {a1.get()}")
    print(f"last name is {b1.get()}")

b = Button(root,text="submit",command=complete)
b.grid(pady=10)

root.mainloop()