#How much insurance?

insurance_per = 0.8

def main():
    replacement_cost = get_replacement_cost()

    insurance_amount = amount_of_insurance(replacement_cost)
    print()
    print("Minimum amount of insurance he or she get: $", format(insurance_amount, ',.2f'), sep='')


def get_replacement_cost():
    cost = float(input("Enter the replacement cost of the building: $"))
    return cost


def amount_of_insurance(replacement_cost):
    return replacement_cost * insurance_per


main()
