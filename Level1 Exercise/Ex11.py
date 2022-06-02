# Ingredient Adjuster

cookies = 48
cup_of_sugar = 1.5
cup_of_butter = 1
cup_of_flour = 2.75

wanted_cookies = float(input("How many cookies do you want to make? \n"))

sugar = ( cup_of_sugar * wanted_cookies) / cookies
butter = (cup_of_butter * wanted_cookies) / cookies
flour = (cup_of_flour * wanted_cookies) / cookies

print("                 RECIPE INFO                         ")
print("you need ", format(sugar, '.2f') , " amount sugar for making one cookie")
print("you need ", format(butter, '.2f') , " amount butter for making one cookie")
print("you need ", format(flour, '.2f') , " amount flour for making one cookie")
