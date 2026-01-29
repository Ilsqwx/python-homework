try:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))

    choise = input("enter +, -, *, /: ")

    if choise == "+":
        print(num1 + num2)
    elif choise == "-":
        print(num1 - num2)
    elif choise == "*":
        print(num1 * num2)
    elif choise == "/":
        print(num1 / num2)
    else:
        print("Invalid operation")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero") 