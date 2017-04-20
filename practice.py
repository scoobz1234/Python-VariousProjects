from time import sleep
''' the above statement imports the sleep function '''

# Name & Age
print ("Whats your name?")
name = input(">>> ") # requests input from user for their name
sleep (1)
print ("How old are you?")
age = input(">>> ") # requests input from user for their age
sleep (1)
print ("Damn " + name + ", " + age + " years old! " + " Okay grandpa...")
sleep (1)
print ("In one year you will be...")
sleep (1)
print ("...")
sleep (1)
print (int(age) + 1) # adds a year to the users age
sleep (2)

''' Math Fun '''

# INPUT
while True: # while loop so you can keep doing math
    print ("Next we'll do some math!")
    sleep (1)
    print ("First Number")
    number_1 = input(">>> ") # requests input from user for the first number in their math problem
    sleep (1)
    print ("Next what operator? + or -")
    operator_1 = input (">>> ") # requests input from user for the operator + or -
    sleep (1)
    print ("Second Number")
    number_2 = input (">>> ") # requests input from user for the second number of their math problem
    sleep (1)

# TRANSFORM
    convert_1 = float(number_1) if '.' in number_1 else int(number_1) # converts inputted number to a float or a integer
    convert_2 = float(number_2) if '.' in number_2 else int(number_2) # converts inputted number to a float or a integer

# OUTPUT
    if operator_1 == '+':
        sleep (1)
        print ("...")
        sleep (1)
        answer = (convert_1) + (convert_2)
        print ('Your answer is: ' + str(answer))
        sleep (2)
        quit_app = input("Want to continue?: (y/n): ")
    elif operator_1 == "-":
        sleep (1)
        print ("...")
        sleep (1)
        answer = (convert_1) - (convert_2)
        print ("Your answer is : " + str(answer))
        sleep (2)
        quit_app = input("Want to continue?: (y/n): ")
    else:
        print ("Unknown Operator! Try Again.")
        sleep (2)
        quit_app = input("Want to continue?: (y/n): ")

    if quit_app == "n":
        break
    else:
        continue
