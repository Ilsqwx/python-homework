from django.contrib import admin
from .models import Vacancy, Article


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "location",
        "salary",
        "created_at",
    )

    search_fields = (
        "title",
        "company",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "-created_at",
    )