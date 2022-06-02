# 8. Average Word Length
# Write a program with a loop that repeatedly asks the user to enter a word. The user should
# enter nothing (press Enter without typing anything) to signal the end of the loop. Once the
# loop ends, the program should display the average length of the words entered, rounded to
# the nearest whole number.

word = 0
total_length = 0
no_of_word = 0

while word != '':
    word = input("Enter the word: ")
    no_of_word += 1

    for char in (word):
        total_length += 1
avg_length = total_length / no_of_word
print(no_of_word)
print(total_length)
print('Total average length of word: ', round(avg_length))

