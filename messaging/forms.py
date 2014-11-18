#-*- coding: utf-8 -*-
from django.forms import ModelForm

from messaging.models import Messages, Contacts


class MessagingForm(ModelForm):

    class Meta:
        model = Messages

        fields = ('user_to', 'title', 'message',
                    'red', 'trash',)# 'sent_at',)

        labels = {
            'user_to': 'Saņēmējs',
            'title': 'Virsraksts',
            'message': 'Ziņa',
            'red': 'Lasīts',
            'trash': 'Miskastē',
            'sent_at': 'Nosūtīts'
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contacts

        fields = ('user', 'contact_user',)

        labels = {
            'user': 'Es',
            'contact_user': 'Lietotājs',
        }

