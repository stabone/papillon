#-*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from polls.models import (Polls, Questions, Answers, CorrectAnswers)

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
        fields = ('poll', 'question',)
        labels = {
            'poll': 'Aptauja',
            'question': 'Jautājums',
        }
        widgets = {
            'question': forms.TextInput(attrs={'class': '', 'autofocus': ''}),
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

