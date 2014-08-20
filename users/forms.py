#-*- coding: utf-8 -*-
from django.forms import ModelForm
from users.models import CustomUser


class UserForm(ModelForm):

    class Meta:
        model = CustomUser

        min_length = {
            'email': 10,
            'password': 6,
        }

        max_length = {
            'password': 32,
        }

        error_messages = {
            'email': {
                'required': 'Lauks ir obligāts',
                'invalid': 'Norādītā epasta formāts ir nederīgs',
            }

            'password': {
                'required': 'Lauks ir obligāts',
                'max_length': 'Maksimālais atļauto simbolu skaits ir 32',
                'min_length': 'Minimālais simbolu skaits ir 6',
            }
        }
