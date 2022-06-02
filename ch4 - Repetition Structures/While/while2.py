# Write a while loop that asks the user to enter two numbers. The numbers should be
# added and the sum displayed. The loop should ask the user if he or she wishes to perform
# the operation again. If so, the loop should repeat, otherwise it should terminate.

choose = 'y'

while choose == 'y':
    num = int(input("Enter First Number:      "))
    num1 = int(input("Enter Second Number:     "))
    sum = num + num1
    print(sum)

    choose = input("Do you want to repeat again? \n\n "
                   "If you want to repeat again press 'y' for yes.   ")