# Tip, Tax, and Total

amt_of_meal_purchase = float(input("Total amount of meal purchse: "))

tip = amt_of_meal_purchase * 0.18

sales_tax = amt_of_meal_purchase * 0.07

total_purchase_amount = (amt_of_meal_purchase + tip + sales_tax)
print("         Customer Bills          ")

print("Total Amount: ", format(total_purchase_amount, '.2f'))

print("Tip Amount: ", format(tip, '.2f'))

print("Total Sales Tax: ", format(sales_tax, '.2f'))