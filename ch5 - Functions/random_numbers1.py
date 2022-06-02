# This program displays five function
# numbers in the range of 1 through 100.

import random

def main():
    for count in range(5):
        #Get the random numbers
        number = random.randint(1, 100)

        #dislay the number
        print(number)

#Call the main function
main()