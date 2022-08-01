from tkinter import *

root = Tk()
root.geometry("300x400")
scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)

# lbx = Listbox(root,yscrollcommand=scrollbar.set)
# for i in range(300):
#     lbx.insert(END,f"{i}")
# lbx.pack(fill=BOTH)
# scrollbar.config(command=lbx.yview)

#for notepad

text = Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

root.mainloop()