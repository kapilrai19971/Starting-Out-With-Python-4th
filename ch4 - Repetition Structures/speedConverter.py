# Write a program to calculate  following output using for loop using formula:
#     mph = kph * 0.6214
#     mph = the speed in miles per hour
#     kph = the speed in kilometers per hour
#     starting speed is 60
#     end speed is 130
#     incrment is 10

# KPH MPH
# ----------------
# 60 37.3
# 70 43.5
# 80 49.7
# 90 55.9
# 100 62.1
# 110 68.4
# 120 74.6
# 130 80.8
print("-------------")
print("KPH \t MPH ")
print("-------------")
start_speed = 30
end_speed = 131
increment = 10

for kph in range(start_speed, end_speed, increment):
    mph = kph * 0.6214
    print(kph,'\t', format(mph, '.1f'))