# 6. Payment Instalments
# Write a program that asks the user to enter the amount of a purchase and the desired
# number of payment instalments. The program should add 5 percent to the amount to get
# the total purchase amount, and then divide it by the desired number of instalments, then
# display messages telling the user the total amount of the purchase and how much each
# instalment will cost.

purchase_amount = float(input("Purchase Amount: "))

noOfInstalment = float(input("Number of instalment: "))

total_amount = purchase_amount + (purchase_amount * 0.05)

totalInstal = total_amount / noOfInstalment

print("The total amount of purchase: ", format(total_amount, '.2f'))

print("Each instalment cost: ", format(totalInstal, '.2f'))


