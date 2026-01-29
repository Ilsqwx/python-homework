numbers = [10,20,30,40,50]

try:
    index = int(input("enter an index: "))
    print(f"number at index {index} is {numbers[index]}")
except ValueError:
    print("Invalid input: Please enter an integer.")
except IndexError:
    print("Index out of range: Please enter a valid index.")
    