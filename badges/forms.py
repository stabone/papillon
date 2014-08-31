from django import forms
from badges.models import Badges, BadgeTypes


class BadgeForm(forms.ModelForm):

    class Meta:
        model = Badges

        exclude = ('user',)

        lables = {
            'title': 'Nosaukums',
        }

        widgets = {
            'title': forms.TextInput(attrs={'autofocus': ''})
        }


class BadgeTypeForm(forms.ModelForm):

    class Meta:
        model = BadgeTypes

        lables = {
            'title': 'Nosaukums',
            'description': 'Apraksts',
        }

        widgets = {
            'title': forms.TextInput(attrs={'autofocus': ''})
        }


