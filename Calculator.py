# Give instructions for the calculator
print("This calculator supports +, -, *, / exponents and square rooting\nTo use exponents type \"pow\" in the option\nTo use square rooting type \"sqrt\" in the options")
# Keeps on running
while True:
    try:
# Make the ptions work
        from math import *
        num1 = float(input("Enter a number: "))
        Option = input("Enter an option: ")
        if Option == "sqrt":
            print(sqrt(num1))
        elif Option == "pow":
            Exponent_num = float(input("Enter a exponent: "))
            print(pow(num1, Exponent_num))
        elif Option == "+":
            num2 = float(input("Enter another number: "))
            print(num1 + num2)
        elif Option == "-":
            num2 = float(input("Enter another number: "))
            print(num1 - num2)
        elif Option == "*":
            num2 = float(input("Enter another number: "))
            print(num1 * num2)
        elif Option == "/":
            num2 = float(input("Enter another number: "))
            print(num1 / num2)
        else:
            print("Invalid Option")
# prints invalid input if he puts a non int
    except:
        print("Invalid Input")
