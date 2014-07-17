#-*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from polls.models import Polls, Questions, Choises

class PollForm(ModelForm):
    class Meta:
        model = Polls
        exclude = ('user',)
        labels = {
            'poll': 'Virsraksts',
            'description': 'Apraksts'
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        exclude = ('poll',)
        labels = {
            # 'poll': 'Aptauja',
            'question': 'Jautājums',
        }
        widgets = {
                'question': forms.TextInput(attrs={'class': '', 'autofocus': ''}),
        }


class ChoiseForm(ModelForm):
    class Meta:
        model = Choises
        exclude = ('choise_type',)
        labels = {
            'question': 'Jautājums',
            'option': 'Atbilde',
            'correct': 'Pareizā atbilde'
        }
        widgets = {
            'option': forms.TextInput(attrs={'autofocus': ''}),
            'correct': forms.CheckboxInput(attrs={'class': 'flag'})
        }
