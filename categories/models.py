from django.db import models


# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=255)

