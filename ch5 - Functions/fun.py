#Void Function
#Defining function named message
#
# def message():
#     print('Hello! ')            #statement cause the message function to be created
#     print('I am Kapil Rai.')
#
# message() # statement calls the message function, causing it to execute

# Indentation in function
# def greet():
#     print("Hello!")
#     print("Namaste ")
#
# print("Shuvratri ")
# greet()
# def main():
#     print("INFORMATION")
#     info()
#     print("Thank you for visiting.")
# def info():
#     name = input("Name: ")
#     add = input("Address: ")
#     ph_no = int(input("Phone No: "))
#     sex = input("Sex: ")
#     age = int(input("Age: "))
#     print("             Hospital Management System              ")
#     print(f"Name: {name}\nAddress: {add}\nPhone No: {ph_no}\nSex: {sex}\nAge: {age}")
# main()
#
# def greet_user(first_name , last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome Aboard")
#
#
# print("Start")
# greet_user("John", "Smith")
# greet_user("Mary", "Kom")
# print("Finish")
#
# def greet_user(f_name, l_name):
#     print(f"Hi {f_name} {l_name}")
#     print("Welcome aboard")
#
# print("Start")
# greet_user(l_name = "Rai", f_name= "Manoj")
# print("Finish")

# Calculation total cost:
# total cost = $50
# shipping cost = $5
# discount = 0.1
# def calc_total(cost, shipping, discount):
#     total = cost + shipping - (cost * discount)
#     print(f"Total cost: ${total}")
#
#
# # print("Start")
# calc_total(cost = 50, shipping= 5, discount = 0.1)
# # print("Finish")
#
# def show_value(quantity):
#     print(quantity)
#
#
# show_value(12)
# def main():
# #     value = 5
# #     show_double(value)
# #
# #
# # def show_double(number):
# #     total = number * 2
# #     print(f"Total: {total}")

#
# main()
#
# def main():
#     number = 50
#     double(number)
#
#
# def double(number):
#     result = number * 2
#     print(result)
#
# main()

# def sum(num1 , num2):
#     result = num1 + num2
#     print(f"The sum of {num1} and {num2} is {result}.")
#
#
# sum(12, 45)

#
# def main():
#     print("The sum of 12 and 45 is")
#     sum(12, 45)
#
# def sum(num1, num2):
#     result = num1 + num2
#     print(result)
#
# main()

# def main():
#     fname = input("Enter your first name: ")
#     lname = input("Enter your last name: ")
#     print("Your reversed name is ")
#     reverse(fname, lname)
#
# def reverse(first, last):
#     print(last, first)
#
#
# main()

# using Global Constants
def main():
    num = int(input("Enter the number: "))
    square(num) 


def square(number):
    result = number * number
    print(f"Square: {result}")


main()
