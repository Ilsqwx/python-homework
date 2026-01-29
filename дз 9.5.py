try:
    f = open("numbers.txt")
    f.read()
    f.close()
except FileNotFoundError:
    print("File not found. Please check the file path.")