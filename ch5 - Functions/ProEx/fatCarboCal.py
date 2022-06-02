#Calories from gat and carbohydrates

def calories():
    fat_grams = get_fat_grams()

    carbo_grams = get_carbohydrate_grams()

    calories_from_fat = calc(fat_grams)
    print()
    
    print("Calories that is from fat: ", format(calories_from_fat, ',.2f'), sep='')
    print()
    
    calories_from_carbs = calcCarbo(carbo_grams)
    
    print("Calories that is gain from carbohydrates: ", format(calories_from_carbs, ',.2f'), sep='')
    print()
    
    total = calories_from_fat + calories_from_carbs
    print('Total Calories: ', total)
    
def get_fat_grams():
    fat = float(input("Enter tha number of fat grams consumed per day: "))
    return fat


def get_carbohydrate_grams():
    carbo_grams = float(input("Enter the number of carbohydrate grams consumed per day: "))
    return carbo_grams


def calc(fat_grams):
    return fat_grams * 9


def calcCarbo(carbo_grams):
    return carbo_grams * 4


calories()
