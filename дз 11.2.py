grades = []

with open("marks.txt", "r") as f:
    for line in f:
        if line.strip() != "":
            grades.append(int(line))

if grades:
    average = sum(grades) / len(grades)
    print(average)
else:
    print("Файл пуст")