from django.shortcuts import render

jobs = [
    {
        "id": 1,
        "title": "Python Developer",
        "company": "SoftServe",
        "salary": "2500$",
        "description": "Розробка backend на Django"
    },
    {
        "id": 2,
        "title": "Frontend Developer",
        "company": "EPAM",
        "salary": "2200$",
        "description": "Створення сучасих вебсайтів"
    },
    {
        "id": 3,
        "title": "QA Engineer",
        "company": "GlobalLogic",
        "salary": "1800$",
        "description": "Тестування вебзастосунків"
    }
]

def index(request):
    context = {
        "jobs": jobs
    }
    return render(request, "jobs/index.html", context)


def detail(request, id):
    job = next(job for job in jobs if job["id"] == id)
    context = {
        "job": job
    }
    return render(request, "jobs/detail.html", context)