# 2. Sales Prediction
# A company has determined that its annual profit is typically 23 percent of total sales. Write
# a program that asks the user to enter the projected amount of total sales, then displays the
# profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

total_sales = float(input("Total Sale Amount: "))
profit = 0.23

profit_amount = total_sales * 0.23

print("Total profit amount: ", format(profit_amount, '.2f'))