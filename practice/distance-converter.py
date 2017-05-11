''' This program will convert Volume and Distances between Metric and US measurements '''
# get sleep function from the time library
from time import sleep
import math
'''setup'''
unit_list = ['in','ft',]
print('Please enter a number')
num1 = float(input(">>> "))
while True:
    print('Please enter the unit you are converting from')
    print('in, ft, mi, cm, m, km')
    try:
        unit1 = input('>>> ')
        if unit1 == unit_list:
            break
        else:
            print ('Oops, that wasnt on the list! Try again...')
    except:
        print: ("That's not in the list")
