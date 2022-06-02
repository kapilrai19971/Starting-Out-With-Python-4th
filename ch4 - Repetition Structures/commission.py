# Program calculates sales commissions.

next = 'Y'

while next == 'Y' or next == 'y':

    sales = float(input("Amount of sales:   $"))
    commissionRate = float(input("Commission rate:      "))

    totalCommission = sales * commissionRate

    print(f"Total commission: $ {format(totalCommission, '.2f')}")


    next = input("Do you want to calculate next calculation:" + "Enter yes for 'Y':  ")