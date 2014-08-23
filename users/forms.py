#-*- coding: utf-8 -*-
from django import forms
from users.models import CustomUser


class UserForm(forms.ModelForm):

    password1 = forms.CharField(label='Parole',
                            max_length=32,
                            min_length=6,
                            widget=forms.PasswordInput)
    password2 = forms.CharField(label='Parole atkārtoti',
                            max_length=32,
                            min_length=6,
                            widget=forms.PasswordInput,
                            help_text='Atkārtota parole')

    class Meta:
        model = CustomUser

        exclude = (
            'password', 'last_login',
            'is_superuser', 'image',
            'bio', 'is_active',
            'is_admin', 'groups',
            'user_permissions'
        )

        min_length = {
            'email': 10,
            'password': 6,
        }

        max_length = {
            'password': 32,
        }

        error_messages = {
            'password_mismatch': 'Norādītās paroles nesakrīt',
            'email': {
                'required': 'Lauks ir obligāts',
                'unique': 'Šāds epasts jau eksistē',
                'invalid': 'Norādītā epasta formāts ir nederīgs',
            },

            'password': {
                'required': 'Lauks ir obligāts',
                'max_length': 'Maksimālais atļauto simbolu skaits ir 32',
                'min_length': 'Minimālais simbolu skaits ir 6',
            },

            'password1': {
                'required': 'Lauks ir obligāts',
                'max_length': 'Maksimālais atļauto simbolu skaits ir 32',
                'min_length': 'Minimālais simbolu skaits ir 6',
            },

            'password2': {
                'required': 'Lauks ir obligāts',
                'max_length': 'Maksimālais atļauto simbolu skaits ir 32',
                'min_length': 'Minimālais simbolu skaits ir 6',
            }
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )

        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
