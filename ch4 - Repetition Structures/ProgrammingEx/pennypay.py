# days = int(input("Enter the number of days to calculate: "))
#
# # print headings
# print()
# print("Days\tSalary in $")
# print("-----------------------------")
#
# # set an accumulator and create loop structure
# salary = 0.01  # the first day is one penny
# total = 0
# for d in range(1, days + 1, 1):
#     print(d, "\t$", salary)
#     total += salary
#     salary *= 2
#
# # show total
# print()
# print("The total earnings is ${}".format(total, ",.2f"))


day = int(input('Enter days to calculate: '))

print('Days\t\t\tSalary')
print('--------------------------')

total = 0
salary = 0.01

for i in range(1, day + 1):
    total += salary
    print(i , '\t\t\t\t', '$' ,format(salary, '.2f'))
    salary *= 2
print('Total: $', format(total, '.2f'))
#     print(i , '\t\t\t\t', '$' ,salary)
#     total += salary
#     salary *= 2
# print(f"Total Salary: $ {format(total, '.2f')}")