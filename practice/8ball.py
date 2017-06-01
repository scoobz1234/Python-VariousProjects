import random

""" FUNCTIONS """

def no_response():
    mean_messages = ['It is not certain',
        'It is decidedly not',
        'no definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful']
#prints random item from the above list
    print(mean_messages[random.randint(0,len(mean_messages)-1)])

def yes_response():
    nice_messages = ['It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Looks like yes',
        'No need to ask again later, because its a definite Yes',
        'Abso-freaken-lutely',
        'My reply is yes',
        'Outlook is so good',
        'Very sure its a yes']
#prints random item from the above list
    print(nice_messages[random.randint(0,len(nice_messages)-1)])

def love_response():
    rude_messages = ['Nobody loves you, go away',
        'Definately not!',
        'Why on earth would someone like you?',
        'yeah...actually...NO',
        'you will die alone!']
#we dont like relationships...hahaha
    print(rude_messages[random.randint(0,len(rude_messages)-1)])

def boyorgirl_response():
    great_message = ["No,no,no,no and more no",
        "blah blah blah",
        "yeah, sure why not.",
        "not a chance."]
#no thanks..none of that lovey crap
    print(great_message[random.randint(0,len(great_message)-1)])

def decide_route():
    rando_number = random.randint(0,1000)
    list_of_strings = ['BOYFRIEND','GIRLFRIEND','BOY','GIRL']
    if "LOVE" in question_input:
        love_response()
    elif question_input in list_of_strings:
        boyorgirl_response()
    elif rando_number >=500:
        yes_response()
    else:
        no_response()

def main():
    global question_input
    question_input = input("What would you like to ask the great and powerful OZ?\n"+">>> ").upper()
    decide_route()

""" PROGRAM START """
while True:
    main()
