#-*- coding: utf-8 -*-
from django import forms
# from django_markdown.widgets import MarkdownWidget
from articles.models import Articles, ArticleReviews


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'category', 'description', 'article', 'embeded',)

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
            'category': 'Kategorija',
            'description': 'Apraksts',
            'article': 'Raksts',
            'embeded': 'Video',
        }

        widgets = {
            'title': forms.TextInput(attrs={'autofocus': '', 'required': ''}),
            'embeded': forms.TextInput(),
            'description': forms.Textarea(),
            'article': forms.Textarea(attrs={'id': 'wsiwg-editor'}),
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ArticleReviews

        fields = ('accept', 'notes',)

        widgets = {
            'notes': forms.TextInput(attrs={'autofocus': '', 'required': ''}),
        }

