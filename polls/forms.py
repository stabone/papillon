from django.forms import ModelForm

from polls.models import Poll, Choise

class PollForm(ModelForm):
    class Meta:
        model = Poll


class ChoiseForm(ModelForm):
    class Meta:
        model = Choise
