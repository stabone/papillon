from django.db import models

from courses.models import Materials

# Create your models here.
class MaterialComments(models.Model):
    material = models.ForeignKey(Materials)
    # user = this should come from session
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
