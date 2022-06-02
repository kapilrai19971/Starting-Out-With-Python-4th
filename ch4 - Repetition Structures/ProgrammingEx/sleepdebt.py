# 11. Sleep Debt
# A “sleep debt” represents the difference between a person’s desirable and actual amount
# of sleep. Write a program that prompts the user to enter how many hours they slept each
# day over a period of seven days. Using 8 hours per day as the desirable amount of sleep,
# determine their sleep debt by calculating the total hours of sleep they got over the seven-day
# period and subtracting that from the total hours of sleep they should have got. If the user
# does not have a sleep debt, display a message expressing your jealousy.


total = 0
weekly_hrs = 56

for i in range(1, 8):
    hrs = int(input(f"Enter sleeping hours per day {i}: "))
    total += hrs

    sleep_debt = weekly_hrs - total
if sleep_debt < 0:
    print("You are jealousy, You don't have sleep debt. ")
else:
    print("You have sleeping debt.")