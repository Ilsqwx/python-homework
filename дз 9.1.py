while True:
    try:
        int(input("enter a number: "))
        break
    except ValueError:
        print("Invalid input")

print("Thank you for entering a valid number!")