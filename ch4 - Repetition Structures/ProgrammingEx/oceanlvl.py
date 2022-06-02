# 9. Ocean Levels
# Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
# application that displays the number of millimeters that the ocean will have risen each year
# for the next 25 years.

start = 2022 # starting year
end = 2047 # ending year i.e. 25 year
o_rise = 1.6
j =1
print('Year\t\t Millimeters')
print('--------------------------')
for i in range(start, end):
    mill = j * o_rise
    print(i , '\t\t\t', format(mill, '.2f'))
    j += 1

