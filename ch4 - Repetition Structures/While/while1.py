# Take 10 integers from keyboard using loop and print their average value on the screen.
sum = 0
i = 1
while i <= 10:
    num = float(input("Enter numbers:    "))
    i = i + 1
    sum = sum + num
    avg = sum/10.0
    print("Average:  ", avg)