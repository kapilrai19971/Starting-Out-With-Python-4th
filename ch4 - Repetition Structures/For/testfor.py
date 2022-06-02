month = int(input("\nEnter the month from 1 to 12: "))
day = int(input("Enter the day from 1 to 31: "))
year = int(input("Enter the year: "))

#65/56/56
message = '\' + format(month) + '/' \
            + format(day) + '/' \
            + format(year) + \
            ' IS '

if (month * day) != year):
    message += 'NOT'

message += 'magic.'

print(message, "\n\n")
