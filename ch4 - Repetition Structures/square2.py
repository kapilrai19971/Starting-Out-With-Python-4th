#Letting user Control loop

print('This program displays lists of numbers and its squares.')
print("(Started from 1) and their squares.")

number = int(input('How high should I go? '))

print('Number \t Squares')
for i in range(1, number+1):
    square = i **2

    print(i, '\t' , square)

