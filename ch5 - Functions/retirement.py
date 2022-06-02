#Employee’s retirement gross pay
CONT_RATE = 0.05

def main():
    gross_pay = float(input("Enter the gross pay: $"))
    bonus =  float(input("Enter the amount of bonus: $"))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)


def show_pay_contrib(gross):
    contrib = gross * CONT_RATE
    print(f"Contribution for gross pay: ${format(contrib, '.2f')}", sep='')


def show_bonus_contrib(bonus):
    contrib = bonus * CONT_RATE
    print(f"Contribution for bonuses: ${format(contrib, '.2f')}", sep = '')


main()
