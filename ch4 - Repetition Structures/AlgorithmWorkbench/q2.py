# Write a while loop that asks the user to enter two numbers. The numbers should be
# added and the sum displayed. The loop should ask the user if he or she wishes to perform
# the operation again. If so, the loop should repeat, otherwise it should terminate.

choose = 'y'

while choose.upper() == 'Y':
    n = int(input("Enter first number: "))
    n1 = int(input("Enter second number: "))
    sum = n + n1
    print(f"Total : {sum}")

    choose = input("Do you want to do next calculation." + " Press 'y' or 'Y' for yes:  ")
