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
    title = models.CharField(max_length=255,blank=False)
    description = models.CharField(max_length=255,blank=False)
    # article = models.FileField(upload=handle_file_upload, )
    attachment = models.ForeignKey(Attachment)
    article = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

