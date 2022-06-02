# Grade Calculator

test1 = int(input("Enter First test point: "))
# Valid
if test1 >= 0 and test1 <=25:
    # Valid
    test2 = int(input("Enter Second test point: "))

    if test2 >= 0 and test2 <= 25:
        # Valid
        mark = int(input("Main exam mark: "))

        if mark >= 0 and mark <= 50:
        #Valid
            test = test1 + test2
            total = test + mark
            if mark < 50 and test < 25:
               print("Fail")

            elif total > 80:
               print("Distinction.")
            elif total >= 60 and total <= 80:
               print("Credit")

            elif total < 60:
               print("Pass.")
            else:
                print("Error.")
        else:
            print("Error")
    else:
        print("Error")

else:
    print("Error.")