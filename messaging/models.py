from django.db import models


class Messages(models.Model):
	#sender = models.ForeignField('auth.User') user id (sender)
	#reciever = models.ForeignField('auth.User') user id (reciever)
	title = models.CharField(max_length=255)
	message = models.TextField()
	red = models.BooleanField(default=False)
	trash = models.BooleanField(default=False)
	sent_at = models.DateTimeField(auto_now_add=True)


class Contacts(models.Model):
	user = models.ForeignField('auth.User')
	added = models.DateTimeField(auto_now_add=True)
