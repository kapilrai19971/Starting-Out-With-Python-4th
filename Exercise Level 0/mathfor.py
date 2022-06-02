# Get the desired future value.
# Get the annual interest rate.
# Get the number of years that the money will sit in the account.
# Calculate the amount that will have to be deposited.
# Display the result of the calculation in step 4.

f = float(input("Future Value: "))
r = float(input("Rate of Interest: "))
n = float(input("No. of years: "))

p = f / (1 + r)**n


print("You have to deposite: ", format(p ,'.2f'))
