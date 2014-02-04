# from django.forms import ModelForm
from django import forms

from courses.models import Categories, Tuts, Materials


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        labels = {
            'course': 'Nosaukums',
        }
        widgets = {
            'course': forms.TextInput(attrs={'class': 'cat'}),
        }

class TutForm(forms.ModelForm):
    class Meta:
        model = Tuts
        labels = {
                'categorie_id': 'Kategorija',
                'title': 'Nosaukums',
                'description': 'Apraksts',
                'level': 'Limenis',
                'rating': 'Vertejums',
                'times_rated': 'Vertets',
                'tags': 'Birkas',
                'post': 'Publicet',
        }
        widgets = {
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
