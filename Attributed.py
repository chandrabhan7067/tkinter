from tkinter import *
from turtle import left
#opecity
root = Tk()

root.geometry("400x400")
root.title("My GUI")

# label options
# text = adds the text
# bg = background
# fg = foreground text color
# font = sets the font
#1 font="comicsansms 19 bold"
#2 font=("comicsansms",19,"bold")

# padx = padding x
# pady = padding y
# relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE


title_label = Label(text='''Abdul Rashid Salim Salman Khan is an Indian actor, film producer, \nand television personality who works in Hindi films. In a film career spanning over thirty \nyears, Khan has received numerous awards, including two National Film Awards as a film producer, \nand two Filmfare Awards for acting.He is cited in the media as one of the most commercially \nsuccessful actors of Indian cinema.[4][5] Forbes included him in their 2015 list of \nTop-Paid 100 Celebrity Entertainers in the world; Khan tied with Amitabh Bachchan for No. \n71 on the list, both with earnings of $33.5 million.[6][7] According to the Forbes 2018 \nlist of Top-Paid 100 Celebrity Entertainers in world, Khan was the highest-rank''',bg = 'red',fg="black",padx=10,pady=10,font="comicsansms 9 bold",
borderwidth=3,relief=SUNKEN)

# pack options
#anchor = nw and many other
#side = top, bottom, left, right
# fill
# padx
# pady


# title_label.pack(side= BOTTOM)
# title_label.pack(side= BOTTOM,anchor="se")
# title_label.pack(side= BOTTOM,anchor="se",fill=X)
# title_label.pack(side= LEFT,fill=Y)
title_label.pack(side= LEFT,fill=Y,padx=30,pady=30)

# pack options

root.mainloop()
