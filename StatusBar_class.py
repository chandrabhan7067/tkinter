from tkinter import*
from tkinter import messagebox as tsmg

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Class and GUI")
    
    def StatusBar(self):
        self.var = StringVar()
        self.var.set("Ready")

        self.stb = Label(self, textvariable=self.var,relief=SUNKEN,anchor="w")
        self.stb.pack(side=BOTTOM,fill=X)

    def applyed(self):
        tsmg.showinfo("from ditails","Form is submitted")        
        
    def createrButton(self):
        Button(self,text="Apply",command=self.applyed).pack()

    def createFrame(self):
        Frame(self,bg="grey",borderwidth=8, relief=SUNKEN).pack(side=RIGHT,fill=Y)

window = GUI()
window.StatusBar()
window.createFrame()
# window.createrButton()
window.mainloop()
