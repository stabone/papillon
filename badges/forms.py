from django import forms #import ModelForm
from badges.models import Badges, BadgeTypes


class BadgeForm(forms.ModelForm):

    class Meta:
    i	model = Badges

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


