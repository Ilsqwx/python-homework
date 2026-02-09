import json
import os

event = input()
date = input()

if os.path.exists("events.json"):
    f = open("events.json", "r")
    data = json.load(f)
    f.close()
else:
    data = []

data.append({"event": event, "date": date})

f = open("events.json", "w")
json.dump(data, f)
f.close()