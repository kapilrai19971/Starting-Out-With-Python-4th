# Write a loop that calculates the total of the following series of numbers:
# 1/30 + 2 /29+......+ 30/1
r = 0
for i in range(1, 31):
    r += i/ (31 - i)
    print(format(r, '.2f'))