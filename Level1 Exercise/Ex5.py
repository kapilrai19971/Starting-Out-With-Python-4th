# 4. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

item = float(input("Price of First item: "))
item1 = float(input("Price of Second item: "))
item2 = float(input("Price of Third item: "))
item3 = float(input("Price of Forth item: "))
item4 = float(input("Price of Fifth item: "))

total = (item + item1 + item2 + item3 + item4)

amount_tax = total * 0.07

amount_with_tax = total + amount_tax

print("         SALES           ")
print("Tax amount: ", format(amount_tax, '.2f'))
print("Total amount with tax: ", format(amount_with_tax, '.2f'))