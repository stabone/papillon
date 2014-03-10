#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User
from time import time


# Create your models here.
class Categories(models.Model):
    course = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.course


class Tuts(models.Model):
    BEGINNER = '1'
    MEDIUM   = '2'
    ADVANCED = '3'
    LEVELS = (
        (BEGINNER, _('Iesācejs')),
        (MEDIUM,   _('Vidējs')),
        (ADVANCED, _('Grūts')),
    )
    category = models.ForeignKey(Categories, db_index=True)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=1, choices=LEVELS, default=BEGINNER)
    rating = models.PositiveSmallIntegerField(default=1)
    times_rated = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=255)
    post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


def handle_file_upload(instance, filename):
    filename = "{0}_{1}".format(int(time()), filename)
    # instance.file.save(save=True)


class Materials(models.Model):
    tut = models.ForeignKey(Tuts, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to=handle_file_upload, max_length=255)
    post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # @property
    # def video(self):
        # pass # for video property processing

