#Time Calculator

user_seconds = float(input("Enter seconds: "))

if user_seconds >= 86400:
    day = user_seconds / 86400
    hour = user_seconds /3600
    minute = hour * 60
    second = minute * 60

    print(f"{user_seconds} second has {day} day, {hour} hour, {minute} minute, and {second} second.")

elif user_seconds >= 3600:
    hour = user_seconds / 3600
    minute = hour * 60
    second = minute * 60
    print(f"{user_seconds} seconds has {hour} hour, {minute} minutes, {second} second.")


elif user_seconds >= 60:
    minute = user_seconds / 60
    second = minute * 60
    print(f"{user_seconds} seconds has {minute} minutes, {second} second.")

