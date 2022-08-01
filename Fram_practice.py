from tkinter import *

from cv2 import getBuildInformation

root = Tk()
root.geometry("400x400")
f1 = Frame(bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)


f2 = Frame(bg="grey",borderwidth=6,relief=SUNKEN)
f2.pack(fill=X)

f3 = Frame(bg="grey",borderwidth=6,relief=SUNKEN)
f3.pack(side=BOTTOM,fill=X)

f4 = Frame(bg="grey",borderwidth=6,relief=SUNKEN)
f4.pack(side=RIGHT,fill=Y)

l1 = Label(f1,text="welcome")
l1.pack(pady=160)

l2 = Label(f2,text="welcome")
l2.pack()

l3 = Label(f3,text="welcome")
l3.pack()

l4 = Label(f4,text="welcome")
l4.pack(pady=130)

l5 = Label(text="sonality who works in Hindi films. In a film career spanning over thirty \nyears, Khan has received numerous awards, including two National Film Awards as a film producer, \nand two Filmfare Awards for acting.He is cited in the media as one of the most commercially \nsuccessful actors of Indian cinema.[4][5] Forbes included him in their 2015 list of \nTop-Paid 100 Celebrity Entertainers in the world; Khan tied with Amitabh Bachchan for No. \n71 on the list, both with earnings of $33.5 million.[6][7] According to the Forbes 2018 \nlis",fg="black",bg="red")
l5.pack(pady=50)

root.mainloop()