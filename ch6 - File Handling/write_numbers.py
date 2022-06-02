#This program demonstrates how numbers must be converted to strings before they are written to a text file.


def main():
    #Open a file for writing.
    outfile = open('number.txt', 'w')

    #Get three numbers from the user.
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    num3 = int(input("Third number: "))

    #Write the numbers to the file.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    #Close the file.
    outfile.close()
    print("Data written to numbers.txt ")

#Call the main function.
main()