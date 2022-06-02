# #Sales Pridiction
#
# A company has determined that its annual profit is typically 23 percent of total sales. Write
# a program that asks the user to enter the projected amount of total sales, then displays the
# profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

profit = 0.23
total_sales = float(input("Enter the total sales: $"))

total_amount = total_sales * profit

print("Total Amount per annual (23 percent): $",total_amount)
