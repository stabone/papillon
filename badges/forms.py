from django import forms
from badges.models import Badges


class BadgeForm(forms.ModelForm):

    class Meta:
        model = Badges

        fields = ('title',)

        lables = {
            'title': 'Nosaukums',
        }

        widgets = {
            'title': forms.TextInput(attrs={'autofocus': ''})
        }


