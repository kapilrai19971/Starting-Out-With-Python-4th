# 1. Bug Collector
# A bug collector collects bugs every day for five days. Write a program that keeps a running
# total of the number of bugs collected during the five days. The loop should ask for the
# number of bugs collected for each day, and when the loop is finished, the program should
# display the total number of bugs collected.

# n = 1
# total = 0
# while n <= 5:
#     print("Enter bugs that collects in day", n, end='')
#     bug = int(input(":    "))
#     n +=1
#     total += bug
# print(f"Total bugs collected: {total} bugs")

# bug collector

# set an accumulator for bugs
# bugs_total=0.0
#
# # set repetition structure.
# for day in range(5):     # it is five days.
#     print("Enter the collected bugs for day", day+1, end='')
#     bugs=int(input(": "))
#     # add bugs to accumulator
#     bugs_total+=bugs
# # display the total bugs
# print()
# print("The total bugs collected: ", bugs_total)

# total = 0
# for day in range(5):
#     print("Enter bugs that are collected in day ", day+1 , end='')
#     bug = int(input(": "))
#     total += bug
# print(f"Total bugs collected: {total} bugs")

# total = 0
#
# for i in range(1,6,1):
#     num = int(input(f"Enter no. of bug that collected in day {i}:"))
#
#     total += num
#
# print('Total no of bugs: ', total)
# total = 0
#
# for i in range(1,6):
#     num = int(input(f"Enter no of bugs collected day {i}: "))
#     total += num
#
# print('Total bugs collected: ',total)
total = 0
n = 1
while n <= 5:
    num = int(input(f"Enter bugs collected {n}:"))
    n +=1
    total += num
print('Total: ', total)


