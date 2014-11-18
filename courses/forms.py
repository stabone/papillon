#-*- coding: utf-8 -*-
# from django.forms import ModelForm
from django import forms

from courses.models import Categories, Tuts, Materials


class CategoryForm(forms.ModelForm):

    class Meta:

        model = Categories

        fields = ('course',)

        labels = {
            'course': 'Nosaukums',
        }

        widgets = {
            'course': forms.TextInput(attrs={'class': 'editor', 'autofocus': ''}),
        }


class TutForm(forms.ModelForm):

    class Meta:

        model = Tuts

        fields = ('category', 'title', 'description',
                    'level', 'tags', 'post',)

        labels = {
            'category': 'Kategorija',
            'title': 'Nosaukums',
            'description': 'Apraksts',
            'level': 'Limenis',
            'tags': 'Birkas',
            'post': 'Publicet',
        }

        widgets = {
            'title': forms.TextInput(attrs={'autofocus': ''})
        }


class MaterialForm(forms.ModelForm):

    class Meta:

        model = Materials

        fields = ('tut', 'title', 'description', 'video', 'post',)

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

