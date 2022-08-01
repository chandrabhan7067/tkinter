from tkinter import *


def click(event):
    global scvariable
    text = event.widget.cget("text")

    if text == '=':
        if scvariable.get().isdigit():
            value = int(scvariable.get())
        else:
            try:
                value = eval(entry.get())

            except Exception as e:
                value = "Error"

        scvariable.set(value)
        entry.update()

    elif text == 'x':
        text = scvariable.get()[:-1]
        scvariable.set(text)
        entry.update()

    elif text == 'C':
        scvariable.set("")
        entry.update()

    else:
        scvariable.set(scvariable.get() + text)
        entry.update()


root = Tk()
root.geometry("330x590")
root.title("Calculator")
root.configure(background="light green")

scvariable = StringVar()
scvariable.set("")

entry = Entry(root, textvariable=scvariable, font="lucida 30 bold")
entry.pack(pady=10, fill=X)

f = Frame(root, bg="grey")

b = Button(f, text="C", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="%", font="lucida 25 bold")
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)

b = Button(f, text="x", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="/", font="lucida 25 bold")
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)

f.pack(pady=20)

f = Frame(root, bg="grey")

b = Button(f, text="7", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 25 bold")
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)

b = Button(f, text="9", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 25 bold")
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)

f.pack(pady=10)

f = Frame(root, bg="grey")

b = Button(f, text="4", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 25 bold")
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)


b = Button(f, text="6", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 25 bold")
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)

f.pack(pady=20)

f = Frame(root, bg="grey")

b = Button(f, text="1", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 25 bold")
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)


b = Button(f, text="3", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="lucida 25 bold")
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)

f.pack(pady=20)


f = Frame(root, bg="grey")

b = Button(f, text="00", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="0", font="lucida 25 bold")
b.pack(side=LEFT, padx=8)
b.bind("<Button-1>", click)


b = Button(f, text=".", font="lucida 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 25 bold")
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)

f.pack(pady=20)

statutasbar = StringVar()
statutasbar.set("Calculator")

root.mainloop()