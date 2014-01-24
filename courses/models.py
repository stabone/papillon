from django.db import models


# Create your models here.
class Categorie(models.Model):
    course = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.course


class Tut(models.Model):
    BEGINNER = '1'
    MEDIUM   = '2'
    ADVANCED = '3'
    LEVELS = (
        (BEGINNER, 'Iesacejs'),
        (MEDIUM,   'Videjs'),
        (ADVANCED, 'Gruts'),
    )
    categorie_id = models.ForeignKey(Categorie, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=1, choices=LEVELS, default=BEGINNER)
    # level = models.CharField(max_length=1)
    rating = models.IntegerField()
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

"""
class Material(models.Model):
    tut_id = models.ForeignKey(Tut, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='video/', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.BooleanField(default=False)
"""