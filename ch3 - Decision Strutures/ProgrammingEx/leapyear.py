# leap year

year = int(input("Enter year:"))

if (year % 100) == 0 and (year % 400) == 0:
    print(f"In {year} February has 29 days.")

elif year % 4 == 0:
    print(f"In {year} February has 29 day and is a leap year.")
else:
    print(f"{year} is not leap year and February has 28 days.")