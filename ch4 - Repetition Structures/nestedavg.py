subject = int(input('Enter total subjects: '))
print('Following are the subject per exam.')
print("1.English\t2.Nepali\t3.Math\t4.Science\t5.Social Studies")
student = int(input('Enter total student: '))
print('--------------------')
for std in range(1, student+1):
    print('Student',std)
    print('------------------')
    std_name = input('Enter Student Name: ')
    total = 0.0
    for sub in range(1, subject +1):
        score = int(input(f'Enter score {sub}: '))

        total += score
    avg = total / subject
    print('Name: ', std_name)
    print('Total marks obtain',total)
    print('Average: ', format(avg, '.2f'))
    print()