#-*- coding: utf-8 -*-
from django import forms
# from django_markdown.widgets import MarkdownWidget
from articles.models import Articles


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Articles
        exclude = ('user',)

        error_messages = {
            'title': {
                'required': 'Lauks ir obligāti jāaizpilda',
                'max_length': 'Maksimālais garums ir 255 simboli',
            },
            'description': {
                'required': 'Lauks ir obligāti jāaizpilda',
                'max_length': 'Maksimālais garums ir 255 simboli',
            },
        }

        labels = {
            'title': 'Virsraksts',
            'description': 'Apraksts',
            'article': 'Raksts',
        }

        widgets = {
            'title': forms.TextInput(attrs={'autofocus': '', 'required': ''}),
            'description': forms.Textarea(),
            'article': forms.Textarea(),
        }
