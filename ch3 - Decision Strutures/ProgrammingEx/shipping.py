# Shipping Charges

print("     The Fast Freight Shipping Company charges         ")

weight_of_packages = float(input("weight of package (in pounds): "))

if weight_of_packages > 0 and weight_of_packages <= 2:
    charge = weight_of_packages * 1.5
    print(f"Your total shipping charge is {charge} with load of {weight_of_packages} pounds.")

elif weight_of_packages > 2 and weight_of_packages <= 6:
    charge1 = weight_of_packages * 3
    print(f"Your total shipping charge is ${charge1} with load of {weight_of_packages} pounds.")

elif weight_of_packages > 6 and weight_of_packages <= 10:
    charge2 = weight_of_packages * 4
    print(f"Your total shipping charge is ${charge2} with load of {weight_of_packages} pounds.")

elif weight_of_packages > 10:
    charge3 = weight_of_packages * 4.75
    print(f"Your total shipping charge is ${charge3} with load of {weight_of_packages} pounds.")