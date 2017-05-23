"""GUI GIT Program"""

#   ***** IMPORTS *****
from subprocess import call, Popen, PIPE
import os

#  ***** FUNCTIONS *****
def git_push():
# solicit input
    print("Whats your Username?")
    user_name = input(">>> ")
    print("Whats your Repo's Name?")
    repo_name = input(">>> ")
# do stuff with the data
    call('git push https://' + user_name + '@github.com/' + user_name + '/' + repo_name + '.git',shell=True)
    print("********************************")
    print(" ********PUSH COMPLETED********")
    print("********************************")

def git_clone():
# solicit input
    # print("Whats the Username?")
    user_name = input("What's the Username?\n>>>  ")
    # print("Whats the Repo's Name?")
    repo_name = input("What's the Repo's Name?\n>>> ")
# do stuff with the data
    call('git clone https://' + user_name + '@github.com/' + user_name + '/' + repo_name + '.git',shell=True)
    print("********************************\n********CLONE COMPLETED********\n********************************\n")

def git_status():
    call("git status",shell=True)

def git_commit():
    os.system('git commit -m"gitHandler"')
    print("********************************\n********COMMIT COMPLETED********\n********************************\n")
    # print(" ********COMMIT COMPLETED******")
    # print("********************************\n")

def git_add():
    call("git add -A",shell=True)
    git_commit()

#   ***** SETUP *****

print("Welcome to Stephen's Git Handler!")
print("type Help at any time to get a list of commands!\n")
while True:
    print("you have access to the following commands:\n\n[Clone]","[Push]","[Status]","[Add_Commit]","[Exit]\n\nalternatly try [C][P][S][A][E] respectivly\n")
    user_command = str(input(">>> ")).upper()

    if user_command == "CLONE" or user_command == "C":
        print("You have selected the Clone function, are you sure?")
        confirm = str(input("(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            git_clone()
        else:
            continue

    elif user_command == "STATUS" or user_command == "S":
        print("You have selected the Status command, are you sure?")
        confirm = str(input("(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            git_status()
            continue
        else:
            continue

    elif user_command == "PUSH" or user_command == "P":
        print("You have selected the Push command, are you sure?")
        confirm = str(input("(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            git_push()
            continue
        else:
            continue

    elif user_command == "ADD_COMMIT" or user_command == "A" or user_command == "COMMIT":
        print("You have selected the Commit command, are you sure?")
        confirm = str(input("(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            git_add()
            continue
        else:
            continue

    elif user_command == "EXIT" or user_command == "E":
        print("You have selected the Exit command, are you sure?")
        confirm = str(input("(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            break
        else:
            continue
