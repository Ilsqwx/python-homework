text = input("Enter a string: ")

with open("output.txt", "a") as file:
    file.write(text + "\n")