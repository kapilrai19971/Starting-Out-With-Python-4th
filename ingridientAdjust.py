# 10. Ingredient Adjuster
# A cookie recipe calls for the following ingredients:
# • 1.5 cups of sugar
# • 1 cup of butter
# • 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients. Write a program that
# asks the user how many cookies he or she wants to make, then displays the number of cups
# of each ingredient needed for the specified number of cookies.

# Ingredient Adjuster

# Ask user how many cookies he or she wants
cookie=int(input("Enter the amount of cookies you want: "))

# Find the ingredients (Simple ratio and proportion

sugar=cookie*(1.5)/48
butter=cookie*(1)/48
flour=cookie*(2.75)/48

print()
print("You will need following ingredients: ")
print(sugar, "cups of sugar")
print(butter, "cups of butter")
print(flour, "cups of flour")