# Starting with a variable text containing an empty string, write a loop that prompts
# the user to type a word. Add the user’s input to the end of text and then print the
# variable. The loop should repeat while the length of text is less than 10 characters.
emptyStr = "" #Getting empty string
while len(emptyStr) < 10: # condition
    emptyStr = input("Enter word: ") # Taking user input
    print(emptyStr) # Printing statement
    print(len(emptyStr)) # Printing length of string
else: # else part
    print("Your word is too long.") # Outside the loop