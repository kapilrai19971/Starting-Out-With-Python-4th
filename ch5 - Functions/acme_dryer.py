#This program displays step-by-step instructions for disassembling an acme dryer
#main function performs the programs main logic

def main():
    #Displays the startup message
    startup_msg()
    input("Press Enter to see step 1.")
    step1()
    input("Press Enter to see step2.")
    step2()
    input("Press Enter to see step3.")
    step3()
    input("Press Enter to see step4.")
    step4()

def startup_msg():
    print('This program tells you how to')
    print('disassemble an ACME laundry dryer.')
    print('There are 4 steps in the process.')
    print()

def step1():
    print("step-1: Unplug the dyer and move it away from the wall. ")
    print()

def step2():
    print("Step-2: Remove the six screws from the back of dryer.")
    print()

def step3():
    print("Step-3: Remove the dryer's panel. ")
    print()

def step4():
    print("Step-4: Pull the top of the dryer straight up")

main()