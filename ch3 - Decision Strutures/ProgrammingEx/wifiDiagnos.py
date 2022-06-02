#Wi-Fi Diagnostic Tree

print("Reboot the computer and try to connect.")
print("Type 'Y' for yes and 'N' for no.")

user_input = input("Did that fix the problem?  ")

if user_input == 'Y' or user_input == 'y' or user_input == 'N' or user_input == 'n':
    if user_input == 'n' or user_input == 'N':
        print("Reboot the router and try to connect.")
        user_input = input("Did that fix the problem?   ")

        if user_input == 'n' or user_input == 'N':
            print("Make sure the cables between the router & modem are plugged in firmly.")
            user_input = input("Did that fix the problem?   ")

            if user_input == 'n' or user_input == 'N':
                print("Move the router to a new location and try to connect.")
                user_input = input("Did that fix the problem?   ")

                if user_input == 'N' or user_input == 'n':
                    print("Get a new router.")

                else:
                    print("         Press 'y' or 'Y' for yes and 'n' or 'N' for No.         ")

            else:
                print("         Press 'y' or 'Y' for yes and 'n' or 'N' for No.         ")
        else:
            print("         Press 'y' or 'Y' for yes and 'n' or 'N' for No.         ")
    else:
        print("         Press 'y' or 'Y' for yes and 'n' or 'N' for No.         ")
else:
    print("         Press 'y' or 'Y' for yes and 'n' or 'N' for No.         ")

