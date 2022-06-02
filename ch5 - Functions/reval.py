discount_rate = 0.1


def main():

    get_discount()
    get_sale_price()


def get_discount():
    global discount_rate
    price = float(input("Item's regular price: $"))
    discount = price * discount_rate
    print("Total Discount: $", format(discount, ',.2f'))
    print()

def get_sale_price():
    mrp_price = float(input("MRP of item: "))
    retail_price = mrp_price - (mrp_price * discount_rate)
    print("Retailed price: $", retail_price)


main()


