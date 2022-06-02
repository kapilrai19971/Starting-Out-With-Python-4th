# Compound Interest

p = float(input("Principal amount to be deposited: $"))

r = float(input("Annual interest rate: %"))/100

n = float(input("No. of time per year that the interest is compouded: "))

t = float(input("No. of years: "))

a = p * (1 + (r/n))**(n * t)

print("The amount of money that will be in your account after " + str(t) +
      " years: $", format(a, '.2f'))

