from django.db import models


# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

