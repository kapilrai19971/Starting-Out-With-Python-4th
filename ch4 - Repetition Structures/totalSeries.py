# This program calculates the sum of a series of numbers entered by the users:

max = 5 #maximu number

#Initialize an accumulator variable

total = 0.0

#Explaining what we are doing

print('This program calculates the sum of')
print(max, 'numbers you will enter.')

for n in range(max):
    number = int(input('Enter a number:  '))
    total += number

print('Total number:', total)