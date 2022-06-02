# Monthly Sales Tax

state_tax = 0.05
county_tax = 0.025

def tax():
    monthly_sales = get_total_sales()

    county_tax_amt = county_sales_tax(monthly_sales)

    state_tax_amt = state_sales_tax(monthly_sales)

    print()
    print("Total amount of county sales tax: $", format(county_tax_amt, ',.4f'), sep='')

    print()
    print("Total amount of state sales tax: $", format(state_tax_amt, ',.4f'), sep='')

    print()
    print("Total sales tax amount: $", format((county_tax_amt + state_tax_amt), ',.4f'), sep='') 

def get_total_sales():
    sales_of_month = float(input("Enter the total sales for the month: $"))
    return sales_of_month


def county_sales_tax(monthly_sales):
    return monthly_sales * county_tax 


def state_sales_tax(monthly_sales):
    return monthly_sales * state_tax


tax()
