# Write a set of nested loops that displays the first ten values of the multiplication tables
# from 1 to 10. The code should print 100 lines in total, starting at “1 3 1 5 1” and
# ending with “10 * 10 = 100”.

print("Multiplication table : ")
for i in range(1, 11):
    for j in range (1,11):
        print(i , "*" , j , "=" ,i * j)


    # print("2" , "*" , i ,"=", 2 * i)