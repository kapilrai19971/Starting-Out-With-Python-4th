# 6. Payment Instalments
# Write a program that asks the user to enter the amount of a purchase and the desired
# number of payment instalments. The program should add 5 percent to the amount to get
# the total purchase amount, and then divide it by the desired number of instalments, then
# display messages telling the user the total amount of the purchase and how much each
# instalment will cost.

amount_purchase = float(input("Enter the amount of purchase: $"))
instalment_payment = float(input("Enter the desired number of payment instalments: "))

total_purchase = amount_purchase + (amount_purchase * 0.05)
instal_pay = total_purchase / instalment_payment

print("Total Purchase Amount: $",format(total_purchase,',.2f'))
print(f"Each instalment will cost: ${format(instal_pay,',.2f')}")