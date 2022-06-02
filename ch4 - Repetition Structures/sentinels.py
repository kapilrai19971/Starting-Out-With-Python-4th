#sentinels

tax_factor = 0.0065

print('Enter the property lot number')
print('or enter 0 to end.')

lot = int(input('Lot number: '))

while lot != 0:
    value = float(input('Enter the property value: $'))

    tax = value * tax_factor

    print('Property tax: $', format(tax,',.2f'))

    print('Enter the property lot number')
    print('or enter 0 to end.')
    lot = int(input('Lot number: '))