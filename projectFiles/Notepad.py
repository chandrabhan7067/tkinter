from tkinter import messagebox as tmsg
import os
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files,","*.*"),("Text Documents","*.txt")])

    if file == "":
        file = None
    
    else:
        root.title(os.path.basename(file) + "- Notepad")  
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    # pass
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files,","*.*"),("Text Documents","*.txt")])

        if file == "":
            file = None
        else:
            # save file as new file
            f = open(file,'w')      
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file + "-Notepad"))
    else:
        # save the file
        f = open(file,'w')      
        f.write(TextArea.get(1.0,END))
        f.close()

def quitFile():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")


def copy():
    TextArea.event_generate("<<Copy>>")


def paste():
    TextArea.event_generate("<<Paste>>")


def about():
    tmsg.showinfo("Notepad About","Note pad by chandrabhan bahetwar")

root = Tk()
root.title("Untiteld menubar")
root.geometry("500x500")


TextArea = Text(root,font="lucida 10")
file = None
TextArea.pack(expand=True,fill=BOTH)


menuBar = Menu(root)

filemenu = Menu(menuBar,tearoff=0)

#To open new file
filemenu.add_command(label="New", command = newFile)

# To save already existing file

filemenu.add_command(label="Open", command=openFile)

# To save the curren file

filemenu.add_command(label="Save",command=saveFile)

filemenu.add_separator()

filemenu.add_command(label="Exit",command=quitFile)

menuBar.add_cascade(label="File",menu=filemenu)


# Edit menu

editmenu = Menu(menuBar,tearoff=0)

# To cur copy and paste the word 
# Edit menu start

editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)

# Edit menu end
menuBar.add_cascade(label="Edit",menu = editmenu)

# Help Menu

Helpbar = Menu(menuBar,tearoff=0)
Helpbar.add_command(label="About Notepad",command=about)

menuBar.add_cascade(label="Help",menu = Helpbar)

root.configure(menu=menuBar)

# scroll bar 

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()