def info(*agrs):
    fname = input("First Name: ")
    lname = input("Last Name: ")
    paddress = input("Permanent Address: ")
    taddress = input("Temporary Address: ")
    emp_id = int(input("Employee ID: "))
    p_no = int(input("Phone Number: "))
    email_id = input("Email: ")

    print("################EMPLOYEE INFORMATION SYSTEM########################")
    print("--------------------------Employee Details------------------------------------")
    print("First Name: ", fname)
    print("Last Name: ", lname)
    print("Permanent Address: ", paddress)
    print("Temprary Address: ", taddress)
    print("Employee ID: ", emp_id)
    print("Phone Number: ", p_no)
    print("Email: ", email_id)


info('Ram', 'Kumar', 'Dhankuta', 'Kathmandu', 22021, 9842304480, 'realsuuraj@gmail.com')