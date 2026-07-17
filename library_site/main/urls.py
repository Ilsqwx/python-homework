from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('stats/', views.stats, name='stats'),
    path('contacts/', views.contacts, name='contacts'),
]