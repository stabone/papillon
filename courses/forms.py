#-*- coding: utf-8 -*-
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
            'course': forms.TextInput(attrs={'class': 'editor'}),
        }

class TutForm(forms.ModelForm):
    class Meta:
        model = Tuts
        exclude = ('author',)
        labels = {
                'category': 'Kategorija',
                # 'author': 'Autors',
                'title': 'Nosaukums',
                'description': 'Apraksts',
                'level': 'Limenis',
                'rating': 'Vertejums',
                'times_rated': 'Vērtēts',
                'tags': 'Birkas',
                'post': 'Publicet',
        }
        widgets = {
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        labels = {
            'tut': 'Materiāla nosaukums',
            'title': 'Nosaukums',
            'description': 'Apraksts',
            'video': 'Video',
            'post': 'Publicēt'
        }
