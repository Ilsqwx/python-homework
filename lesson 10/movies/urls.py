from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movies'),
    path('add/', views.movie_add, name='movie_add'),
    path('<int:id>/', views.movie_detail, name='movie_detail'),
    path('edit/<int:id>/', views.movie_edit, name='movie_edit'),
    path('delete/<int:id>/', views.movie_delete, name='movie_delete'),
]