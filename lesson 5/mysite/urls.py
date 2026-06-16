from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('courses/', views.courses),
    path('teachers/', views.teachers),
    path('contacts/', views.contacts),
]