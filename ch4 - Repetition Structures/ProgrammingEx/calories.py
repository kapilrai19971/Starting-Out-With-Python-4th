# 2. Calories Burned
# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
# uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
#
# cal = 4.2
# time = 10
# while time <= 30:
#     print(f"You are burning {cal * time} calories in {time} minutes." )
#     time += 5

# calories burned
# cal_per_min=4.2
#
# # print the headers
# print("Minutes\t\tCalories")
# print("------------------------")
#
# for mins in range(10,31,5):
#     calories=mins*cal_per_min
#     print(mins,"\t\t",calories)

# print()
# calBurn = 4.2
#
# for time in range(10,31,5):
#     total = time * calBurn
#     print(f"You are burning {total} calories in {time} minutes.")

# burn = 4.2 #per minute
# n = 10
# while n <= 30:
#     total = n * burn
#     print(f'Calories burn in {n} minutes is ', total)
#     n += 5

calBurn = 4.2

for time in range(10,31,5):
    total = time * calBurn
    print('Calories burn in', time ,' minutes' , ' is ', total)


