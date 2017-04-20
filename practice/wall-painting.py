''' Find the cost of painting a wall '''

from time import sleep

# SETUP
coverage = int(400) #each paint can can cover 400 square feet

# INPUT
print ("What is the width of the wall?")
sleep (1)
width = input(">>> ") # gets input from user for the width of the wall
print ("What is the height of the wall?")
sleep (1)
height = input(">>> ") # gets input from user for the height of the wall
print ("How much does the paint cost per gallon?")
sleep (1)
cost = input(">>> ") # gets input from the user of the cost per gallon of paint

# TRANSFORM
width_C = float(width) if '.' in width else int(width) # converts the width input to a float or integer
height_C = float(height) if '.' in height else int(height) # converts the height input to a float or integer
cost_C = float(cost) if '.' in cost else int(cost) # converts the cost to float or integer
sqft = width_C * height_C # square footage of the wall
paint_Needed = sqft / coverage # find out how many cans you need
Cost_of_Job = paint_Needed * cost_C # multiplies how many cans you need by the cost per can

# OUTPUT
print ("Square footage:",sqft)
sleep (1)
print ("Cans of paint needed:",paint_Needed)
sleep (1)
print ("The cost of paint will be:",Cost_of_Job)
