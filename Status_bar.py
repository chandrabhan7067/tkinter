from tkinter import *

root = Tk()
root.geometry("400x400")

def upload():
    statusvar.set("Wait for a while")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(anchor="w",textvariable=statusvar,relief=SUNKEN)
sbar.pack(side=BOTTOM,fill=X)

Button(root,text="upload",command=upload).pack()

root.mainloop()