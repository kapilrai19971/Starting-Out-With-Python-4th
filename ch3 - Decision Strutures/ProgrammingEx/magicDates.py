# Magic Dates

month = int(input("Enter month (1 -12): "))
day = int(input("Enter day (1- 31): "))
year = int(input("Enter year (only 2 last digits of year): "))

print(str(month) + '/' + str(day) + '/' + str(year) + " is")

if ((month * day) == year):
    print(" magic.")

else:
    print("not magic.")