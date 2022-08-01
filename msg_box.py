from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("500x500")

def myfun():
    print("yes its working")

def helpyou():
    print("i will help you")
    tmsg.showinfo("help","Chandrabhan will help you please contact 7067803966")

def rateus():
    print("yes its work")
    value = tmsg.askquestion("was your experience good", "was your experience good")
    if value == 'yes':
        msg = "please rate us on playstore"
    else:
        msg = "tell us what was wrong"
    tmsg.showinfo("Experience",msg)

def divya():
    ans = tmsg.askretrycancel("divya ke dost bn ja","soory divya ka bf h phle se")
    if ans:
        print("retry krne pr bhi nhi bnegi")
    else:
        print("skt ldke")

mainmenu = Menu(root)
filemenu = Menu(mainmenu,tearoff=0)
filemenu.add_command(label="rename",command=myfun)
filemenu.add_command(label="edit",command=myfun)
filemenu.add_command(label="open",command=myfun)
filemenu.add_command(label="view",command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(menu = filemenu,label="file")


filemenu2 = Menu(mainmenu,tearoff=0)
filemenu2.add_command(label="copy",command=myfun)
filemenu2.add_command(label="paste",command=myfun)
filemenu2.add_command(label="cut",command=myfun)
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = filemenu2,label="edit")

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="help",command=helpyou)
m3.add_command(label="Rate",command=rateus)
m3.add_command(label="befrienddivya",command=divya)
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = m3,label="Help")


root.mainloop()