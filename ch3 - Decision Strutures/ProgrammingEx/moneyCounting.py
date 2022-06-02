# Money Counting Game

pennies = int(input("Pennies: "))
nickel = int(input("Nickel: "))
dimes = int(input("Dimes: "))
quarter = int(input("Quarter: "))

dollar = pennies + (5 * nickel) + (10 * dimes) + (25 * quarter)

if dollar == 100:
    print("You wine the game.")

elif dollar >= 100:
    print("You entered more than 1 dollar.")

elif dollar <= 100:
    print("You entered less than 1 dollar.")