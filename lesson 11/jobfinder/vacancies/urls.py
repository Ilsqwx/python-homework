from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancy_list, name='vacancy_list'),
    path('<int:id>/', views.vacancy_detail, name='vacancy_detail'),
    path('add/', views.add_vacancy, name='add_vacancy'),
    path('<int:id>/edit/', views.edit_vacancy, name='edit_vacancy'),
    path('<int:id>/delete/', views.delete_vacancy, name='delete_vacancy'),
]