from tkinter import *
from turtle import color

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width,height=canvas_height)
can_widget.pack()
can_widget.create_line(0,0,400,400,fill="red")

can_widget.create_rectangle(300,150,500,300,fill="red")

can_widget.create_text(400,220,text="Tkinter")

can_widget.create_oval(505,140,700,305,fill="green")

root.mainloop()
