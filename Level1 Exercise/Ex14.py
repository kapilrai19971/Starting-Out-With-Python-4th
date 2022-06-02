# Planting Grapevines

r = float(input("Length of row (in feet): "))
e = float(input("Amount of space used by an end-post assembly(in feet): "))
s = float(input("Amount of space between the vines(in feet): "))

v = r - (2 * e) / s

print("The number of grapevines that will fit in the row: ", v)