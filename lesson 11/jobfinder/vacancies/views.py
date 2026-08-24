from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacancies
from .forms import VacancyForm
from django.core.paginator import Paginator


def vacancy_list(request):
    vacancies = Vacancies.objects.all()

    search = request.GET.get('q')

    if search:
        vacancies = vacancies.filter(title__icontains=search)

    paginator = Paginator(vacancies, 10)
    page = request.GET.get('page')
    vacancies = paginator.get_page(page)

    return render(request, 'vacancies/index.html', {
        'vacancies': vacancies
    })


def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancies, id=id)

    return render(request, 'vacancies/detail.html', {
        'vacancy': vacancy
    })


def add_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm()

    return render(request, 'vacancies/add_vacancy.html', {
        'form': form
    })


def edit_vacancy(request, id):
    vacancy = get_object_or_404(Vacancies, id=id)

    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)

        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm(instance=vacancy)

    return render(request, 'vacancies/add_vacancy.html', {
        'form': form
    })


def delete_vacancy(request, id):
    vacancy = get_object_or_404(Vacancies, id=id)

    if request.method == 'POST':
        vacancy.delete()
        return redirect('vacancy_list')

    return render(request, 'vacancies/delete.html', {
        'vacancy': vacancy
    })