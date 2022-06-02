def main():
    principal = get_principal()
    time = get_time()
    rate = get_rate()
    si = (principal * time * rate) / 100
    print("Simple Interest: $", format(si,',.2f'), sep='')


def get_principal():
    p = float(input("Principal: $"))
    return p


def get_time():
    t = float(input("Time(in years): "))
    return t


def get_rate():
    r = float(input("Rate: "))
    return r


main()