# Software Sales

# price is $99
retail_price = 99
software = int(input("Software Quantity: "))

if software > 0 and software <= 10:
    total = software * 99
    print(f"your total amount is  {total}")
    print("You didn't get any discount.")

elif software >= 10 and software <= 19:
    total1 = software * 99
    discount = total1 * 0.1
    after_discount = total1 - discount
    print(f"You have to pay ${after_discount}")
    print(f"You have received ${discount} of discount.")

elif software >= 20 and software <= 49:
    total2 = software * 99
    discount1 = total2 * 0.2
    after_discount1 = total2 - discount1
    print(f"You have to pay ${after_discount1}")
    print(f"You have received ${discount1} of discount.")

elif software >= 50 and software <= 99:
    total3 = software * 99
    discount2 = total3 * 0.3
    after_discount2 = total3 - discount2
    print(f"You have to pay ${after_discount2}")
    print(f"You have received ${discount2} of discount.")

elif software >= 100:
    total4 = software * 99
    discount3 = total4 * 0.4
    after_discount3 = total4 - discount3
    print(f"You have to pay ${after_discount3}")
    print(f"You have received ${discount3} of discount.")