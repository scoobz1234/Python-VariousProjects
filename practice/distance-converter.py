''' This program will convert Volume and Distances between Metric and US measurements '''
# get sleep function from the time library
from time import sleep

def inches_to_feet():
    cnvt1 = num1 / 12
    print("Converting",num1,unit1,"to Feet:","your answer is",cnvt1,"feet")
def feet_to_feet():
    print("Converting",num1,unit1,"to Feet:","your answer is",cnvt1,"feet")
def miles_to_feet():
    cnvt1 = num1 * 5280
    print("Converting",num1,unit1,"to Feet:","your answer is",cnvt1,"feet")
def feet_to_miles():
    cnvt1 = num1 / 5280
    print("Converting",num1,unit1,"to Miles:","your answer is",cnvt1,"Mile")
def feet_to_inches():
    cnvt1 = num1 * 12
    print("Converting",num1,unit1,"to Inches:","your answer is",cnvt1,"inches")
def miles_to_kilo():
    cnvt1 = num1 * 1.60934
    print("Converting",num1,unit1,"to Kilometers:","your answer is",cnvt1,"kilometers")
def kilo_to_miles():
    cnvt1 = num1 / 1.60934
    print("Converting",num1,unit1,"to Miles:","your answer is",cnvt1,"Miles")
def kilo_to_feet():
    cnvt1 = num1 * 3280.84
    print("Converting",num1,unit1,"to Feet:","your answer is",cnvt1,"Feet")
def kilo_to_inches():
    cnvt1 = num1 * 39370.1
    print("Converting",num1,unit1,"to Inches:","your answer is",cnvt1,"Inches")


'''setup'''
print("What unit are you converting from?","in,ft,mi,km")
unit1 = input()
print("What is the number?")
num1= int(input())
print("What are you converting to?",'in,ft,mi,km')
unit2 = input()
if unit1== "in" and unit2== "ft" :
    unit1 = "Inches"
    inches_to_feet()
elif unit1== "ft" and unit2 =="ft":
    unit1= "Feet"
    feet_to_feet()
elif unit1=="mi" and unit2 =="ft":
    unit1= "Miles"
    miles_to_feet()
elif unit1=="ft" and unit2 =="mi":
    unit1= "Feet"
    feet_to_miles()
elif unit1=="ft" and unit2 =="in":
    unit1= "Feet"
    feet_to_inches()
elif unit1=="mi" and unit2 =="km":
    unit1= "Miles"
    miles_to_kilo()
elif unit1=="km" and unit2 =="mi":
    unit1= "Kilometers"
    kilo_to_miles()
elif unit1=="km" and unit2 =="in":
    unit1= "Kilometers"
    kilo_to_inches()
elif unit1=="km" and unit2 =="ft":
    unit1= "Kilometers"
    kilo_to_feet()
