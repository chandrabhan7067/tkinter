from tkinter import*

from matplotlib.pyplot import pink, text

root = Tk() 

root.title("just try to make a travelling form")
root.geometry("430x280")
root.configure(bg="pink")

Label(root,text="welcome to chandu Travels", font="comicsansms 13 bold",pady=15,bg="pink").grid(row=0,column=3)

name = Label(root,text="name",bg="pink",font="comicsansms 9 bold")
phone = Label(root,text="phone number",bg="pink",font="comicsansms 9 bold")
gender = Label(root,text="gender",bg="pink",font="comicsansms 9 bold")
gmail= Label(root,text="gmail",bg="pink",font="comicsansms 9 bold")
pymentMode = Label(root,text="pyment mode",bg="pink",font="comicsansms 9 bold")

name.grid(row=1 , column=2,pady=2,padx=7)
phone.grid(row= 2, column=2,pady=2,padx=7)
gender.grid(row= 3, column=2,pady=2,padx=7)
gmail.grid(row= 4, column=2,pady=2,padx=7)
pymentMode.grid(row= 5, column=2,pady=2,padx=7)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
gmailvalue = StringVar()
pymentvalue = StringVar()
checkboxvalue = IntVar()

nameentry = Entry(root,textvariable=namevalue)
phoneentry = Entry(root,textvariable=phonevalue)
genderentry = Entry(root,textvariable=gendervalue)
gmailentry = Entry(root,textvariable=gmailvalue)
pymententry = Entry(root,textvariable=pymentvalue)

nameentry.grid(row= 1, column=3,pady=2)
phoneentry.grid(row= 2, column=3,pady=2)
genderentry.grid(row= 3, column=3,pady=2)
gmailentry.grid(row= 4, column=3,pady=2)
pymententry.grid(row= 5, column=3,pady=2)

# check button
checkboxbutton = Checkbutton(root,text="want to order food",variable=checkboxvalue,font="comicsansms 9 bold")
checkboxbutton.grid(row=6,column=3)

def getval():
    print('submited !')
    with open("record.txt","a") as f:
        f.write(f"{namevalue.get()}, {phonevalue.get()}, {gendervalue.get()}, {gmailvalue.get()}, {pymentvalue.get()} {checkboxvalue.get()}\n")

Button(root,text=" submit ",pady=3,fg="blue",command=getval).grid(row=7,column=2,pady=3)

root.mainloop()