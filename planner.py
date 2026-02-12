import os
import json

FILE_NAME = "planner.json"

def load_events():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            planner = json.load(file)

        if not planner:
            return {}, 1

        next_id = max(int(key) for key in planner.keys()) + 1
        return planner, next_id
    except FileNotFoundError:
        return {}, 1
 

def save_events(planner):
    with open(FILE_NAME , "w", encoding="utf-8") as file:
        json.dump(planner , file , indent = 4, ensure_ascii=False)

def add_event(planner, event_id):
    e_name = input("Enter name of your event: ")
    e_date = input("Enter date (YYYY-MM-DD): ")
    e_time = input("Enter time (HH:MM): ")
    e_description = input("Enter description: ")

    planner[str(event_id)] = {
        "title": e_name,
        "date": e_date,
        "time": e_time,
        "description": e_description
    }

    save_events(planner)
    return event_id + 1


def show_events(planner, event_id):
    if planner == {}:
        print("file data is empty")
        return

    for event_id, event in planner.items():
        print("ID:", event_id)
        print("Title:", event["title"])
        print("Date:", event["date"])
        print("Time:", event["time"])
        print("Description:", event["description"])


def delete_event(planner):
    if planner == {}:
        print("no data to delete")
        return

    for event_id in planner:
        print(event_id)

    print("what event would u like to delete")
    delete_id = input("enter id to delete : ")

    if delete_id in planner:
        del planner[delete_id]
        save_events(planner)
        print("deleted")
    else:
        print("Not Found")


def find_by_date(planner):
    date = input("Enter date (YYYY-MM-DD): ")

    found = False

    for event_id, event in planner.items():
        if event["date"] == date:
            print("ID:", event_id)
            print("Title:", event["title"])
            print("Date:", event["date"])
            print("Time:", event["time"])
            print("Description:", event["description"])
            found = True

    if found == False:
        print("No events found for this date.")


def main():
    planner, event_id = load_events()

    while True:
        print("\n1 - Add event")
        print("2 - Show events")
        print("3 - Delete event")
        print("4 - Find by date")
        print("5 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            event_id = add_event(planner, event_id)
        elif choice == "2":
            show_events(planner, event_id)
        elif choice == "3":
            delete_event(planner)
        elif choice == "4":
            find_by_date(planner)
        elif choice == "5":
            break
        else:
            print("Wrong choice")


if name == "__main__":
    main()