                            """        Lightweight GIT Program          """

                            """       ***** IMPORTS *****        """
from subprocess import call, Popen, PIPE
import os
from time import sleep
                            """       ***** FUNCTIONS *****      """
def git_push():
# solicit input
    user_name = input("What's your UserName?\n>>> ")
    repo_name = input("What's your Repo's Name?\n>>> ")
# do stuff with the data
    call('git push https://' + user_name + '@github.com/' + user_name + '/' + repo_name + '.git',shell=True)
    print("\n********************************\n********PUSH COMPLETED********\n********************************\n")

def git_clone():
# solicit input
    user_name = input("What's the Username?\n>>>  ")
    repo_name = input("What's the Repo's Name?\n>>> ")
# do stuff with the data
    call('git clone https://' + user_name + '@github.com/' + user_name + '/' + repo_name + '.git',shell=True)
    print("\n********************************\n********CLONE COMPLETED********\n********************************\n")

def git_status():
    call("git status",shell=True)

def git_commit():
    os.system('git commit -m"gitHandler"')
    print("\n********************************\n********COMMIT COMPLETED********\n********************************\n")

def git_add():
    call("git add -A",shell=True)
    git_commit()

                            """        ***** INPUT *****     """

print("*****************************\nWelcome to the Auto Git Handler!\n*****************************\n\n")
print("******************************\nCreated by Stephen Ouellette 17'!\n******************************\n\n")
sleep(3)
print("type Help at any time to get a list of commands!\n")
while True:
    print("you have access to the following commands:\n\n[Clone]","[Push]","[Status]","[Add_Commit]","[Exit]\n\nalternatly try [C][P][S][A][E] respectivly\n")
    user_command = str(input(">>> ")).upper()

    if user_command == "CLONE" or user_command == "C":
        confirm = str(input("You have selected the Clone function, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            git_clone()
        else:
            continue

    elif user_command == "STATUS" or user_command == "S":
        confirm = str(input("You have selected the Status command, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            git_status()
            continue
        else:
            continue

    elif user_command == "PUSH" or user_command == "P":
        confirm = str(input("You have selected the Push command, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            git_push()
            continue
        else:
            continue

    elif user_command == "ADD_COMMIT" or user_command == "A" or user_command == "COMMIT":
        confirm = str(input("You have selected the Add/Commit command, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            git_add()
            continue
        else:
            continue

    elif user_command == "EXIT" or user_command == "E":
        confirm = str(input("You have selected the Exit command, are you sure?\n(Y/N)\n>>> ")).upper()
        if confirm == "Y" or "YES":
            break
        else:
            continue
