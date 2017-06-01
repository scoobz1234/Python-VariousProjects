"""This program will convert 1-99 numbers to English words"""
import math # this is so we can use the math.floor function.
while True:
    number = int(input("Enter a number 1-99 to print: "))
#ones list
    ones_list = ['zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
# teens list
    teens_list = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
# Tens list
    tens_list = ['Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
# Hundreds list
    hundreds_list = ['One Hundred','Two Hundred','Three Hundred','Four Hundred','Five Hundred','Six Hundred','Seven Hundred','Eight Hundred','Nine Hundred']

    if number <= 9: # if the number is lass than 9
        print(ones_list[number]) # print the number from the list above according to its place value
    elif number >= 10 and number <= 19: # if the number is between 10 and 19
        tens = number % 10 # converts the number you put to a 1-9 so you can use it to find the list location
        print(teens_list[tens]) # print the number from the teens list according to its number place
    elif number > 19 and number <= 99: # if the number is between 19 and 99
        ones = math.floor(number/10) # divide the number to get its ones place, and because its not always even we take the floor of the number
        twos = ones - 2 # take the ones and subtract two from it.
        tens = number % 10 # converts the 10 to the 1-9 number so we can get its location from the tens list
        if tens == 0: # if tens is 0 then we just print from the tens list because there isnt a following number. 20,30 ect.
            print(tens_list[twos]) # print from the tens list with the twos location number
        elif tens != 0: # if tens is not equal to 0 so there is a 1-9 after the first place I.E 21
            print(tens_list[twos] + "-" + ones_list[tens]) # print from tens list using twos, and then number from ones list.
    elif number > 99 and number <=999:
        ones = math.floor(number/10)
        twos = ones -2
        tens = number % 10
        hundreds = number % 100
        if hundreds == 0: # if tens is 0 then we just print from the tens list because there isnt a following number. 20,30 ect.
            print(tens_list[twos] + "-" + ones_list[tens]) # print from the tens list with the twos location number
        elif hundreds != 0: # if tens is not equal to 0 so there is a 1-9 after the first place I.E 21
            print(hundreds_list[hundreds] + tens_list[twos] + "-" + ones_list[tens]) # print from tens list using twos, and then number from ones list.
    else:
        print ("Didn't I say 1-99? ...")
        continue

    odd_even = number % 2 # if its even its a 0 else its odd!
    if odd_even == 0: # if even its a 0
        print("Thats an even Number!")
    else: # else its odd!
        print("Thats an odd Number!")

    print ('To Continue type (Y) to exit type (N)')
    cont = input ('>>>')
    cont_upper = cont.upper() # makes whatever the user enters uppercase
    if cont_upper != "Y": # if its not a Y then it will break
        break
    else:
        continue
