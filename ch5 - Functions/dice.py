#This program the rolling dice.

import random

MIN = 1
MAX = 6

def main():
    again = 'y'

    while again == 'y' or again == 'Y':
        print("Rolling the dice.......")
        print("First value: ")
        print(random.randint(MIN, MIN))
        print("The Second value: ")
        print(random.randint(MIN, MAX))

        again = input("Roll them again? (y = yes): ")


main()