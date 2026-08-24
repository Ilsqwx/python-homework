from django import forms
from .models import Vacancies


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = [
            'title',
            'company',
            'location',
            'salary',
            'description',
            'source_url',
        ]