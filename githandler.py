"""GUI GIT Program"""

#   ***** IMPORTS *****
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from subprocess import call, Popen, PIPE
import os

#  ***** FUNCTIONS *****
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

#   ***** GUI *****
root = Tk()
root.wm_title("Git Handler")
root.geometry("200x200")


Button(root, text="Git Push", command=git_push, pady=10).pack(fill=X)
Button(root, text="Git Clone", command=git_clone, pady=10).pack(fill=X)
Button(root, text="Git Add/Commit", command=git_add, pady=10).pack(fill=X)
Button(root, text="Git Status", command=git_status, pady=10).pack(fill=X)
Button(root, text="Exit", command=root.quit, pady=10).pack(fill=X)

#   ***** Welcome Pop-up *****
messagebox.showinfo("Welcome","This is a program to automate your Git stuff!")

mainloop()
