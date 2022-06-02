#Restaurant Selector
print("                     Restaurant Choice                          \n\n")
print("""Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes\n \n""")

vegetarian = input("Is anyone in your party a vegetarian?   ")
vegan = input("Is anyone in your party a vegan?     ")
gluten_free = input("Is anyone in your party gluten-free?   ")

if vegetarian == 'yes' and vegan == 'no' and gluten_free == 'yes' :
    print("Here is your choice:         ")
    print("""Main Street Pizza Company
Corner Cafe
The Chef's Kitchen""")

elif vegetarian == 'no' and vegan == 'no' and gluten_free == 'no':
    print("Here is your choice:         ")
    print("Joe’s Gourmet Burger")

elif vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'yes':
    print("Here is your choice:       ")
    print("Corner Cafe  \nThe Chef’s Kitchen—")

elif vegetarian == 'yes' and vegan == 'no' and gluten_free == 'no':
    print("Here is your choice:       ")
    print("Mama’s Fine Italian ")