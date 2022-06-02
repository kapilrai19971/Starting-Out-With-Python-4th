# Write an if-else statement that assigns True to the again variable if the score variable
# is within the range of 40 to 49. If the score variable’s value is outside this range,
# assign False to the again variable.

print("Enter number: ")

num = int(input())

if num >= 40 and num <= 49:
    print("True.")

else:
    print("False.")