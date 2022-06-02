mark_up = 2.5
another = 'y'

while another == 'y' or another == 'Y':
    wholesale = float(input("Enter the item's" + " wholesale cost: $"))

    retail = wholesale * mark_up

    print('Retail price: $', format(retail, '.2f'), sep='')

    another = input('Do you have another item'+ ' (Enter y of yes): ')