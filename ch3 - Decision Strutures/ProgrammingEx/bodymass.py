# Body Mass Index

user_weight = float(input("Enter user weight(in pounds): "))
user_height = float(input("Enter user height(in inches): "))

bmi = user_weight * 703 / (user_height)**2

if bmi < 18.5:
    print("Underweight")

elif bmi >= 18.5 and bmi < 25:
    print("Optimal")

elif bmi > 25:
    print("Overweight")