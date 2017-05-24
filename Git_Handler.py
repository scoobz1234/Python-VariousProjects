""" GUI GIT Program """

"""   ***** IMPORTS *****   """

import os
from tkinter import *
import tkinter
from tkinter import simpledialog, messagebox
from subprocess import call, Popen, PIPE

"""  ***** FUNCTIONS *****  """

def exit_prompt():
    exit_prompt = messagebox.askquestion("Quit","Do you want to quit?",icon="warning")
    if exit_prompt == 'yes':
        print ("Thanks for using Git Handler")
        quit()
    else:
        print ("Please Continue")

def git_push():
# solicit input
    user_name = simpledialog.askstring("Username:","What is your username?")
    repo_name = simpledialog.askstring("Repo Name","What's your Repo's Name?")
# let them know they gotta put in their password(until i figure this part out)
    messagebox.showinfo("Password","Please enter your Password in the Terminal")
# do stuff with the data
    call('git push https://' + user_name + '@github.com/' + user_name + '/' + repo_name + '.git',shell=True)
    exit_prompt()

def git_clone():
# solicit input
    user_name = simpledialog.askstring("Username:","What is your username?")
    repo_name = simpledialog.askstring("Repo Name","What's your Repo's Name?")
# do stuff with the data
    call('git clone https://' + user_name + '@github.com/' + user_name + '/' + repo_name + '.git',shell=True)
    exit_prompt()

def git_status():
    call("git status",shell=True)
    messagebox.showinfo("Status","Check the Terminal!")
    exit_prompt()

def git_commit():
    os.system('git commit -m"gitHandler"')
    exit_prompt()

def git_add():
    call("git add -A",shell=True)
    git_commit()

def git_create():
    create_window = Toplevel(root)
    create_window.wm_title("Create Git Repo")
    w = 200
    h = 200
    ws = create_window.winfo_screenwidth()
    hs = create_window.winfo_screenheight()
    x = (ws/1.6) - (w/1.6)
    y = (hs/2) - (h/2)
    create_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#buttons to do stuff! pady give us bigger buttons and fill x fills from left and right.
    push = Button(create_window, text="Git Create", command=git_push, pady=10).pack(fill=X)
    clone = Button(create_window, text="Git Init", command=git_clone, pady=10).pack(fill=X)
    commit = Button(create_window, text="stuff", command=git_add, pady=10).pack(fill=X)

"""   ***** GUI *****   """
#   ***** Welcome Pop-up *****
messagebox.showinfo("Welcome","This is a program to automate your Git stuff!")

#main window
root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.wm_title("Git Handler")
w = 200
h = 200
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#file menu cascade drop down tearoff = 0 makes it so the cascade menus cant be removed.
file_menu = Menu(menu,tearoff = 0)
menu.add_cascade(label="New", menu=file_menu)
file_menu.add_command(label="New Repository..", command=git_create)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#edit menu cascade drop down
edit_menu = Menu(menu,tearoff = 0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Test Menu",command=git_status)

#buttons to do stuff! pady give us bigger buttons and fill x fills from left and right.
push = Button(root, text="Git Push", command=git_push, pady=10).pack(fill=X)
clone = Button(root, text="Git Clone", command=git_clone, pady=10).pack(fill=X)
commit = Button(root, text="Git Add/Commit", command=git_add, pady=10).pack(fill=X)
status = Button(root, text="Git Status", command=git_status, pady=10).pack(fill=X)
exit = Button(root, text="Exit", command=root.quit, pady=10).pack(fill=X)

root.mainloop()
