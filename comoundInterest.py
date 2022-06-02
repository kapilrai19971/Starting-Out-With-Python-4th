#Compound Interest
print("Compounded time must be written as 4 months, 12 months, 6 months etc.\n "
      "Interest rate should be written as 2 percent but not 0.02")
#Getting principal, interest rate, compounded time and time
p = float(input("Principal: $"))

#This is for rate that should be whole number and divided by 100
r = float(input("Annual Interest Rate: ")) / 100
n = float(input("Compounded Time: "))
t = float(input("Number of years: "))

#Calculation of compound amount
amount = p * (1 + r/n) ** (n * t)

#Printing compound interest
print("Total compounded interest: $", format(amount,'.2f'))

