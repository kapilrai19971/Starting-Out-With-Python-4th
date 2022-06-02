# Write an if-else statement that determines whether the points variable is outside
# the range of 9 to 51. If the variable’s value is outside this range it should display
# “Invalid points.” Otherwise, it should display “Valid points.”

print("Enter number: ")

num = int(input())

if num >= 9 and num <= 51:
    print("Valid points.")

else:
    print("Invalid points.")