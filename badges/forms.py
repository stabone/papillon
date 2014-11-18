from django import forms
from badges.models import Badges, BadgeTypes


class BadgeForm(forms.ModelForm):

    class Meta:
        model = Badges

        fields = ('badge',)

        lables = {
            'badge': 'Nosaukums',
        }

        widgets = {
            'badge': forms.TextInput(attrs={'autofocus': ''})
        }


class BadgeTypeForm(forms.ModelForm):

    class Meta:
        model = BadgeTypes
        fields = ('title', 'description',)

        lables = {
            'title': 'Nosaukums',
            'description': 'Apraksts',
        }

        widgets = {
            'title': forms.TextInput(attrs={'autofocus': ''})
        }


