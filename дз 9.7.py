while True:
    try:
        num1 = int(input("enter a number:"))
        if num1 < 0:
            print("Please enter a non-negative number.")
            continue
        break
    except ValueError:
        print("Invalid input")

while True:
    try:
        num2 = int(input("enter a number:"))
        if num2 < 0:
            print("Please enter a non-negative number.")
            continue
        break
    except ValueError:
        print("Invalid input")

try:
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")