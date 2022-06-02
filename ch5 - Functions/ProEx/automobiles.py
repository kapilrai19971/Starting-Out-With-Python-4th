#This program total monthly cost of automobile cost and annual expenses.

def main():
    
    auto_loan = get_automobile_loan()

    auto_insurance = get_insurance()

    auto_gas = get_gas_cost()

    auto_oil = get_oil_cost()

    auto_tires = get_tire_expenses()

    auto_maintenance = get_maintenance_cost()

    monthly_cost = (auto_loan + auto_insurance + auto_gas + auto_oil + auto_tires + auto_maintenance)


    total = (auto_loan + auto_insurance + auto_gas + auto_oil + auto_tires + auto_maintenance) * 12
    print()
    print("Total expenses per month: $", format(monthly_cost, ',.2f'), sep='')
    print()

    print("Total expenses year: $", format(total, ',.2f'), sep ='')
    
def get_automobile_loan():
    loan = float(input("Enter loan expenses per month: $"))
    return loan


def get_insurance():
    insurance = float(input("Enter Automobile insurance per month: $"))
    return insurance


def get_gas_cost():
    gas = float(input("Enter gas cost per month: $"))
    return gas


def get_oil_cost():
    oil_cost = float(input("Enter oil cost per month: $"))
    return oil_cost


def get_tire_expenses():
    tire_cost = float(input("Enter tire cost per months: $"))
    return tire_cost


def get_maintenance_cost():
    maintenance_cost = float(input("Enter maintenance cost per month: $"))
    return maintenance_cost


main()
