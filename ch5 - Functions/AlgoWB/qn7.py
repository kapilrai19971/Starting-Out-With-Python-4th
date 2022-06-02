# 7. The following statement calls a function named half, which returns a value that is
# half that of the argument. (Assume the number variable references a float value.)
# Write code for the function.
# result = half(number)

def main():
    num = 4.23
    result = half(num)
    print(f"Value: {result}")


def half(number):
    return number


main()