'''this is a program that checks if your a vampire and gets your age'''
'''setup'''
import datetime
now = datetime.datetime.now() #sets the date and time to the now variable
year = now.year # gets the year, for use later

'''input'''

print ('Are you a Vampire?')

while True: #loop start for the question
    vampire = input(">>> ")
    vamp_up = vampire.upper() # makes the vampire variable all uppercase

    if vamp_up == "YES":
        print ("Outstanding!")
        break # this stops the loop

    else:
        print ("for real though... not a Vampire? Get outta here!")
        exit() # put this in here so people dont think i have a bug infinite loop, even though i really didnt want it here...

print ("How old are you?")
age = int(input(">>> ")) #takes user input and makes it an integer

if age >= 100 and age <=999: # if age is greater than 99 and less than 10000
    born = str(year - age)# takes year and subtracts your age from it
    print("WOW! You were born in " + born + "!")

elif age >= 1000 and age <= 9999:# if age is greater than 999 and less than 10000
    born = str(year - age)# takes year and subtracts your age from it
    print("Wow, you are super old! " + born + " was your birth year!!")

elif age >= 10000:# if your age is greater than 10000
    born = str(year - age)
    print ("dude...seriously.. how many people have you killed?")
    killed = int(input(">>> ")) # takes user input converts to integer

    if killed >= 1000: # if killed greater than 999
        print (killedstr , "! that many? Nice!")

    elif killed <= 999:
        print ("Weak sauce, come back when your in the big leagues...")

elif age < 100:
    print ("Bro, not even a Vampire..")
    #end
