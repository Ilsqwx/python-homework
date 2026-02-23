class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def show(self):
        print("Event:", self.title, self.date)

    def get_info(self):
        return "Event: " + self.title + " " + self.date


class Training(Event):
    def __init__(self, title, date, trainer):
        self.title = title
        self.date = date
        self.trainer = trainer

    def show(self):
        print("Training:", self.title, self.date, self.trainer)

    def get_info(self):
        return "Training: " + self.title + " " + self.date + " " + self.trainer


class Birthday(Event):
    def __init__(self, title, date, person):
        self.title = title
        self.date = date
        self.person = person

    def show(self):
        print("Birthday:", self.title, self.date, self.person)

    def get_info(self):
        return "Birthday: " + self.title + " " + self.date + " " + self.person


class OnlineEvent(Event):
    def __init__(self, title, date, link):
        self.title = title
        self.date = date
        self.link = link

    def show(self):
        print("OnlineEvent:", self.title, self.date, self.link)

    def get_info(self):
        return "OnlineEvent: " + self.title + " " + self.date + " " + self.link


events = [
    Event("Meeting", "25.02"),
    Training("Python", "26.02", "Alex"),
    Birthday("Party", "01.03", "Max"),
    OnlineEvent("Webinar", "05.03", "zoom.com")
]

for i in events:
    i.show()

for i in events:
    print(i.get_info())