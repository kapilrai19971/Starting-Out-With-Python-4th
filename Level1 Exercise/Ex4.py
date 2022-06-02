# 3. Pounds to Kilograms
# One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter
# the mass of an object in pounds and then calculates and displays the mass of the object in
# kilograms.

mass = float(input("Mass of an object(In Pound): "))

kilogram = mass * 0.454

print("The mass of given object in kilogram is",format(kilogram, '.2f'))
