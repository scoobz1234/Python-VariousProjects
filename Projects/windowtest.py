from tkinter import *
#defines the function show name later called with a button
def show_name():
    print("Hello",e1.get(),e2.get())
    e1.delete(0,END)
    e2.delete(0,END)
master = Tk()
master.configure(background="Black",bd=15)

#label for the first name entry window
Label(master, text="First Name",fg="Red",bg="Black").grid(row=0,column=0,)
#label for the last name entry window
Label(master, text="Last Name",fg="Red",bg="Black").grid(row=0,column=1)
#button to quit
Button(master, text="Exit", command=master.quit,highlightbackground="Black").grid(row=2,column=1)
#button to call the show name function
Button(master, text="Greet", command=show_name,highlightbackground="Black").grid(row=2,column=0)
#entry window for first name
e1 = Entry(master,bg="Black",relief=SUNKEN,fg="Blue")
#entry window for last Name
e2 = Entry(master,bg="Black",relief=SUNKEN,fg="Blue")
#tells the window where to place the first name entry box
e1.grid(row=1, column=0)
#tells the window where to place the last name entry box
e2.grid(row=1, column=1)

mainloop( )
