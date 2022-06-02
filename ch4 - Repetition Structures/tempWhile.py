
temp = int(input("Enter temperature: "))

while temp > 102.5:
    print("Turn down the thermostat and wait for 5 min and check again.")
    temp = int(input("Enter temperature: "))

else:
    print(f"{temp} degree celsius temperature is acceptable.")
    print("Check in 15 minutes.")