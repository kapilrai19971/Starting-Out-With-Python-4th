# # 3. Lap Times
# # Write a program that asks the user to enter the number of times that they have run around
# # a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps.
# # When the loop finishes, the program should display the time of their fastest lap, the time of
# # their slowest lap, and their average lap time.
#
# laps = int(input("Enter laps:  "))
#
# time = 0
# fastest_lap = 0
# lowest_lap = 0
# total = 0
# avg = 0
# check = True
#
# for x in range(1, laps + 1):
#     # print("laps: ", x)
#     time = int(input(f"Enter time of {x} laps in mins: "))
#     while check == True:
#         fastest_lap = time
#         lowest_lap = time
#         check = False
#         total += time
#     if laps > lowest_lap:
#         lowest_lap = time
#
#     if time < fastest_lap:
#         fastest_lap = time
#
#     avg = total / laps
#
# print("Time of fastest lap: ", fastest_lap)
# print("Time of slowest lap: ", lowest_lap)
# print("Average time of all laps: ", avg)
#
total = 0.0
lap_time = []
lap = int(input('Enter total laps: '))

for time in range(1, lap +1):
    time = int(input(f'Time of lap {time}:'))
    total += time
    lap_time.append(time)

avg = total / lap
fast_time = min(lap_time)
slowest_time = max(lap_time)

print('Average lap time per laps: ' ,format(avg, '.2f'), 'mins')
print(f'Fastest time of lap is {fast_time} mins.')
print(f'Sowest time of lap is {slowest_time} mins.')
