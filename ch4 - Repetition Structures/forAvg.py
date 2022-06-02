# # min_kph = 60
# # increment = 10
# # max_kph = 131
# # print("KPH\t\tMPH")
# # for kph in range(min_kph,max_kph,increment):
# #     mph = kph * 0.6214
# #     print(kph, "\t",format(mph, '.1f'))
# #
# # START_SPEED = 60 # Starting speed
# # END_SPEED = 131 # Ending speed
# # INCREMENT = 10 # Speed increment
# # CONVERSION_FACTOR = 0.6214 # Conversion factor
# #
# # # Print the table headings.
# # print('KPH\tMPH')
# # print('--------------')
# # # Print the speeds.
# # for kph in range(START_SPEED, END_SPEED, INCREMENT):
# #     mph = kph * CONVERSION_FACTOR
# #     print(kph, '\t', format(mph, '.1f'))
#
# # for i in range(1,6,1):
# #     print("Hello World")
#
# # start = 60
# # end = 131
# # increment = 10
# #
# # print("KPH \t\t MPH")
# # for kph in range(start,end,increment):
# #     mph = kph * 0.6214
# #     print(kph , "\t\t\t" , format(mph, '.1f'))



# Printing squares of numbers, that is input by user , How high should user goses..

# print("Table of number and it's squares...")
#
# n = int(input("How high should i go?    "))
# print("Numbers \t\t Squares")
# for i in range(1,n+1):
#     square = i **2
#
#     print(i, "\t\t\t\t", square)


#Average time of runner that he runs in lap:

avg = 0
total = 0
lap = int(input("Enter laps: "))
for i in range(1, lap+1):
    time = int(input(f"Lap time of lap {i} in second: "))
    total += time

print("Total: ", total)
avg = total/lap
print("Average: ", avg)


