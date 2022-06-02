# This program uses a loop to display a
# table of numbers and their squares.

print('Displaying list of numbers')
print('and their squares.')

# Getting starting number
start = int(input('Enter starting number:  '))

# Getting ending number
end = int(input("Enter ending number:  "))

# Printing heading of tables
print()
print('Numbers\t\tSquare')

# Print the numbers and their squares.
for i in range(start, end+1):
    square = i**2
    print(i, '\t\t\t' , square)
