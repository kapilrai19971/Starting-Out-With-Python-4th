#This program demonstrates keyword arguments

def main():
    #show the amiunt of simple interest, using 0.01 as
    #interest rate per period, 10 as the no. og periods,
    #and $10000 as principal.
    show_interest(rate = 0.01, periods = 10, principal = 10000.00)


#the show_interest funcion displays the amount of
#simple interest for a given principal, interest rate
#per period, and no. of periods.
def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f"The simple interest of {principal} is {format(interest, '.2f')}", sep='')

#Call the main function
main()

#Without main function
def interest(principal, rate, periods):
    result = principal * rate * periods
    print("Total simple interest is ", format(result, '.2f'), sep='')


interest(principal= 10000.00, rate = 0.01, periods= 10)
