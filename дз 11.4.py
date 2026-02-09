import os

filename = "text.txt"

if os.path.exists(filename):
    with open(filename, "r") as f:
        content = f.read()
        print(content)
else:
    print(f"The file {filename} does not exist.")