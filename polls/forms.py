from django.forms import ModelForm

from polls.models import Polls, Choises

class PollForm(ModelForm):
    class Meta:
        model = Polls


class ChoiseForm(ModelForm):
    class Meta:
        model = Choises
