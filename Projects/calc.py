from tkinter import *
from math import *

def evaluate(event):
    res.configure(text = "Answer: " + str(eval(entry.get())))
w = Tk()
Label(w, text="Your Calculation:").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()
