# Personal Information
# Write a program that displays the following information:
# • Your name
# • Your address, with city, state, and ZIP
# • Your telephone number
# • Your college major

name = input("Name: ")

own_address = input("Address: ")

tele_phone = int(input("Telephone No: "))

major_sub = input("Major subject: ")

print("         PERSONAL INFORMATION            ")

print("Name: " + name + "\n" + "Address: " + own_address + "\n" + "Telephone No: " +
      str(tele_phone) + "\n" + "Major Subject: " + major_sub)