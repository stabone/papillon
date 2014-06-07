#-*- coding: utf-8 -*-
from django.db import models

# from courses.models import Materials
# from polls.models import Polls


class MaterialComments(models.Model):
    user = models.ForeignKey('auth.User')
    material = models.ForeignKey('courses.Materials')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PollComments(models.Model):
    user = models.ForeignKey('auth.User')
    poll = models.ForeignKey('polls.Polls')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


