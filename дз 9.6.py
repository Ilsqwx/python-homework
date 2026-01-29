UAH.Rate = 45

try:
    amout = float(input("Enter the amout: "))
    result = amout * rate 
    print("Result:", result)
except ValueError:
    print("Invalid input")
    