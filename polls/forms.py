from django.forms import ModelForm

from polls.models import Polls, Questions, Choises

class PollForm(ModelForm):
    class Meta:
        model = Polls


class QuestionForm(ModelForm):
    class Meta:
        model = Questions


class ChoiseForm(ModelForm):
    class Meta:
        model = Choises
