# 9. Circle Measurements
# Write a program that asks the user to enter the radius of a circle. The program should calculate
# and display the area and circumference of the circle using πr*p2 for the area and 2πr
# for the circumference.
# Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math"
# to the start of the program and then use "math.pi" wherever you need the value of pi in
# the program.

pi = 3.14159

radius = float(input("Enter the radius of a circle: "))

circumference = pi * radius * 2

area_of_circle = (pi * radius)**2

print("Circumference of Circle: ",format(circumference,',.2f'))
print("Area of circle: ",format(area_of_circle,',.2f'))