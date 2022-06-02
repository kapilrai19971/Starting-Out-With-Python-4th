#Area of rectangle

print(" First Rectangle: ")
l1 = float(input("Length (l1): "))
w1 = float(input("Width (w1): "))

print(" Second Rectangle: ")

l2 = float(input("Length (l2): "))
w2 = float(input("Width (w2:: "))

area1 = l1 * w1
area2 = l2 * w2

if area1 > area2:
    print(f"First rectangle is greater area with {format(area1, '.2f')} ")

elif area2 > area1:
    print(f"Second rectangle is greater area with {format(area2, '.2f')}")

else:
    print(f"Rectangles are equal with area of {format(area1, '.2f')} = {format(area2, '.2f')}")

