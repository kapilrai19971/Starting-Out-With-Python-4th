# Male and Female Percentages

male_student = int(input("Enter no of male students: "))
female_student = int(input("Enter no of female students: "))

total_student = male_student + female_student

mPercentage = male_student / total_student
fPercentage = female_student / total_student

print("             PERCENTAGE OF STUDENTS             ")
print("Total : ", total_student)
print("Male : ", format(mPercentage, '.0%'))
print("Female: ", format(fPercentage, '.0%'))