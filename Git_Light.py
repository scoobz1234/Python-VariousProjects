"""       Lightweight GIT Program    """
# text wrap is reccomended, there are some long lines in this one....
# created by Stephen Ouellette 2017
# no key logging....yet..... :-P
# make sure you place this program in the directory you want to clone into IE desktop so it will become /Desktop/REPO
# and if you want to be able to push, add, and commit, you will need to place this file in the repo's main folder. /Desktop/Repo/Git_Light.py
"""       ***** IMPORTS *****        """

from subprocess import call, Popen, PIPE
import os
from time import sleep
#this just gets the terminal size so i can center text in it.
os.get_terminal_size()
os.get_terminal_size().columns

"""     ***** CLASSES *****       """
# this creates the colors class to make this all pretty in the console
class colors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

"""       ***** FUNCTIONS *****      """

def git_push():
# ask user for his/her username and repo name for the push.
# this might not work on a schoo computer, as i had to do a git config, on my personal comp.
    user_name = input("What's your UserName?\n>>> ")
    repo_name = input("What's your Repo's Name?\n>>> ")
# runs the git push command in terminal
    call('git push https://' + user_name + '@github.com/' + user_name + '/' + repo_name + '.git',shell=True)
    print("")
    print(colors.green,"********************************".center(os.get_terminal_size().columns),colors.endc)
    print(colors.bold,"*********PUSH COMPLETED*********".center(os.get_terminal_size().columns),colors.endc)
    print(colors.green,"********************************".center(os.get_terminal_size().columns),colors.endc)
    print("")
    print(colors.purple,"********************************".center(os.get_terminal_size().columns),colors.endc)

def git_clone():
# get the username and rep name for the git your going to clone from
    user_name = input("What's the Username?\n>>>  ")
    repo_name = input("What's the Repo's Name?\n>>> ")
# runs the git clone command in terminal
    call('git clone https://' + user_name + '@github.com/' + user_name + '/' + repo_name + '.git',shell=True)
    print("")
    print(colors.green,"********************************".center(os.get_terminal_size().columns),colors.endc)
    print(colors.bold,"********CLONE COMPLETED********".center(os.get_terminal_size().columns),colors.endc)
    print(colors.green,"********************************".center(os.get_terminal_size().columns),colors.endc)
    print("")
    print(colors.purple,"********************************".center(os.get_terminal_size().columns),colors.endc)

def git_status():
# runs the git status command in terminal
    call("git status",shell=True)
    print("")
    print(colors.purple,"********************************".center(os.get_terminal_size().columns),colors.endc)

def git_commit():
# runs the git commit command in terminal (note: this is using os.system because of an error call was causing for this command)
    os.system('git commit -m"gitHandler"')
    print("")
    print(colors.green,"********************************".center(os.get_terminal_size().columns),colors.endc)
    print(colors.bold,"********COMMIT COMPLETED********".center(os.get_terminal_size().columns),colors.endc)
    print(colors.green,"********************************".center(os.get_terminal_size().columns),colors.endc)
    print("")
    print(colors.purple,"********************************".center(os.get_terminal_size().columns),colors.endc)

def git_add():
# runs the git add command in terminal then runs the git_commit function.
    call("git add -A",shell=True)
    git_commit()

"""        ***** HOMEMADE SPLASH SCREEN *****     """

print("\n\n")
print(colors.red,"********************************".center(os.get_terminal_size().columns),colors.endc)
print(colors.bold,"Welcome to the Auto Git Handler!".center(os.get_terminal_size().columns),colors.endc)
print(colors.red,"********************************".center(os.get_terminal_size().columns),colors.endc)
print("\n\n")
sleep(1)
print(colors.red,"**********************************".center(os.get_terminal_size().columns),colors.endc)
print(colors.bold,"Created by: Stephen Ouellette 17'!".center(os.get_terminal_size().columns),colors.endc)
print(colors.red,"**********************************".center(os.get_terminal_size().columns),colors.endc)
print("\n\n")
sleep(3)
print("type",colors.yellow,"[Help]",colors.endc,"or",colors.yellow,"[H]",colors.endc,"at any time to get a list of commands!")

