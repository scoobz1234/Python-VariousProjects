"""This program will convert 1-9999 numbers to English words"""
import math # this is so we can use the math.floor function.
import os
os.get_terminal_size()
os.get_terminal_size().columns

""" CLASS """

class colors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

""" LISTS """
#ones list
ones_list = ['zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
# teens list
teens_list = ['zero','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
# Tens list
tens_list = ['zero','Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
# Hundreds list
hundreds_list = ['zero','One Hundred','Two Hundred','Three Hundred','Four Hundred','Five Hundred','Six Hundred','Seven Hundred','Eight Hundred','Nine Hundred']
# Thousands list
thousands_list = ['zero','One Thousand','Two Thousand','Three Thousand','Four Thousand','Five Thousand','Six Thousand','Seven Thousand','Eight Thousand','Nine Thousand']

""" FUNCTIONS """
# checks what the locations of the numbers are so we can call the right function
def check():
    if len(user_input) >3 and len(user_input) <=4:
        thousands()
    elif len(user_input) >2 and len(user_input) <=3:
        hundreds()
    elif len(user_input) >1 and len(user_input) <=2:
        tens()
    elif len(user_input) >0 and len(user_input) <2:
        ones()

# prints a number in the thousands
def thousands():
    first_digit = int(user_input[0])
    second_digit = int(user_input[1])
    third_digit = int(user_input[2])
    fourth_digit = int(user_input[3])
    if third_digit == 1:
        location_of_digit = third_digit + fourth_digit
        print(colors.red,"********************************",colors.endc)
        print (thousands_list[first_digit],hundreds_list[second_digit],teens_list[location_of_digit])
        print(colors.red,"********************************",colors.endc)

    elif third_digit >1:
        third_digit = int(user_input[1])
        print(colors.red,"********************************",colors.endc)
        print (thousands_list[first_digit],hundreds_list[second_digit],tens_list[third_digit],ones_list[fourth_digit])
        print(colors.red,"********************************",colors.endc)

#prints a number in the hundreds
def hundreds():
    first_digit = int(user_input[0])
    second_digit = int(user_input[1])
    third_digit = int(user_input[2])
    if second_digit == 1:
        location_of_digit = second_digit + third_digit
        print(colors.red,"********************************",colors.endc)
        print (hundreds_list[first_digit],teens_list[location_of_digit])
        print(colors.red,"********************************",colors.endc)
    elif second_digit >1:
        second_digit = int(user_input[1])-1
        print(colors.red,"********************************",colors.endc)
        print (hundreds_list[first_digit],tens_list[second_digit],ones_list[third_digit])
        print(colors.red,"********************************",colors.endc)

#prints a number in the tens
def tens():
    first_digit = int(user_input[0])
    second_digit = int(user_input[1])
    location_of_digit = first_digit + second_digit
    print(colors.red,"********************************",colors.endc)
    print (teens_list[location_of_digit])
    print(colors.red,"********************************",colors.endc)

#prints a number in the ones
def ones():
    first_digit = int(user_input[0])
    print(colors.red,"********************************",colors.endc)
    print(ones_list[first_digit])
    print(colors.red,"********************************",colors.endc)


""" INPUT """
# get the user input for what number to convert
def main():
    global user_input
    user_input = input("Enter a number 1-9999 to print: ")
    if user_input[0] == "0" and user_input [1] == "0":
        user_input = user_input[2:]
    elif user_input[0] == "0":
        user_input = user_input[1:]
    check()

while True:
    main()
