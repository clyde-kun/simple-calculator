operation = input('What math operation will you be using? ')

if operation == 'Addition':
    add1 = float(input('Number '))
    add2 = float(input('Plus '))
    print(add1 + add2)

if operation == 'Subtraction':
    sub1 = float(input("Number "))
    sub2 = float(input('Subracted '))
    print(sub1 - sub2)

if operation == 'Division':
    div1 = float(input("Number "))
    div2 = float(input("Divided by "))
    print(div1 / div2)

if operation == 'Multiplication':
    mul1 = float(input('Number '))
    mul2 = float(input("Multiplied by "))
    print(mul1 * mul2)

if operation == 'Exponentation':
    exp1 = float(input("Number "))
    exp2 = float(input("Raised to "))
    print(exp1 ** exp2)

close = input("press enter to end program")
