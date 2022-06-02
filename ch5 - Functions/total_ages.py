def main():
    age = int(input("Enter your age: "))

    friend_age = int(input("Enter your best friend age: "))

    total = add(age, friend_age)

    print("Together you are", total, "year old.")


def add(age, friend_age):
    result = age + friend_age
    return result


main()