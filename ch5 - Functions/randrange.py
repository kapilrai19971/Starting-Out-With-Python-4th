import random
print("Use of randrange function:")


def main():
    print("Printing random number from randrange: ")

    message()
    print("--------------------")


def message():
    number = random.randrange(0, 101, 10)
    print(number)


main()

print()
print("Use of random function:")


def main():
    num = random.random()
    print("The use of random function and ranfom floating-point number: ", num)


main()

print()
print("Use of uniform function: ")


def uni():
    numbers = random.uniform(1.0, 10.0)
    print(numbers)


uni()