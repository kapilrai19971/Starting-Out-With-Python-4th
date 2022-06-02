# 8. Tip, Tax, and Total
# Write a program that calculates the total amount of a meal purchased at a restaurant. The
# program should ask the user to enter the charge for the food, then calculate the amounts
# of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

tips = 0.18
sales_tax = 0.07

charge_of_food = float(input("Enter a Food Price: $"))

tips_amount = charge_of_food * tips

amount_sales_tax = charge_of_food * sales_tax

total = charge_of_food + tips_amount + amount_sales_tax

print("Tips Amount: $",format(tips_amount,',.2f'))
print("Amount of sales tax: $",format(amount_sales_tax,',.2f'))
print("Total Amount: $",format(total,',.2f'))