# Feet to Inches

def ftoi():
    feet = get_feet()

    footInches = foot_to_inches(feet)

    print()
    print(f"{feet} feet is equal to {format(footInches, ',.4f')} inches")

def get_feet():
    foot = float(input("Enter a number of feet: "))
    return foot


def foot_to_inches(feet):
    return feet * 12

ftoi()
