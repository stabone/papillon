#-*- coding: utf-8 -*-
from django import forms

from categories.models import Categories


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories

        fields = ('title',)

        labels = {
            'title': 'Nosaukums',
        }

        widgets = {
            'title': forms.TextInput(attrs={'autofocus': '', 'required': ''}),
        }

