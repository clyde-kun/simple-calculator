close = 'continue'

while close == 'continue':
    operation = input('What math operation will you be using? ')
    if operation == 'Addition':
        numbers = input("How many numbers will you be using? ")
        if numbers == "2":
            num1 = float(input('Number '))
            num2 = float(input('Plus '))
            print(num1 + num2)
        if numbers == "3": 
            num1 = float(input('Number '))
            num2 = float(input('Plus '))
            num3 = float(input('Plus '))
            print(num1 + num2 + num3)
        if numbers == "4": 
            num1 = float(input('Number '))
            num2 = float(input('Plus '))
            num3 = float(input('Plus '))
            num4 = float(input('Plus '))
            print(num1 + num2 + num3 + num4)
        if numbers == "5": 
            num1 = float(input('Number '))
            num2 = float(input('Plus '))
            num3 = float(input('Plus '))
            num4 = float(input('Plus '))
            num5 = float(input('Plus '))
            print(num1 + num2 + num3 + num4 + num5)

    if operation == 'Subtraction':
        numbers = input("How many numbers will you be using? ")
        if numbers == "2":
            num1 = float(input("Number "))
            num2 = float(input('Subracted '))
            print(num1 - num2)
        if numbers == "3":
            num1 = float(input("Number "))
            num2 = float(input('Subracted '))
            num3 = float(input('Subtracted by '))
            print(num1 - num2 - num3)
        if numbers == "4": 
            num1 = float(input('Number '))
            num2 = float(input('Subracted '))
            num3 = float(input('Subtracted by '))
            num4 = float(input('Subtracted by '))
            print(num1 - num2 - num3 - num4)
        if numbers == "5": 
            num1 = float(input('Number '))
            num2 = float(input('Subracted '))
            num3 = float(input('Subtracted by '))
            num4 = float(input('Subtracted by '))
            num5 = float(input('Subtracted by '))
            print(num1 - num2 - num3 - num4 - num5)
        
    if operation == 'Division':
        numbers = input("How many numbers will you be using? ")
        if numbers == "2":
            num1 = float(input("Number "))
            num2 = float(input("Divided by "))
            print(num1 / num2)
        if numbers == "3":
            num1 = float(input("Number "))
            num2 = float(input('Divided by '))
            num3 = float(input('Divided by '))
            print(num1 / num2 / num3)
        if numbers == "4": 
            num1 = float(input('Number '))
            num2 = float(input('Divided by '))
            num3 = float(input('Divided by '))
            num4 = float(input('Divided by '))
            print(num1 / num2 / num3 / num4)
        if numbers == "5": 
            num1 = float(input('Number '))
            num2 = float(input('Divided by '))
            num3 = float(input('Divided by '))
            num4 = float(input('Divided by '))
            num5 = float(input('Divided by '))
            print(num1 / num2 / num3 / num4 / num5)

    if operation == 'Multiplication':
        numbers = input("How many numbers will you be using? ")
        if numbers == "2":
            num1 = float(input('Number '))
            num2 = float(input("Multiplied by "))
            print(num1 * num2)
        if numbers == "3":
            num1 = float(input("Number "))
            num2 = float(input('Multiplied by '))
            num3 = float(input('Times '))
            print(num1 * num2 * num3)
        if numbers == "4": 
            num1 = float(input('Number '))
            num2 = float(input('Multiplied by '))
            num3 = float(input('Multiplied by '))
            num4 = float(input('Multiplied by '))
            print(num1 * num2 * num3 * num4)
        if numbers == "5": 
            num1 = float(input('Number '))
            num2 = float(input('Multiplied by '))
            num3 = float(input('Multiplied by '))
            num4 = float(input('Multiplied by '))
            num5 = float(input('Multiplied by '))
            print(num1 * num2 * num3 * num4 * num5)

    if operation == 'Exponentation':
        numbers = input("How many numbers will you be using? ")
        num1 = float(input("Number "))
        num2 = float(input("Raised to "))
        print(exp1 ** exp2)

    close = input("press enter to end program or type continue to perform another calculation ")


