name = input("Enter your name: ")
while True:
    try:
        age = int(input("Enter your age: "))
        if age >= 1 and age <= 120:
            break
        else :
            print("Age must be between 1 and 120.")
            continue
            
    except ValueError:
        print("Invalid age. Please enter a number between 1 and 120.")