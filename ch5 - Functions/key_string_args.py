#This program demonstrate passing two stings as keyword arguments to a function.

def main():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    print("Your reversed name is ")
    reverse_name(last = last_name, first = first_name)

def reverse_name(first, last):
    print(last, first)

main()
