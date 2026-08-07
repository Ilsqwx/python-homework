from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vacancies/", views.vacancies, name="vacancies"),
    path("vacancy/<int:id>/", views.vacancy_detail, name="vacancy_detail"),
    path("articles/", views.articles, name="articles"),
    path("articles/<int:id>/", views.article_detail, name="article_detail"),
    path("add-article/", views.add_article, name="add_article"),
    path("about/", views.about, name="about"),
]