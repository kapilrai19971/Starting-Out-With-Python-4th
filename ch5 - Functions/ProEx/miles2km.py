# 1. Kilometer Converter
# Write a program that asks the user to enter the distance of a kilometer, then converts that
# distance to miles. The conversion formula is as follows:
# Miles = Kilometers X 0.6214
#
# def main():
#     get_miles()


# def get_miles():
#     conv = 0.6214
#     km = float(input("Enter the distance of a kilometer: "))
#     miles = km * conv
#     print(f"Total distance in miles of {km}: {format(miles, '.2f')} miles")
#
# get_miles()
conv = 0.6214
def main():
    km = float(input("Enter the distance of a kilometer: "))
    result= get_miles(km)
    print(f"Total distance of {km} KM: {format(result, '.2f')} ")


def get_miles(n):
    return n * conv


main()