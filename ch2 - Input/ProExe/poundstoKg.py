#Pound to Kilogram

# One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter
# the mass of an object in pounds and then calculates and displays the mass of the object in
# kilograms.
pound = 0.454
mass_in_pound = float(input("Enter a mass of object in pounds: "))
pound_to_kilogram = mass_in_pound * pound

print(f"Mass of an object in {mass_in_pound} pounds: {pound_to_kilogram} Kilograms")