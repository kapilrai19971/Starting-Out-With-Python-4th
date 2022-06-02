# Mass and Weight

print("Enter mass (in Kilogram.): ")

mass = float(input())

weight = mass * 9.8

if weight > 500:
    print(f"It is too heavy with weigh of {format(weight , '.2f')} newton.")

elif weight < 100:
    print(f"It is too light with weigh of {format(weight, '.2f')} newtons.")