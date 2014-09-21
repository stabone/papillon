#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

from articles.models import Articles


class MaterialComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    material = models.ForeignKey('courses.Materials')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        permissions = (
            ('add_video_comments', 'Komentārs materiālam'),
            ('get_video_comments', 'Materiālu komentāri'),
        )


class PollComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    poll = models.ForeignKey('polls.Polls')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        permissions = (
            ('add_poll_comments', 'Komentārs aptauja'),
            ('get_poll_comments', 'Aptaujas  komentāri'),
        )


class ArticleComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    article = models.ForeignKey(Articles)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

