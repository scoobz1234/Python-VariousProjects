from tkinter import *
from time import sleep

#defines the function show name later called with a button
def show_name():
    times= int(e3.get())
    for i in range(times):
        print("Hello",e1.get(),e2.get())
    Label(master, text="Check the Terminal!!!").grid(row=4,column=0)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

master = Tk()
master.wm_title("Name Repeater")

#label for the entries window
Label(master, text="First Name:").grid(row=0,column=0,)
Label(master, text="Last Name:").grid(row=1,column=0,)
Label(master, text="Times to Repeat").grid(row=2,column=0,)


#buttons to do stuff
Button(master, text="Exit", command=master.quit).grid(row=3,column=2)
Button(master, text="Go!", command=show_name).grid(row=3,column=0)
Button(master, text="Reset", command='').grid(row=3,column=1)
#entry windows for input
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

#tells the window where to place the first name entry box
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


mainloop( )
