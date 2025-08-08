"""
📅 Day 2 – Simple Calculator
Goal: Support +, -, *, / operations using user input

Concepts: Loops, conditionals, functions, error handling
"""
print("Simple calculator")
try :
    while True:
        print("Enter which operation you want to perform  :\n1. +\n2. -\n3. *\n4./\n")
        operation = int(input("Enter choice in integers :"))
        num = []
        for i in range(2):
            numm = int(input(f"Enter {i+1} number :"))
            num.append(numm)

        if operation == 1:
            result = sum(num)
            print(f"Addition of {num[0]} and {num[1]} is {result}")
            print()
            opt = input("Want to continue operation or exit (continue/exit)  :")
            if opt == "continue":
                continue
            elif opt == "exit":
                break
        elif operation == 2:
            result = num[0]-num[1]
            print(f"Subtraction of {num[0]} and {num[1]} is {result}")
            print()
            opt = input("Want to continue operation or exit (continue/exit)  :")
            if opt == "continue":
                continue
            elif opt == "exit":
                break

        elif operation == 3:
            result = num[0] * num[1]
            print(f"Multiplication of {num[0]} and {num[1]} is {result} ")
            print()
            opt = input("Want to continue operation or exit (continue/exit)  :")
            if opt == "continue":
                continue
            elif opt == "exit":
                break
        elif operation == 4:
            result = num[0] / num[1]
            print(f"Division of {num[0]} and {num[1]} is {result}")
            print()
            opt = input("Want to continue operation or exit (continue/exit)  :")
            if opt == "continue":
                continue
            elif opt == "exit":
                break
        else :
            print("Invalid operation number ")

except ValueError:
    print("Invalid input. Please enter a number.")