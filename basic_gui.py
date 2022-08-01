from tkinter import *

#for creting a basic gui screen
root = Tk()

# logic for gui qualities

# width x height
#set starting width and height of gui
root.geometry('644x434')


# width, height
root.minsize(400,200)

# width, height
root.maxsize(1000,600);

textInGui = Label(text="This is my first GUI and i am so happy after creating this GUI")
textInGui.pack()

#for creting a basic gui screen
root.mainloop()
