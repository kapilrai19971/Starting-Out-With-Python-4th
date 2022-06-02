#This program uses the return value of a function:

def main():

    first_age = int(input("Enter your age: "))
    second_age = int(input("Enter your friend's age: "))

    total = sum(first_age, second_age)

    print("Together you are", total, "years old.")


def sum(num1, num2):
    return num1 + num2


main()