#This program calculates the length of a right angle triangle's hypotenuse.
import math


def hypoten():
    #Get the length of the triangle's two sides.
    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))

    #Calculate the length of the hypotenuse.
    c = math.hypot(a, b)

    #Display the lenth of the hypotenuse.
    print('The length of the hypotenuse is', format(c,',.2f'))


hypoten()