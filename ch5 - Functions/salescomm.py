# def main():
#     num = int(input("Enter a number: "))
#     is_even(num)
#     if (num % 2) == 0:
#         print("Even.")
#
#     else:
#         print("Odd.")
#
#
# def is_even(n):
#     if (n % 2) == 0:
#         status = True
#
#     else:
#         status = False
#
#     return status



# def is_even(number):
#     if (number % 2) == 0:
#         print("The number is even.")
#
#     else:
#         print("The number is odd.")
#
#     return number
#

# main()
def is_even(number):
    if (number % 2) == 0:
        status = True
    else:
        status = False
    return status

num = int(input("Number: "))
if is_even(num):
    print("Even.")
else:
    print("Odd.")



