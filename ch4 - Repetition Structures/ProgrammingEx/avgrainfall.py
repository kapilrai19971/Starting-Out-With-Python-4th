# 5. Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average rainfall over
# a period of years. The program should first ask for the number of years. The outer loop will
# iterate once for each year. The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of
# rainfall, and the average rainfall per month for the entire period.

year = int(input('Enter no. year: '))
months = 12
total = 0
for i in range(1, year+1):
    print('Year: ', i)
    for j in range(1,13,1):
        rainfall = int(input(f'Enter the inches of rainfall in month {j} : '))
        total += rainfall

print('Total no. of months: ', months * year)
print(f'Average rainfall : {total/(months * year)}')
print('Total inches of rainfall: ',total, 'inches')

# print('Average rainfall per month :', avg)

#
# years=int(input("How many years of data you want to enter?: "))
# months=12
# total_rainfall=0.0      # this is accumulator
#
# # there will be a nested loop. One for year one for months within year loop.
# for y in range(1,years+1):
#     print()
#     print("Enter the data for year", y)
#     print("------------------------")
#     for m in range(1, months+1):
#         print("Please enter year", y, "month", m, "rainfall amount in inches", end='')
#         rainfall=float(input(": "))
#         total_rainfall+=rainfall
#
# print()
# print("There are ", years*months, "months in the data.")
# print("Total inches of rain is", total_rainfall)
# print("Average rainfall per month is ", format(total_rainfall/(years*months), ",.2f"))