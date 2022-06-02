#Program to illustrate append vs write mode.

file2 = open("myfile2.txt", "w")
L = ["This is Kathmandu. \n", "This is Paris. \n", "This is London. \n"]

file2.writelines(L)
file2.close()

#Append-adds at last

file2 = open("myfile2.txt", "a")
file2.write("Today \n")
file2.close()

file2 = open("myfile2.txt", "r")
print("Output of Readlines after appending")
print(file2.readlines())
print()
file2.close()

#Write over writes
file2 = open("myfile2.txt", "w")
file2.write("Tomorrow \n")
file2.close()

file2 = open("myfile2.txt", "r")
print("Output of Readlines after writing")
print(file2.readlines())
print()
file2.close()
