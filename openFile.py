from tkinter import *
from tkinter import filedialog as fd
import os
from tkinter import messagebox as tsmg

root = Tk()
root.geometry("500x500")

TextArea = Text(root)
file = None
TextArea.pack(expand=True,fill=BOTH)

def open():
    # global file
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    file = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    # tsmg.showinfo(
    #     title='Selected File',
    #     message=filename
    # )
    
    root.title(os.path.basename(file) + "- Notepad")  
    TextArea.delete(1.0,END)
    f = open(file,"r")
    TextArea.insert(1.0,f.read())
    f.close()

Button(root,text="Open file",command=open).pack()

root.mainloop()