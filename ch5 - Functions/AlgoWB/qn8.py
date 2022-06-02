# 8. A program contains the following function definition:
# def cube(num):
# return num * num * num
# Write a statement that passes the value 4 to this function and assigns its return value
# to the variable result.

def main():
    n = 4
    result = cube(n)
    print(f"Cube of {n}: {result}")

def cube(num):
    return num * num * num


main()