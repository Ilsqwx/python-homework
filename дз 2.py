tasks = []

while True:
    print("\n1 - Показати задачі")
    print("2 - Додати задачу")
    print("3 - Видалити задачу")
    print("4 - Редагувати задачу")
    print("5 - Пошук")
    print("6 - Сортування")
    print("0 - Вихід")

    choice = input("Вибери: ")

    if choice == "1":

        if len(tasks) == 0:
            print("Задач нема")

        for i in range(len(tasks)):
            print(i + 1, tasks[i]["title"], "-", tasks[i]["priority"])



    elif choice == "2":

        title = input("Назва задачі: ")
        priority = input("Пріоритет low/medium/high: ")

        task = {
            "title": title,
            "priority": priority
        }

        tasks.append(task)

        print("Задачу додано")



    elif choice == "3":

        for i in range(len(tasks)):
            print(i + 1, tasks[i]["title"])

        number = int(input("Номер задачі: "))

        if number > 0 and number <= len(tasks):
            tasks.pop(number - 1)
            print("Задачу видалено")



    elif choice == "4":

        for i in range(len(tasks)):
            print(i + 1, tasks[i]["title"])

        number = int(input("Яку задачу редагувати: "))

        if number > 0 and number <= len(tasks):

            new_title = input("Нова назва: ")
            new_priority = input("Новий пріоритет: ")

            tasks[number - 1]["title"] = new_title
            tasks[number - 1]["priority"] = new_priority

            print("Задачу змінено")



    elif choice == "5":

        word = input("Що знайти: ")

        for task in tasks:

            if word.lower() in task["title"].lower():
                print(task["title"], "-", task["priority"])



    elif choice == "6":

        for i in range(len(tasks)):

            for j in range(len(tasks) - 1):

                if tasks[j]["priority"] > tasks[j + 1]["priority"]:

                    temp = tasks[j]
                    tasks[j] = tasks[j + 1]
                    tasks[j + 1] = temp

        print("Задачі відсортовано")



    elif choice == "0":
        break



    else:
        print("Неправильний вибір")