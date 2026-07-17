from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def stats(request):
    return render(request, 'stats.html')


def contacts(request):
    return render(request, 'contacts.html')