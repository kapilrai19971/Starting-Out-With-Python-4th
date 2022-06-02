# #Miles-Per-Gallon

# A car's miles-per-gallon (MPG) can be calculated with the following formula:
# MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas
# used. It should calculate the car's MPG and display the result.

miles_driven = float(input("Enter Miles driven: "))
gallons_of_gas_used = float(input("Enter gallons of gas used: "))

mpg = miles_driven / gallons_of_gas_used

print("Miles Per Gallons (MPG): ", mpg)