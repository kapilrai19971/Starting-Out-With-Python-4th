# 10. Tuition Increase
# At one college, the tuition for a full-time student is $8,000 per semester. It has been announced
# that the tuition will increase by 3 percent each year for the next 5 years. Write a program
# with a loop that displays the projected semester tuition amount for the next 5 years.

per_sem = 8000
interest = 0.03
start = 2022
end = 2027

print('Year\t\t Semester Fee')
print('---------------------------')
for fee in range(start, end):
    total = per_sem * interest
    per_sem += total
    print(fee, '\t\t\t','$', format(per_sem, '.2f'))


