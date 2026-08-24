from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm


def home(request):
    return render(request, 'home.html')


def author(request):
    return render(request, 'author.html')


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})


def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movie_detail.html', {'movie': movie})


def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies')
    else:
        form = MovieForm()

    return render(request, 'movie_form.html', {
        'form': form,
        'title': 'Додати фільм'
    })


def movie_edit(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movie_form.html', {
        'form': form,
        'title': 'Редагувати фільм'
    })


def movie_delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    movie.delete()
    return redirect('movies')