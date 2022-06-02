#if- else statement solution

score = float(input("Enter score: \n"))

if score >= 80:
    print("Your grade is A.")
else:
    if score >= 65:
        print("Your grade is B.")
    else:
        if score >= 50:
            print("Your grade is C.")
        else:
            if score >= 40:
                print("Your grade is D.")

            else:
                print("Your grade is F.")