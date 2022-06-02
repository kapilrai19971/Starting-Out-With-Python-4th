total = 0
start = 10
end = 81
increment = 10
eqv = 1.60934

print('Miles \t\t Kilometers')
print('------------------------')
for miles in range(start, end, increment):
    total = miles * eqv
    print(miles, '\t\t\t\t' , format(total, '.2f') )