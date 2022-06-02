# Write code that prompts the user to enter a positive nonzero number and validates
# the input.

n = int(input("Enter positive nonzero number:  "))

while n > 0:
    print(f"{n} is not nonzero number.")
    n = int(input("Enter positive nonzero number: "))
else:
    print(f"{n} is nonzero number.")