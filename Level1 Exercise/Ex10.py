#Circle measurement
import math
radius = float(input("Radious of circle: "))

area = math.pi * (radius**2)

circumference = 2 * math.pi * radius

print("         Circle Measurement          ")

print("Area of circle: ", format(area, '.2f'))

print("Circumference of a circle: ", format(circumference, '.2f'))
