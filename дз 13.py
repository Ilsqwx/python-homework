class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_info(self):
        print(self.name, self.age, self.course)
    
    def change_course(self , new_course):
        self.course = new_course


class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def show(self):
        print(f"{self.title} | Completed: {self.completed}")


class Event:
    def __init__(self, title , date):
        self.title = title
        self.date = date
        self.description = ""

    def show(self):
        print(f"Event: {self.title} / Date: {self.date} / Desc: {self.description}")

    def update_description(self, new_description):
        self.description = new_description



task1 = Task("Do homework")
task2 = Task("Go to gym")
task3 = Task("Read book")

task2.mark_done()


event1 = Event("Meeting", "2026-02-17")

student1 = Student("anya", 18, 1)
student2 = Student("lev", 20, 2)


student1.change_course(3)

event1.update_description("Important meeting with team")


student1.show_info()
student2.show_info()

task1.show()
task2.show()
task3.show()

event1.show()


