#This program converts cups to fluids ounces.

def main():
    cups_needed = int(input("Enter the numbers of cups: "))

    cups_to_ounces(cups_needed)


def intro():
    print("This program converts measurements")
    print("in cups to fluids ounces. For you")
    print("reference the formula is: ")
    print("1 cups = 8 fluid ounces")
    print()


def cups_to_ounces(cups):
    ounces = cups * 8
    print("That converts to", ounces , 'ounces')


main()