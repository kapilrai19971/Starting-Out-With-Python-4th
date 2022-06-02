#Create a global variable

number = 0

def main():
    global number
    number = int(input("Enter a Number: "))
    show_number()

def show_number():
    print("The number you have entered is", number)


main()