from django.db import models


class Messages(models.Model):
	user_from = models.ForeignKey('auth.User',related_name='sender') # user id (sender)
	user_to = models.ForeignKey('auth.User',related_name='reciever') # user id (reciever)
	title = models.CharField(max_length=255)
	message = models.TextField()
	red = models.BooleanField(default=False)
	trash = models.BooleanField(default=False)
	sent_at = models.DateTimeField(auto_now_add=True)


class Contacts(models.Model):
	user = models.ForeignKey('auth.User')
	added = models.DateTimeField(auto_now_add=True)
