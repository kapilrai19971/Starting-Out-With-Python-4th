#This program show the assessment value and property tax.

accessment_value_per = 0.6

accessment_tax = 0.0072 #i.e. 72 cent

def property_tax():
    property_actual_value = get_property_cost()

    accessment_value = get_accessment_cost(property_actual_value)
    print("Accessment value of $" + str(property_actual_value) + ": $" + str(format(accessment_value, ',.2f')))
    print()
    
    accessment_property_tax = get_property_tax(accessment_value)
    print("Accessment property tax $" + str(accessment_value) + ": $" + str(format(accessment_property_tax, ',.2f')), sep='')


def get_property_cost():
    property_cost = float(input("Enter actual value of property: $"))
    return property_cost


def get_accessment_cost(property_actual_value):
    accessment_cost = property_actual_value * accessment_value_per
    return accessment_cost


def get_property_tax(accessment_value):
    property_tax = accessment_value * accessment_tax
    return property_tax


property_tax()