"""         ***** INPUT *****       """
#starts the program loop
# the colors.color sets the color of the text that follows it, and the colors.endc ends the color.
# it is possible to start colors.color on one print statement, and end it several prints later, however it spaces things out a little awkwardly
while True:
    print("\nyou have access to the following commands:\n\n",colors.yellow,"[Clone]","[Push]","[Status]","[Add_Commit]","[Exit]",colors.endc,"\n\nalternately try ",colors.yellow,"[C] [P] [S] [A] [E]",colors.endc,"respectively\n")
    user_command = str(input(">>> ")).upper()
#if the user types C or Clone it will call the git_clone function.
    if user_command == "CLONE" or user_command == "C":
        confirm = str(input("You have selected the Clone function, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or confirm == "YES":
            print(colors.purple,"********************************".center(os.get_terminal_size().columns),colors.endc)
            git_clone()
        else:
            continue
#if the user types S or Status it will call the git_status function.
    elif user_command == "STATUS" or user_command == "S":
        confirm = str(input("You have selected the Status command, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or confirm == "YES":
            print(colors.purple,"********************************".center(os.get_terminal_size().columns),colors.endc)
            git_status()
            continue
        else:
            continue
#if the user types P or Push it will call the git_push function.
    elif user_command == "PUSH" or user_command == "P":
        confirm = str(input("You have selected the Push command, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or confirm == "YES":
            print(colors.purple,"********************************".center(os.get_terminal_size().columns),colors.endc)
            git_push()
            continue
        else:
            continue
#if the user types A or Add_commit or Commit or Add it will call the git_add function
    elif user_command == "ADD_COMMIT" or user_command == "A" or user_command == "COMMIT":
        confirm = str(input("You have selected the Add/Commit command, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or confirm == "YES":
            print(colors.purple,"********************************".center(os.get_terminal_size().columns),colors.endc)
            git_add()
            continue
        else:
            continue
#if the user types H or Help it will list the commands.
    elif user_command == "HELP" or user_command == "H":
        while True:
            print("\n")
            print("Type any of the following commands:\n")
            print(colors.yellow,"[A]",colors.endc,"or",colors.yellow,"[ADD_Commit]",colors.endc,"------ runs the git add -A and git commit -m commands")
            print(colors.yellow,"[C]",colors.endc,"or",colors.yellow,"[Clone]",colors.endc,"----------- runs the git clone command")
            print(colors.yellow,"[E]",colors.endc,"or",colors.yellow,"[Exit]",colors.endc,"------------ runs the exit command (leaves the program)")
            print(colors.yellow,"[H]",colors.endc,"or",colors.yellow,"[Help]",colors.endc,"------------ runs the help command and lists these commands")
            print(colors.yellow,"[P]",colors.endc,"or",colors.yellow,"[Push]",colors.endc,"------------ runs the git push command in terminal")
            print(colors.yellow,"[S]",colors.endc,"or",colors.yellow,"[Status]",colors.endc,"---------- runs the git status command in terminal\n")
            press_enter_to_continue = input("Press",colors.yellow,"[Enter]",colors.endc,"to Continue...")
            print("")
            break
#if the user types E or Exit it will break the loop which will end the program.
    elif user_command == "EXIT" or user_command == "E":
        confirm = str(input("You have selected the Exit command, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or confirm == "YES":
            print(colors.red,"**********************************".center(os.get_terminal_size().columns),colors.endc)
            print(colors.bold,"Thanks for using Git Handler!!!!!!".center(os.get_terminal_size().columns),colors.endc)
            print(colors.red,"**********************************".center(os.get_terminal_size().columns),colors.endc)
            break
        else:
            continue
