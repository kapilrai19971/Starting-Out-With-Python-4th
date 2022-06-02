#Factorail of nonnegative numbers

num = int(input("Enter non-negative number: "))
total = 1 # accumulator

for i in range(1, num + 1):
    total *= i

print(f"Factorial of {num}: ", total)
