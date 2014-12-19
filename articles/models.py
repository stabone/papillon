#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

from time import time


def handle_file(instance, filename):
    filename = "".format()
    return filename


class Attachment(models.Model):
    title = models.CharField(max_length=255)
    entity = models.FileField(upload_to=handle_file)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class Articles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    embeded = models.TextField(blank=True)
    article = models.TextField(blank=True)
    modify  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        permissions = (
            ('index', 'Raksti'),
            ('add', 'Pievienot rakstu'),
            ('edit', 'Labot rakstu'),
            ('update', 'Atjaunot rakstu'),
            ('item', 'Apskatīt rakstu'),
            ('delete', 'Dzēst rakstu'),
        )


class Reviews(models.Model):
    article = models.ForeignKey(Articles, db_index=True)
    accept = models.BooleanField(default=True)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

