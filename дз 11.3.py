login = input("Enter your login: ")
password = input("Enter your password: ")

with open("users.txt", "a") as f:
    f.write(f"{login}:{password}\n")
print("User registered successfully!")
