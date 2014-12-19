#-*- coding: utf-8 -*-
from django import forms
# from django_markdown.widgets import MarkdownWidget
from articles.models import Articles, Reviews


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'description', 'article', 'embeded',)

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
            'embeded': 'embeded',
        }

        widgets = {
            'title': forms.TextInput(attrs={'autofocus': '', 'required': ''}),
            'embeded': forms.TextInput(),
            'description': forms.Textarea(),
            'article': forms.Textarea(),
        }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('accept', 'notes',)

        widgets = {
            'notes': forms.TextInput(attrs={'autofocus': '', 'required': ''}),
        }

