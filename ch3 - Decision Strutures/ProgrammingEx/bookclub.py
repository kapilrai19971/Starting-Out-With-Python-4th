#Book Club Points

print("          Serendipity Booksellers Book Club            ")

book_purchased = int(input("No. of book purchased: "))

if book_purchased == 0:
    print("Points: 0 ")

elif book_purchased <= 2:
    print("Points: 5 ")

elif book_purchased <= 4:
    print("Points: 15 ")

elif book_purchased <= 6:
    print("Points: 30 ")

elif book_purchased >= 8:
    print("Points: 60 ")

