#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

from helper.utils import random_string

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
        (BEGINNER, 'Iesācejs'),
        (MEDIUM,   'Vidējs'),
        (ADVANCED, 'Grūts'),
    )
    category = models.ForeignKey(Categories, db_index=True)
    author = models.ForeignKey('auth.User')
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


def get_file_extention(filename):
    extentio = filename.split('.')[-1].lower()
    return extentio


def handle_file_upload(instance, filename):
    filename = "{0}_{1}.{2}".format(
                        int(time()),
                        random_string(max=10),
                        get_file_extention(filename) )
    # print("{0}".format(filename))
    return filename


class Materials(models.Model):
    def verify_format(file):
        extension = get_file_extention(file.name)
        allowed_formats = ['mkv', 'webm', 'mp4']
        if extension not in allowed_formats:
            raise ValidationError('Atļautie formāti: %s' % ', '.join(allowed_formats))

    tut = models.ForeignKey(Tuts, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to=handle_file_upload, max_length=255, validators=[verify_format])
    post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

