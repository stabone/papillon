from django.db import models


class Message(models.Model):
    # user = models.ForeignField(User) # reference to user model
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
