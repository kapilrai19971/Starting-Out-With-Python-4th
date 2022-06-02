def is_valid(mod_num):
    if mod_num != 100 and mod_num != 200 and mod_num != 300:
        status = True

    else:
        status = False

    return status

model = int(input("Enter the model number: "))

while is_valid(model):
    print('The valid model numbers are 100, 200 and 300.')
    model = int(input("Enter a valid model number: "))