# Get the original price of the item.
# Calculate 20 percent of the original price. This is the amount of the discount.
# Subtract the discount from the original price. This is the sale price.
# Display the sale price.

o_price = float(input("Original Price: "))

discount_amount = o_price * 0.2

sale_amout = o_price - discount_amount

print("The sale amount is", sale_amout)

