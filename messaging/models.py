from django.db import models
from django.conf import settings


class Messages(models.Model):
	user_from = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='sender')
	user_to = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='reciever')
	title = models.CharField(max_length=255)
	message = models.TextField()
	red = models.BooleanField(default=False)
	trash = models.BooleanField(default=False)
	sent_at = models.DateTimeField(auto_now_add=True)


class Contacts(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	added = models.DateTimeField(auto_now_add=True)
