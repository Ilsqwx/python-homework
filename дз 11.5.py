a = int(input())
b = int(input())
result = a + b

f = open("calc.txt", "a")
f.write(f"{a} + {b} = {result}\n")
f.close()

print(result)