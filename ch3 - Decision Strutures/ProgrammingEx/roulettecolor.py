# Roulette Wheel Colors

pocket = int(input("Enter pocket (0 - 36): "))

if pocket == 0:
    print("Green")


elif pocket >= 1 and pocket <= 10:
        if (pocket % 2) == 0:
            print("Black")

        else:
            print("Red")

elif pocket >= 11 and pocket <= 18:
        if (pocket % 2) == 0:
            print("Red")

        else:
            print("Black")

elif pocket >= 19 and pocket <= 28:
        if (pocket % 2) == 0:
            print("Black")

        else:
            print("Red")

elif pocket >= 29 and pocket <= 36:
        if (pocket % 2) == 0:
            print("Red")

        else:
            print("Black")
else:
    print("Error")