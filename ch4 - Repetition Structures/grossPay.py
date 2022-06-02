
hrs = int(input('Enter the hours worked per week:  '))

while hrs < 1 or hrs > 85:
    print('ERROR: The hours that entered by you is not accepted.')
    print('Weekly working hours cannot be 0 or more than 90 hrs.')
    hrs = int(input('Enter the hours worked per week:  '))
pay_rate = int(input('Enter pay rate per hour: $'))

gross_pay = hrs * pay_rate

print('Total gross pay: $', format(gross_pay,'.2f'))