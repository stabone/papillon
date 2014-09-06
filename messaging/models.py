#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Messages(models.Model):
	user_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender')
	user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reciever')
	title = models.CharField(max_length=255)
	message = models.TextField()
	red = models.BooleanField(default=False)
	trash = models.BooleanField(default=False)
	sent_at = models.DateTimeField(auto_now_add=True)

	class Meta:
            ordering = ['-sent_at']
            permissions = (
                ('inbox', 'Ziņas'),
                ('add_message', 'Sūtīt ziņas'),
                ('trash_message', 'Pārvietot uz miskasti'),
                ('delete_message', 'Dzēst ziņu'),
            )


class Contacts(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_me')
	contact_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_contact')
	added = models.DateTimeField(auto_now_add=True)

        class Meta:
            permissions = (
                ('add_contact', 'Pievienot kontaktu'),
                ('delete_contact', 'Dzēst kontaktu'),
            )
