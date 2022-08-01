from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("1000x800")

def every_100(text):
    temp = ""
    for i in range (0,len(text)):
        temp += text[i]
        if i%100 == 0 and i != 0:
            temp += "\n"
    return temp

texts = []
photos = []

for i in range(0,2):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
    image = Image.open(f"{i+1}.jpg")
    
    image = image.resize((250,225))
    
    photos.append(ImageTk.PhotoImage(image))
    
f0 = Frame(root, width=800,height=70)
Label(f0,text="Today news",font="lucida 33 bold").pack()
Label(f0,text="july 3, 2022",font="lucida 13 bold").pack()
f0.pack()

# f1 = Frame(root,width=900,height=200)
# Label(f1,text=texts[0],pady=20,padx=10).pack(side="left")
# Label(f1,image=photos[0],anchor="e").pack(pady=20,padx=10)
# f1.pack(anchor="w")

# f2 = Frame(root,width=900,height=200)
# Label(f2,text=texts[1],pady=20,padx=10).pack(side="right")
# Label(f2,image=photos[1],pady=20).pack(pady=20,padx=10)
# f2.pack(anchor="w")

for i in range(0,2):
    f1 = Frame(root,width=900,height=200)
    Label(f1,text=texts[i],pady=20,padx=10).pack(side="left")
    Label(f1,image=photos[i],anchor="e").pack(pady=20,padx=10)
    f1.pack(anchor="w")

root.mainloop()