# Write code that prompts the user to enter a number in the range of 1 through 100 and
# validates the input.

n = int(input("Enter numbers between 1 to 100: "))

while True:
    if n > 0 and n <= 100:
        print(f"You have enter right number: {n}")
        break
    else:
        print("Out of Range.")
        break