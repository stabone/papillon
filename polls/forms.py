#-*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from polls.models import (Polls, Questions, Choises, Answers, CorrectAnswers)

class PollForm(ModelForm):
    class Meta:
        model = Polls
        fields = ('public', 'poll', 'description',)
        labels = {
            'public': 'Publicēt?',
            'poll': 'Virsraksts',
            'description': 'Apraksts'
        }
        widgets = {
            'poll': forms.TextInput(attrs={'autofocus': ''})
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('question',)
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
        fields = ('question', 'option', 'correct',)
        labels = {
            'question': 'Jautājums',
            'option': 'Atbilde',
            'correct': 'Pareizā atbilde'
        }
        widgets = {
            'option': forms.TextInput(attrs={'autofocus': ''}),
            'correct': forms.CheckboxInput(attrs={'class': 'flag'})
        }


class AnswerForm(ModelForm):
    class Meta:
        model = Answers

        fields = ('question', 'answer',)

        labels = {
            'question': 'Jautājums',
            'answer': 'Atbilde',
        }

        widgets = {
            'answer': forms.TextInput(attrs={'autofocus': ''})
        }

