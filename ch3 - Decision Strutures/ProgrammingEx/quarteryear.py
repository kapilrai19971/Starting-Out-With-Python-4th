# Quarter of the Year

month = int(input("Enter month: "))

if month >= 1 and month <= 3:
    print("First Quarter.")

elif month >= 4 and month <= 6:
    print("Second Quarter.")

elif month >= 7 and month <= 9:
    print("Third Quarter.")

elif month >= 10 and month <= 12:
    print("Fourth Quarter.")

else:
    print("Error!")