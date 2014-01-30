from django.db import models
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
        (BEGINNER, 'Iesacejs'),
        (MEDIUM,   'Videjs'),
        (ADVANCED, 'Gruts'),
    )
    categorie_id = models.ForeignKey(Categories, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=1, choices=LEVELS, default=BEGINNER)
    rating = models.PositiveSmallIntegerField(default=1)
    times_rated = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


def handle_file_upload(instance, filename):
    filename = "{0}_{1}".format(int(time()), filename)
    # instance.file.save(save=True)


class Materials(models.Model):
    tut_id = models.ForeignKey(Tuts, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to=handle_file_upload, max_length=255)
    post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

