jobs = [
    {"title": "Python Developer", "city": "Kyiv", "salary": 1200, "remote": True},
    {"title": "Frontend Developer", "city": "Lviv", "salary": 1000, "remote": False},
    {"title": "Backend Developer", "city": "Kyiv", "salary": 1500, "remote": True},
    {"title": "QA Engineer", "city": "Odesa", "salary": 900, "remote": False},
    {"title": "DevOps Engineer", "city": "Kharkiv", "salary": 1800, "remote": True},
    {"title": "UI/UX Designer", "city": "Lviv", "salary": 1100, "remote": True},
    {"title": "Data Analyst", "city": "Kyiv", "salary": 1300, "remote": False},
    {"title": "Project Manager", "city": "Dnipro", "salary": 1400, "remote": True},
    {"title": "Mobile Developer", "city": "Odesa", "salary": 1600, "remote": False},
    {"title": "System Administrator", "city": "Kharkiv", "salary": 800, "remote": True}
]

for job in jobs:
    print(job)

for job in jobs:
    if job["remote"]:
        print(job)

x = int(input())
for job in jobs:
    if job["salary"] > x:
        print(job)

city = input()
x = int(input())
for job in jobs:
    if job["city"] == city and job["salary"] > x:
        print(job)

total = 0
for job in jobs:
    total += job["salary"]
print(total / len(jobs))

max_job = jobs[0]
for job in jobs:
    if job["salary"] > max_job["salary"]:
        max_job = job

print(max_job)
