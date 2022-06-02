#Total Purchase

# A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

tax_percent = 0.07
item1 = float(input("First Item Price: $"))
item2 = float(input("Second Item Price: $"))
item3 = float(input("Third Item Price: $"))
item4 = float(input("Forth Item Price: $"))
item5 = float(input("Fifth Item Price: $"))

sub_total = item1 + item2 + item3 + item4 + item5
amount_of_sales_tax = sub_total * tax_percent
total_amount_after_tax = sub_total + amount_of_sales_tax
print()
print(f"Subtotal before tax: ${format(sub_total,'.2f')}")
print(f"Amount of Tax: ${format(amount_of_sales_tax,'.2f')}")
print(f"Total amount after tax: ${format(total_amount_after_tax,'.2f')}")
