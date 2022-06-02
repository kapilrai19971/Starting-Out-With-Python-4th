#Gross Pay that is input users value is invalid

# This program displays gross pay.
#  Get the number of hours worked.
hours = int(input('Enter the hours worked this week: '))

# Get the hourly pay rate.
pay_rate = int(input('Enter hourly pay rate: $'))
# Calculate gross pay
gross_pay = hours * pay_rate

#Display the gross pay
print("Total gross pay: $", format(gross_pay, '.2f'))

#There cannot be more than 400 hrs worked hours in week and this is invalid but it is validation loop error.



