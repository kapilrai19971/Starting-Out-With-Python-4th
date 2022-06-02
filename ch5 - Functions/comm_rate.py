def main():
    sale = selling()
    advanced = pay_advance()
    comm_rate = get_commission_rate(sale)
    pay = sale * comm_rate - advanced
    print("Payout: $", format(pay, ',.2f'), sep='')

    if pay < 0:
        print("The Salesperson must reimburse")
        print("the company.")
        after_reimburse = sale + pay
        print("After reimbursing payout: $", format(after_reimburse, ',.2f'), sep='')


def selling():
    monthly_sales = float(input("Enter the monthly sales: $"))
    return monthly_sales


def pay_advance():
    print("Enter the amount of advance pay, or")
    print("enter 0, if no advanced pay was given.")
    advance = float(input("Advance pay: $"))
    return advance


def get_commission_rate(sale):
    if sale < 10000.00:
        rate = 0.10

    elif sale >= 10000.00 and sale <= 14999.99:
        rate = 0.12

    elif sale >= 15000.00 and sale <= 17999.99:
        rate = 0.14

    elif sale >= 18000.00 and sale <= 21999.99:
        rate = 0.16

    else:
        rate = 0.18

    return rate


main()