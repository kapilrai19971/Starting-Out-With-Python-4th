import circle
import rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():
    choice = 0

    while choice != QUIT_CHOICE:

        display_menu()

        choice = int(input("Enter your choice: "))

        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("Area of circle: ", format(circle.area(radius), ',.2f'), sep='')

        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("Circumference of circle: ", format(circle.circumference(radius), ',.2f'), sep='')

        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Width of rectangle: "))
            length = float(input("Length of rectangle: "))
            print("Area of rectangle: ", format(rectangle.area(width, length), ',.2f'), sep='')

        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Width of rectangle: "))
            length = float(input("Length of rectangle: "))
            print("Perimeter of rectangel: ", format(rectangle.perimeter(width, length), ',.2f'), sep='')

        elif choice == QUIT_CHOICE:
            print("Exiting the program......")

        else:
            print("Error: INVALID SELECTION")


def display_menu():
    print("##### MENU #####")
    print("1) Area of circle")
    print("2) Circumference of circle")
    print("3) Area of rectangle")
    print("4) Perimeter of rectangle")
    print("5) Quit")


main()
