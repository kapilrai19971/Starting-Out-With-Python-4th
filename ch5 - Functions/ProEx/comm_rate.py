#This program shows salesperson's commission rate and advanced payment.

def commission():
    monthly_sales = get_salesperson_sales()
    
    advanced_pay = get_advanced_pay()
    
    commission_rate = get_comm_rate(monthly_sales)
    
    total_payout = monthly_sales * commission_rate - advanced_pay
    
    print("Total pay out: $", format(total_payout, ',.2f'), sep='')

    if total_payout < 0:
        print("Employee must reimburse to the company.")


def get_salesperson_sales():
    sales_per_month = float(input("Enter salesperson's sales per month: $"))
    return sales_per_month


def get_advanced_pay():
    print("If worker doesn't received advanced pay, write 0 ")
    advanced_payment = float(input("Enter advanced pay: $"))
    return advanced_payment


def get_comm_rate(monthly_sales):
    if monthly_sales < 10000:
        rate = 0.1

    elif monthly_sales >= 10000 and monthly_sales <= 14999.99:
        rate = 0.12

    elif monthly_sales >= 15000 and monthly_sales <= 17999.99:
        rate = 0.14

    elif monthly_sales >= 18000 and monthly_sales <= 21999.99:
        rate = 0.16

    else:
        rate = 0.18

    return rate

commission()
