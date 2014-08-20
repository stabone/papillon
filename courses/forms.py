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
            'course': forms.TextInput(attrs={'class': 'editor', 'autofocus': ''}),
        }

class TutForm(forms.ModelForm):

    class Meta:
        model = Tuts
        exclude = ('author', 'rating', 'times_rated', 'post',)
        labels = {
            'category': 'Kategorija',
            'title': 'Nosaukums',
            'description': 'Apraksts',
            'level': 'Limenis',
            'rating': 'Vertejums',
            'times_rated': 'Vērtēts',
            'tags': 'Birkas',
            # 'post': 'Publicet',
        }
        widgets = {
            'title': forms.TextInput(attrs={'autofocus': ''})
        }

class MaterialForm(forms.ModelForm):

    class Meta:
        model = Materials
        exclude = ('post',)
        labels = {
            'tut': 'Materiāla nosaukums',
            'title': 'Nosaukums',
            'description': 'Apraksts',
            'video': 'Video',
            'post': 'Publicēt'
        }
        widgets = {
            'title': forms.TextInput(attrs={'autofocus': ''})
        }
