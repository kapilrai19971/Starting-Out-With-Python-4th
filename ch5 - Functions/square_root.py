#This program demonstrates the sqrt function

import math


def sqr_root():
    #Get a number
    number = float(input("Enter a number: "))

    #Get square root of the number
    square_root = math.sqrt(number)

    #Display the square root
    print('The square root of',number,' is ',square_root)


sqr_root()
