#-*- coding: utf-8 -*-
from django.forms import ModelForm

from messaging.models import Messages, Contacts


class MessagingForm(ModelForm):
    class Meta:
        model = Messages
        exclude = ('red', 'trash', 'sent_at',)
        labels = {
            'title': 'Virsraksts',
            'message': 'Ziņa',
            'red': 'Lasīts',
            'trash': 'Miskastē',
            'sent_at': 'Nosūtīts'
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contacts

