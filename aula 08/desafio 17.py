import math
catOps = float(input('Enter the value of the opposing cathetus: '))
catADJ = float(input('Enter the value of the adjacent cathetus: '))
hipo = math.hypot(catOps, catADJ)
print("The value of the hypotenuse is: {:.2f}".format(hipo))