from django.forms import ModelForm
from django import forms

from polls.models import Polls, Questions, Choises

class PollForm(ModelForm):
    class Meta:
        model = Polls
        exclude = ('user',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        widgets = {
                'question': forms.TextInput(attrs={'class': ''}),
        }


class ChoiseForm(ModelForm):
    class Meta:
        model = Choises
        exclude = ('choise_type',)
