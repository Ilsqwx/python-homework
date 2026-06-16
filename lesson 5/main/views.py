from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Головна</h1>")

def courses(request):
    return HttpResponse("<h1>Курси</h1><p>Python, Django</p>")

def teachers(request):
    return HttpResponse("<h1>Викладачі</h1><p>Іван, Марія</p>")

def contacts(request):
    return HttpResponse("<h1>Контакти</h1><p>Телефон: 123456</p>")