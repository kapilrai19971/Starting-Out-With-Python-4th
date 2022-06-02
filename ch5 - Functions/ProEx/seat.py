#Stadium Seating

def std_seating():
    print("Total Seat on stdium is 1000000")
    class_a = get_class_a()

    class_b = get_class_b()

    class_c = get_class_c()

    total_seat = add(class_a , class_b, class_c)

    total_sold_amt = (class_a * 20) + (class_b * 15) + (class_c * 10)

    print()
    print("Total seats tickets sold: ", total_seat)
    print()
    print("Total tickets sold amount: $", format(total_sold_amt, ',.2f'), sep='')


def get_class_a():
    classA = float(input("Enter total tickets sold of Class-A: "))
    return classA


def get_class_b():
    classB = float(input("Enter total tickets sold of Class-B: "))
    return classB


def get_class_c():
    classC = float(input("Enter total tickets sold of Class-C: "))
    return classC


def add(class_a, class_b, class_c):
    return (class_a + class_b + class_c)


std_seating()
    


