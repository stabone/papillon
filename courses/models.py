from django.db import models

# Create your models here.
class Categorie(models.Model):
    course = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.course

class Tut(models.Model):
    categorie_id = models.ForeignKey(Categorie)
    # author_id = models.ForeignKey(Author) #one on one
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.IntegerField(default=0)
    rating = models.IntegerField()
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

