def main():
    #opeing file name info.txt
    infofile = open('info.txt', 'w')
    #write the name of employee to the file
    infofile.write("John Smith\n")
    infofile.write("Manoj Kimdahang\n")


    infofile.close()


main()


def read():
    ram = open('info.txt', 'r')
    file_contents = ram.read()

    ram.close()

    print(file_contents)


read()