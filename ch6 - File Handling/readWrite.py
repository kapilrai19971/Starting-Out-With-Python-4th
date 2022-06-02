#Writing data in a file

file1 = open("myfile.txt", "w")

L = ["This is kathmandu. \n", "This is Paris. \n", "This is London \n"]

#\n is placed to indicate EOL(End of Line)

file1.write("Hello \n")
file1.writelines(L)
file1.close() # To change file access modes

file1 = open("myfile.txt", "r+")

print("Output of read function is")
print(file1.read())
print()

#seek(n) takes the file handle to th nth bite from the beginning
file1.seek(0)

#To show difference betwn read and readlines

print("Output of Read(9) function is")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readlines(9) function is")
print(file1.readline(9))

file1.seek(0)

#readlines function

print("Output of Readlines function is")
print(file1.readlines())
print()

file1.close()
