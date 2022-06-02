# def main():
#     n = int(input("First Number: "))
#     n1 = int(input("Second Number: "))
#     total = add(n, n1)
#     print("Total: ",total)
#
#
# def add(x, y):
#     result = x + y
#     return result
#
#
# main()

# def main():
#     loop()
#
#
# def loop():
#     for i in range(5):
#         print(i * '*')
#
#
# main()

# def main():
#     value = int(input("Enter Number: "))
#     show_double(value)
#
#
# def show_double(number):
#     result = number * 2
#     print(f"Double of {number}: {result}")
#
#
# main()

# def send(message):
#     print(f"""Hello!
# {message}""")
#
#
# send("Everybody \nPlease wear mask while going outside or to work.\nThank You!")

# def main():
#     principal = float(input("Principal: $"))
#     time = float(input("Time: "))
#     rate = float(input("Rate: "))
#     total = simple_interest(principal, time, rate)
#     print("Simple interest: $", total)
#
#
# def simple_interest(p, t, r):
#     simpleInterst = p * t * r
#     return simpleInterst
#
#
# main()

# def adding():
#     a = 20
#     b = 30
#     total = a + b
#     print("After calling, sum: ", total)
#
#
# adding()

# def simpleInterest():
#     p = float(input("Principal: $"))
#     t = float(input("Time: "))
#     r = float(input("Rate: "))
#     si = (p * r * t)/ 100
#     print(f"Total simple interest of ${p} in {t} : ${si}")
#
#
# simpleInterest()
#
# def max_of_three():
#     num1 = float(input("Enter First Number: "))
#     num2 = float(input("Enter Second Number: "))
#     num3 = float(input("Enter Third Number: "))
#
#     if num1 > num2 and num1 > num3:
#         print(f"First number is greater number: {num1}")
#
#     elif num2 > num1 and num2 > num3:
#         print(f"Second number is greater number: {num2}")
#
#     elif num3 > num1 and num3 > num2:
#         print(f"Third number is greater number: {num3}")
#
#
# max_of_three()


# def simpleinterest():
#     p = float(input("Principal: $"))
#     t = float(input("Time: "))
#     r = float(input("Rate: "))
#     si = (p * t * r) / 100
#     return si
#
#
# print("Simple Interest: $", simpleinterest())


# def multiplication(a, b):
#     result = a * b
#     print("After calling the function: ", result)
#
#
# multiplication(3, 5)

# def simpleinterest(p, t, r):
#     si = (p * t * r) / 100
#     print("Simple Interest: ", si)
#
#
# simpleinterest(50000, 1, 10)

# def max_three_num(a, b, c):
#     if a > b and a > c:
#         print(f"First number is greater: {a}")
#
#     elif b > c and b > a:
#         print(f"Second number is greater: {b}")
#
#     elif c > a and c > b:
#         print(f"Third number is greater: {c}")
#
#
# max_three_num(5, 7, 3)

def addition(a, b):
    result = a + b
    return result

print("Addition: ", addition(25, 45))