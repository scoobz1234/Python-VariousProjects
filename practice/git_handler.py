#!/usr/bin/python
import tkinter
import subprocess

from tkinter import messagebox
from tkinter import *
root = Tk()
class HackBar:

  def __init__(self,master):

      frame=Frame(master,width = 600,height = 250)
      #frame.pack()

      def printconsole(event):
          print("Exit")
          quit()
      def retrieve_input(event):
          input = self.Text.get("1.0",'end-1c')
          #print(input)
          #subprocess.call(input,shell=TRUE)
          subprocess.Popen(input)
          #root.quit()
          #root = Tk()
          #print p.communicate()

      self.button1 = Button(root,text = "Execute")
      self.button1.bind("<Button-1>",retrieve_input);
      self.button1.grid(row = 0,sticky = E)

      self.button2 = Button(root,text = "  Quit   ",command = master.quit)
      self.button2.bind("<Button-1>",printconsole);
      self.button2.grid(row = 1,sticky = E)

      self.Text = Text(root,height =4)
      self.Text.grid(row = 0,column = 1,rowspan=2)

menu = Menu(root)
def AboutDialog():
    messagebox.showinfo('About','For any issues or suggestion contact rushic24@gmail.com ')
root.config(menu = menu)
submenu1 = Menu(menu)
menu.add_cascade(label="Help",menu=submenu1)
submenu1.add_command(label = "About",command = AboutDialog)

b = HackBar(root)
root.mainloop()
