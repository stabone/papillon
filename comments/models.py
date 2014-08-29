#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class MaterialComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    material = models.ForeignKey('courses.Materials')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
	ordering = ['-created_at']


class PollComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    poll = models.ForeignKey('polls.Polls')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
	ordering = ['-created_at']

