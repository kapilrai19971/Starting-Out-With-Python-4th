# def main():
#     f_name, l_name = get_name()
#     print("First Name: ",f_name,'\n',"Last Name: ", l_name)
#
#
# def get_name():
#     first_name = input("Enter your First Name: ")
#     last_name = input("Enter your Second Name: ")
#
#     return first_name, last_name
#
#
# main()
#
# def even(n):
#     is_even(number)
#     if (n % 2) == 0:
#         status = True
#
#     else:
#         status = False
#
#     return status
#
# def is_even(number):
#     num = int(input("Enter a number: "))
#     if (num % 2) == 0:
#         print("Even")
#
#     else:
#         print("Odd")
#
#
#
# is_even()

def is_even(number):
    if (number%2)==0:
        status=True
    else:
        status=False
    return status

number=int(input("Enter a number: "))

if is_even(number):         # means that if the result of this function is True.
    print("The number is even")
else:
    print("The number is odd.")